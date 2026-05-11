import { useState, useEffect } from 'react'
import './App.css'
import NoteForm from './components/NoteForm'
import NoteList from './components/NoteList'
import Dashboard from './components/Dashboard'
import axios from 'axios'

function App() {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(false)

  const API_URL = 'http://localhost:5000/api'

  useEffect(() => {
    fetchNotes()
  }, [])

  const fetchNotes = async () => {
    try {
      const response = await axios.get(`${API_URL}/notes`)
      setNotes(response.data)
    } catch (error) {
      console.error('Notes fetch error:', error)
    }
  }

  const handleAddNote = async (noteText) => {
    setLoading(true)
    try {
      const response = await axios.post(`${API_URL}/analyze`, {
        text: noteText
      })
      const newNote = {
        id: Date.now(),
        text: noteText,
        sentiment: response.data.sentiment,
        score: response.data.score,
        timestamp: new Date().toLocaleString()
      }
      setNotes([newNote, ...notes])
    } catch (error) {
      console.error('Add note error:', error)
      alert('Not eklenirken hata oluştu')
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
        <h1>💭 Duygu Analiz Notesi</h1>
        <p>Notlarını yaz, duygu durumunu anla</p>
      </header>

      <main className="app-main">
        <NoteForm onAddNote={handleAddNote} loading={loading} />
        <Dashboard notes={notes} />
        <NoteList notes={notes} onDeleteNote={handleDeleteNote} />
      </main>
    </div>
  )
}

export default App
