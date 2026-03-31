import { useEffect, useState } from 'react'

function App() {
  const [players, setPlayers] = useState<string[]>([])
  const [status, setStatus] = useState<string>('unknown')

  useEffect(() => {
    fetch('/api/players')
      .then(r => r.json())
      .then(data => setPlayers(data.players ?? []))

    fetch('/api/startup')
      .then(r => r.json())
      .then(data => setStatus(data.status))
  }, [])

  return (
    <div>
      <h1>Minecraft Dashboard</h1>
      <p>Server status: {status}</p>
      <h2>Players online: {players.length}</h2>
      <ul>
        {players.map(p => <li key={p}>{p}</li>)}
      </ul>
    </div>
  )
}

export default App