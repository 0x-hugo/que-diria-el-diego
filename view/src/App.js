import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

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
    <Box 
      position="relative" 
      sx={{ 
        height: '100vh',
        width: '100vw',
        padding: '2rem', 
        backgroundImage: `url(https://cdn.britannica.com/76/124976-050-E03E50CE/Diego-Maradona-1986.jpg)`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
      }}
    >
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <Typography variant="h4" color="white">Que diria el Diego</Typography>
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
        <Typography id="response" color="white">{response}</Typography>
      </Box>
    </Box>
  );
}

export default App;
