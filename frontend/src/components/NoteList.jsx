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

export default function NoteList({ notes, onDeleteNote }) {
  return (
    <div className="note-list">
      <h2>📝 Tüm Notlar ({notes.length})</h2>
      {notes.length === 0 ? (
        <p className="empty-state">Henüz not eklemeddin. Başla! 🚀</p>
      ) : (
        <div className="notes-grid">
          {notes.map(note => (
            <div
              key={note.id}
              className="note-card"
              style={{ borderLeftColor: sentimentColor[note.sentiment] }}
            >
              <div className="note-header">
                <span className="sentiment-emoji">
                  {sentimentEmoji[note.sentiment]}
                </span>
                <span className="sentiment-label">
                  {note.sentiment === 'positive' && 'Pozitif'}
                  {note.sentiment === 'negative' && 'Negatif'}
                  {note.sentiment === 'neutral' && 'Tarafsız'}
                </span>
                <span className="score">({(note.score * 100).toFixed(0)}%)</span>
              </div>
              <p className="note-text">{note.text}</p>
              <div className="note-footer">
                <span className="timestamp">{note.timestamp}</span>
                <button
                  className="delete-btn"
                  onClick={() => onDeleteNote(note.id)}
                >
                  🗑️
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
