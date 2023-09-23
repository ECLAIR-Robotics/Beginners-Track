import React from 'react';
import logo from './logo.svg';
import './App.css';
import './Thing.css';
import TestButton from './components/TestButton'

function Thing() {
  return (

    <header>
      <p> This is just a test for the frontend of the E-Clair Beginner's Track project. </p>
      <div className='flex-container'>
        <TestButton />
        <TestButton />
        <TestButton />
        <TestButton />
        <TestButton />
        <TestButton />
      </div>
    </header>

  );
}

export default Thing;

