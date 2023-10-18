import { Routes, Route } from "react-router-dom"
import ANA from './components/AddNewAppliances';
import ButtonGrid from './components/ButtonGrid';
import React from 'react';
import logo from './logo.svg';
import './App.css';
import './components/Footer';
import { Link } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        </a>
      </header>
      <Routes>
        <Route path="Grid" element={ <ButtonGrid/> } />
        <Route path="ANA" element={ <ANA/> } />
      </Routes>
      <Link to="Grid">Click to view the Grid page</Link>
      <Link to="ANA">Click to view the ANA page</Link>
    </div>
  );
} 

export default App;
