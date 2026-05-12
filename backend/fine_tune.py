import torch
import pandas as pd
from pathlib import Path
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)
from datasets import Dataset
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

torch.manual_seed(42)

BATCH_SIZE = 4
GRADIENT_ACCUMULATION_STEPS = 4
NUM_EPOCHS = 15
LEARNING_RATE = 1e-5
WARMUP_STEPS = 200
MODEL_NAME = "xlm-roberta-base"
OUTPUT_DIR = "./fine_tuned_model"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

logger.info(f"Using device: {DEVICE}")
logger.info(f"Batch size: {BATCH_SIZE} (Effective: {BATCH_SIZE * GRADIENT_ACCUMULATION_STEPS})")


def print_gpu_stats(prefix=""):
    if torch.cuda.is_available():
        allocated = torch.cuda.memory_allocated(0) / 1e9
        reserved = torch.cuda.memory_reserved(0) / 1e9
        total = torch.cuda.get_device_properties(0).total_memory / 1e9

        temp = "N/A"
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader'],
                capture_output=True, text=True, timeout=2
            )
            if result.returncode == 0:
                temp = result.stdout.strip()
        except FileNotFoundError:
            pass

        logger.info(f"{prefix}GPU: {allocated:.2f}GB/{reserved:.2f}GB (Total: {total:.2f}GB) | Temp: {temp}C")

        if float(allocated) > total * 0.9:
            logger.warning("GPU memory usage > 90%!")
            torch.cuda.empty_cache()


def load_data():
    logger.info("Loading data...")
    data_dir = Path("data")

    train_df = pd.read_csv(data_dir / "train.csv")
    val_df = pd.read_csv(data_dir / "validation.csv")

    logger.info(f"Train samples: {len(train_df)}")
    logger.info(f"Val samples: {len(val_df)}")

    train_dataset = Dataset.from_pandas(train_df)
    val_dataset = Dataset.from_pandas(val_df)

    return train_dataset, val_dataset


def preprocess_function(examples, tokenizer):
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=128,
        padding="max_length"
    )


def compute_class_weights(dataset):
    from collections import Counter
    labels = [item['label'] for item in dataset]
    label_counts = Counter(labels)
    total = len(labels)
    num_classes = len(label_counts)
    weights = {}
    for label, count in label_counts.items():
        weights[label] = total / (num_classes * count)
    logger.info(f"Class weights: {weights}")
    return weights


def main():
    logger.info("=" * 60)
    logger.info("FINE-TUNING SENTIMENT MODEL - GPU SAFE")
    logger.info("=" * 60)

    try:
        logger.info("Loading model and tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME,
            num_labels=3,
            id2label={0: "negative", 1: "neutral", 2: "positive"},
            label2id={"negative": 0, "neutral": 1, "positive": 2}
        )
        model.to(DEVICE)
        print_gpu_stats("[AFTER MODEL LOAD] ")

        train_dataset, val_dataset = load_data()

        logger.info("Tokenizing datasets...")
        train_dataset = train_dataset.map(
            lambda x: preprocess_function(x, tokenizer),
            batched=True,
            remove_columns=["text"]
        )
        val_dataset = val_dataset.map(
            lambda x: preprocess_function(x, tokenizer),
            batched=True,
            remove_columns=["text"]
        )

        training_args = TrainingArguments(
            output_dir=OUTPUT_DIR,
            num_train_epochs=NUM_EPOCHS,
            per_device_train_batch_size=BATCH_SIZE,
            per_device_eval_batch_size=BATCH_SIZE,
            gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
            warmup_steps=WARMUP_STEPS,
            weight_decay=0.01,
            logging_dir="./logs",
            logging_steps=50,
            eval_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            metric_for_best_model="eval_loss",
            learning_rate=LEARNING_RATE,
            dataloader_pin_memory=True,
            dataloader_num_workers=0,
            fp16=torch.cuda.is_available(),
            gradient_checkpointing=True,
            max_grad_norm=1.0,
        )

        data_collator = DataCollatorWithPadding(tokenizer)

        import torch.nn as nn
        class_weights = compute_class_weights(train_dataset)
        weights = torch.tensor([class_weights[i] for i in range(3)], dtype=torch.float).to(DEVICE)

        class CustomTrainer(Trainer):
            def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
                labels = inputs.pop("labels")
                outputs = model(**inputs)
                logits = outputs.logits
                loss_fct = nn.CrossEntropyLoss(weight=weights)
                loss = loss_fct(logits.view(-1, self.model.config.num_labels), labels.view(-1))
                return (loss, outputs) if return_outputs else loss

        trainer = CustomTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            data_collator=data_collator,
        )

        logger.info("Starting training...")
        print_gpu_stats("[BEFORE TRAINING] ")

        train_result = trainer.train()

        print_gpu_stats("[AFTER TRAINING] ")

        logger.info("Saving model...")
        trainer.save_model(OUTPUT_DIR)
        tokenizer.save_pretrained(OUTPUT_DIR)

        logger.info(f"Model saved to: {OUTPUT_DIR}")
        logger.info("Training completed successfully!")
        logger.info(f"Training loss: {train_result.training_loss:.4f}")

        logger.info("Cleaning up GPU memory...")
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        print_gpu_stats("[AFTER CLEANUP] ")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except RuntimeError as e:
        logger.error(f"Runtime error: {e}")
        raise
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise


if __name__ == "__main__":
    main()
