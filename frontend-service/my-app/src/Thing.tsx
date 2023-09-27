import React from 'react';
import logo from './logo.svg';
import './App.css';
import './Thing.css';
import TestButton from './components/TestButton'

function Thing() {
  return (

    <header>
      <h1> Home Automation System </h1>
      <div className="flex-container">
        <TestButton text="Light #1"/>
        <TestButton text="Light #2"/>
        <TestButton text="Light #3"/>
        <TestButton text="Placeholder #1"/>
        <TestButton text="Placeholder #2"/>
        <TestButton text="Placeholder #3"/>
      </div>
    </header>

  );
}

export default Thing;