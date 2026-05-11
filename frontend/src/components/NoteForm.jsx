import { useState } from 'react'
import '../styles/NoteForm.css'

export default function NoteForm({ onAddNote, loading }) {
  const [text, setText] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (text.trim()) {
      onAddNote(text)
      setText('')
    }
  }

  return (
    <form className="note-form" onSubmit={handleSubmit}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Bugün nasıl hissediyorsun? Notunu yaz..."
        disabled={loading}
        rows="4"
      />
      <button type="submit" disabled={loading || !text.trim()}>
        {loading ? '⏳ Analiz ediliyor...' : '✨ Analiz Et'}
      </button>
    </form>
  )
}
