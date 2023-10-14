import React from 'react';
import logo from './logo.svg';
import {useState, useEffect} from 'react';
import './App.css';

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
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}

export default App;
