import { useState, useEffect } from 'react'
import './App.css'
import NoteForm from './components/NoteForm'
import NoteList from './components/NoteList'
import Dashboard from './components/Dashboard'
import axios from 'axios'

function App() {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

  useEffect(() => {
    fetchNotes()
  }, [])

  const fetchNotes = async () => {
    try {
      setError(null)
      const response = await axios.get(`${API_URL}/notes`)
      setNotes(response.data)
    } catch (error) {
      console.error('Fetch notes error:', error)
      setError('Failed to load notes')
    }
  }

  const handleAddNote = async (noteText) => {
    if (!noteText?.trim()) return

    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/analyze`, {
        text: noteText
      })

      const newNote = {
        id: Date.now() + Math.random(),
        text: noteText,
        sentiment: response.data.sentiment || 'neutral',
        score: response.data.score || 0,
        timestamp: new Date().toLocaleString()
      }
      setNotes([newNote, ...notes])
    } catch (error) {
      console.error('Add note error:', error)
      setError(error.response?.data?.error || 'Failed to analyze note')
    } finally {
      setLoading(false)
    }
  }

  const handleDeleteNote = (id) => {
    setNotes(notes.filter(note => note.id !== id))
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Sentiment Analysis Notes</h1>
        <p>Write your thoughts, understand your feelings</p>
      </header>

      {error && <div className="error-banner">{error}</div>}

      <main className="app-main">
        <NoteForm onAddNote={handleAddNote} loading={loading} />
        <Dashboard notes={notes} />
        <NoteList notes={notes} onDeleteNote={handleDeleteNote} />
      </main>
    </div>
  )
}

export default App
