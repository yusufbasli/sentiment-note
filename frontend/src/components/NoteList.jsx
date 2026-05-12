import '../styles/NoteList.css'

const sentimentEmoji = {
  positive: '😊',
  negative: '😔',
  neutral: '😐'
}

const sentimentColor = {
  positive: '#4ade80',
  negative: '#ef4444',
  neutral: '#94a3b8'
}

const sentimentLabel = {
  positive: 'Positive',
  negative: 'Negative',
  neutral: 'Neutral'
}

export default function NoteList({ notes, onDeleteNote }) {
  return (
    <div className="note-list">
      <h2>All Notes ({notes.length})</h2>
      {notes.length === 0 ? (
        <p className="empty-state">No notes yet. Start writing!</p>
      ) : (
        <div className="notes-grid">
          {notes.map(note => {
            const sentiment = note.sentiment || 'neutral'
            const color = sentimentColor[sentiment] || sentimentColor.neutral
            const emoji = sentimentEmoji[sentiment] || sentimentEmoji.neutral
            const label = sentimentLabel[sentiment] || 'Unknown'

            return (
              <div
                key={note.id}
                className="note-card"
                style={{ borderLeftColor: color }}
              >
                <div className="note-header">
                  <span className="sentiment-emoji">{emoji}</span>
                  <span className="sentiment-label">{label}</span>
                  <span className="score">({Math.round((note.score || 0) * 100)}%)</span>
                </div>
                <p className="note-text">{note.text}</p>
                <div className="note-footer">
                  <span className="timestamp">{note.timestamp}</span>
                  <button
                    className="delete-btn"
                    onClick={() => onDeleteNote(note.id)}
                    aria-label="Delete note"
                  >
                    Delete
                  </button>
                </div>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
