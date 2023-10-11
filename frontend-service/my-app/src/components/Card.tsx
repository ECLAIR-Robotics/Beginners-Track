import React from 'react';
import logo from '../logo.svg';
import TestImage from '../static/Test.png'
import '../App.css';
import '../styles/card.css';
import TestButton from './TestButton'

function Card() {
  return (

    <header>
      <img src={logo} className="App-logo" alt="logo" />
      <img src={TestImage} className="Funny" alt="Maid" />
      <h2> *Hey, it's a HOME Automation System, and who takes care of homes? Maids, of course! </h2>
      <h1> Home Automation System </h1>
      <div className="flex-container">
        <TestButton text="Light #1"/>
        <TestButton text="Light #2"/>
        <TestButton text="Light #3"/>
        <TestButton text="Fan #1"/>
        <TestButton text="Fan #2"/>
        <TestButton text="Fan #3"/>
      </div>
    </header>
  );
}



export default Card;