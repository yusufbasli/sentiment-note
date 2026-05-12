import torch
import subprocess

print("=" * 60)
print("GPU CHECK - Sentiment Analysis Fine-tuning")
print("=" * 60)

# PyTorch CUDA Check
print(f"\n[OK] PyTorch Version: {torch.__version__}")
print(f"[OK] CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"[OK] GPU Count: {torch.cuda.device_count()}")
    print(f"[OK] Current GPU: {torch.cuda.current_device()}")
    print(f"[OK] GPU Name: {torch.cuda.get_device_name(0)}")

    props = torch.cuda.get_device_properties(0)
    total_mem = props.total_memory / 1e9
    print(f"[OK] GPU Memory: {total_mem:.2f} GB")
    print(f"[OK] CUDA Version: {torch.version.cuda}")

    # Current memory usage
    allocated = torch.cuda.memory_allocated(0) / 1e9
    reserved = torch.cuda.memory_reserved(0) / 1e9
    print(f"\nMemory Usage:")
    print(f"   - Allocated: {allocated:.2f} GB")
    print(f"   - Reserved: {reserved:.2f} GB")
    print(f"   - Available: {total_mem - reserved:.2f} GB")

    # nvidia-smi check
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader'],
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            temp = result.stdout.strip()
            print(f"\nGPU Temperature: {temp}C")
    except FileNotFoundError:
        print("\n[INFO] nvidia-smi not available (normal on some systems)")
    except subprocess.TimeoutExpired:
        print("\n[INFO] nvidia-smi timeout")

    print("\n[OK] GPU STATUS: READY FOR FINE-TUNING")
    print(f"   - Safe batch size: 8-16")
    print(f"   - Estimated training time: 15-30 minutes")
else:
    print("\n[ERROR] GPU NOT DETECTED - CPU training will be very slow")
    print("   Consider using Google Colab or cloud GPU instead")

print("=" * 60)
