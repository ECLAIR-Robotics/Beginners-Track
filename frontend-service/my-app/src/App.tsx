import React from 'react';
import logo from './logo.svg';
import TestImage from './static/Test.png'
import './App.css';
import './Maid (well, it IS a home automation system, and who takes care of homes).png'
import '../styles/card.css';
import TestButton from './components/TestButton'
import { useState, useEffect } from 'react';


/*
https://www.pluralsight.com/guides/how-to-use-the-map()-function-to-export-javascript-in-react?clickid=ztZzYd3-OxyPRO3XIcV5J3kyUkFToOWX0z5yUo0&irgwc=1&mpid=29332&aid=7010a000001xAKZAA2&utm_medium=digital_affiliate&utm_campaign=29332&utm_source=impactradius
https://legacy.reactjs.org/docs/lists-and-keys.html

get rid of ALL the test buttons --> have one map function and add a button for element in the array of relays

for each button created --> need to be able to remove if necessary (POST request to /relay/delete)

what if client wants to add relay? how to get that input?
  - some button that sends a POST request to /relay/add


NOTES:
to test if backend api is working, need to ssh in raspi: 
  user: krithi@ipaddress
  pw: 12345678
    cd Beginners-Track/backend-service
    python3 -m base
  then go back to your local terminal and run npm start in my-app
  
  if backend api isn't working pls write down which requests you aren't able to fulfill and lmk
  if there's anything weird going on
    see api requests in backend-service/core/views.py
  
 */
function App() {
  return (
    <header>
      <img src={logo} className="App-logo" alt="logo" />
      <img src={TestImage} className="Funny" alt="Maid" />
      <h2> *Hey, it's a HOME Automation System, and who takes care of homes? Maids, of course! </h2>
      <h1> Home Automation System </h1>
      <div className="flex-container">
        <TestButton text="Light #1" />
        <TestButton text="Light #2" />
        <TestButton text="Light #3" />
        <TestButton text="Fan #1" />
        <TestButton text="Fan #2" />
        <TestButton text="Fan #3" />
      </div>
    </header>
  );
}

export default App;

/*
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
*/