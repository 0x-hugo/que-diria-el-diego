import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleClick = () => {
    let localhost = 'http://localhost:5005';
    let path = '/ask';
    let query = `prompt=${encodeURIComponent(prompt)}`;
    fetch(`${localhost}${path}?${query}`)
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
        setResponse(json.data);
      });
  };

  return (
    <div style={{ padding: '2rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <Typography variant="h4">Que diria el Diego</Typography>
      <TextField
        id="prompt"
        variant="outlined"
        label="Tu pregunta"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <Button variant="contained" color="primary" onClick={handleClick}>
        Preguntale al más grande
      </Button>
      <Typography id="response">{response}</Typography>
    </div>
  );
}

export default App;
