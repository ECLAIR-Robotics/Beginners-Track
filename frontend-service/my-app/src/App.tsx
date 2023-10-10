import React from 'react';
import logo from './logo.svg';
import TestImage from './static/Test.png'
import './App.css';
import './Maid (well, it IS a home automation system, and who takes care of homes).png'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <img src={TestImage} className="Funny" alt="Maid"/>
      </header>
    </div>
  );
}

export default App;