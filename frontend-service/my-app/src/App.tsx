import { Routes, Route } from "react-router-dom"
import ANA from './components/AddNewAppliances';
import ButtonGrid from './components/ButtonGrid';
import MainPage from './components/MainPage';
import React from 'react';
import logo from './logo.svg';
import './App.css';
import './components/Footer';
import { Link } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      
      <Routes>

        <Route path="/" element={ <MainPage/> } />
        <Route path="/ANA" element={ <ANA/> } />
      </Routes>
      {/* <Link to="Grid">Click to view the Grid page</Link>
      <Link to="ANA">Click to view the ANA page</Link> */}
    </div>
  );
} 

export default App;
