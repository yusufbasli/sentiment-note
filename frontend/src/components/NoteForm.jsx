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

  const handleChange = (e) => {
    const value = e.target.value
    if (value.length <= 1024) {
      setText(value)
    }
  }

  return (
    <form className="note-form" onSubmit={handleSubmit}>
      <textarea
        value={text}
        onChange={handleChange}
        placeholder="What's on your mind today?"
        disabled={loading}
        rows="4"
        maxLength="1024"
      />
      <div className="form-footer">
        <span className="char-count">{text.length}/1024</span>
        <button type="submit" disabled={loading || !text.trim()}>
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </div>
    </form>
  )
}
