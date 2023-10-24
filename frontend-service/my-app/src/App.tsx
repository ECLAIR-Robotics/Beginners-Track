import React from 'react';
import logo from './logo.svg';
import TestImage from './static/Test.png'
import {useState, useEffect} from 'react';
import './App.css';
import './Maid (well, it IS a home automation system, and who takes care of homes).png'
import '../styles/card.css';
import TestButton from './components/TestButton'


/*
https://www.pluralsight.com/guides/how-to-use-the-map()-function-to-export-javascript-in-react?clickid=ztZzYd3-OxyPRO3XIcV5J3kyUkFToOWX0z5yUo0&irgwc=1&mpid=29332&aid=7010a000001xAKZAA2&utm_medium=digital_affiliate&utm_campaign=29332&utm_source=impactradius
https://legacy.reactjs.org/docs/lists-and-keys.html

get rid of all the test buttons --> have one map function and add a button for element in the array of relays
for each button created --> need to be able to remove if necessary and rename
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
  const [data, setData] = useState({message: ""})
  const [clicked, setClicked] = useState(false);
  useEffect(() => { 
    fetch(`http://10.159.65.135:5000/`)
      .then(res => res.json())
      .then(data => setData(data))
  }, []);
  useEffect(() => {
    console.log(data)
  }, [data]);

  const handleClick = () => { 
    setClicked(!clicked);
    console.log(clicked)
  };
  // React.useEffect(() => {
  //   console.log(data)
  // }, [data]);

  // return (
  //   
  // );

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
      </header>
    </div>
  );
}

export default App;
*/