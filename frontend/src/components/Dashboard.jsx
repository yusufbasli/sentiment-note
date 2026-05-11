import { useMemo } from 'react'
import '../styles/Dashboard.css'

export default function Dashboard({ notes }) {
  const stats = useMemo(() => {
    const total = notes.length
    const positive = notes.filter(n => n.sentiment === 'positive').length
    const negative = notes.filter(n => n.sentiment === 'negative').length
    const neutral = notes.filter(n => n.sentiment === 'neutral').length

    return {
      total,
      positive,
      negative,
      neutral,
      positivePercent: total > 0 ? ((positive / total) * 100).toFixed(0) : 0,
      negativePercent: total > 0 ? ((negative / total) * 100).toFixed(0) : 0,
      neutralPercent: total > 0 ? ((neutral / total) * 100).toFixed(0) : 0
    }
  }, [notes])

  if (stats.total === 0) return null

  return (
    <div className="dashboard">
      <h2>📊 İstatistikler</h2>
      <div className="stats-container">
        <div className="stat-card positive">
          <div className="emoji">😊</div>
          <div className="info">
            <div className="label">Pozitif</div>
            <div className="value">{stats.positive}</div>
            <div className="percent">{stats.positivePercent}%</div>
          </div>
        </div>

        <div className="stat-card negative">
          <div className="emoji">😔</div>
          <div className="info">
            <div className="label">Negatif</div>
            <div className="value">{stats.negative}</div>
            <div className="percent">{stats.negativePercent}%</div>
          </div>
        </div>

        <div className="stat-card neutral">
          <div className="emoji">😐</div>
          <div className="info">
            <div className="label">Tarafsız</div>
            <div className="value">{stats.neutral}</div>
            <div className="percent">{stats.neutralPercent}%</div>
          </div>
        </div>

        <div className="stat-card total">
          <div className="emoji">📝</div>
          <div className="info">
            <div className="label">Toplam Not</div>
            <div className="value">{stats.total}</div>
            <div className="percent">100%</div>
          </div>
        </div>
      </div>

      <div className="progress-bar">
        <div className="bar positive" style={{ width: `${stats.positivePercent}%` }}></div>
        <div className="bar negative" style={{ width: `${stats.negativePercent}%` }}></div>
        <div className="bar neutral" style={{ width: `${stats.neutralPercent}%` }}></div>
      </div>
    </div>
  )
}
