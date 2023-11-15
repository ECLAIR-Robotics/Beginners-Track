import React from 'react';
import logo from './logo.svg';
import Image from './static/Test.png'
import './App.css';
// import '../styles/card.css';
import Button from './components/RelayButton'
import { useState, useEffect } from 'react';
import AddForm from './components/AddForm';


/*
https://www.pluralsight.com/guides/how-to-use-the-map()-function-to-export-javascript-in-react?clickid=ztZzYd3-OxyPRO3XIcV5J3kyUkFToOWX0z5yUo0&irgwc=1&mpid=29332&aid=7010a000001xAKZAA2&utm_medium=digital_affiliate&utm_campaign=29332&utm_source=impactradius
https://legacy.reactjs.org/docs/lists-and-keys.html

get rid of ALL the test buttons --> have one map function and add a button for element in the array of relays

for each button created --> need to be able to remove if necessary (POST request to /relay/delete)

what if client wants to add relay? how to get that input?
  - some button that sends a POST request to /relay/add

see demo files for examples

NOTES:
to test if backend api is working, need to ssh in raspi: 
  user: krithi@ipaddress
  pw: 12345678
    cd Beginners-Track/backend-service
    python3 -m base
  then go back to your local terminal and run npm start in my-app

    see api requests in backend-service/core/views.py


    notes: 

    useeffect 
    usestate: give your website a state



  
 */

function App() {

  // const [data, setData] = useState({ message: "" })
  // const [clicked, setClicked] = useState(false);

  // useEffect(() => {
  //   fetch(`http://10.159.66.57:5000/relay/add`) // WRONG URL
  //     .then(res => res.json())
  //     .then(data => setData(data))
  // }, []);
  // useEffect(() => {
  //   console.log(data)
  // }, [data]);

  // const handleClick = () => {
  //   setClicked(!clicked);
  //   console.log(clicked)
  // };

  // const callBackend = () => {
  //   // fetch the backend url (local host 5000 / whatever ?data=${testData})

  // }


  return (
    <main className="">

      <h1 className="mx-auto container flex justify center mt-20">
        random tailwind practice thingy
      </h1>

      <h2 className="mx-auto container flex justify center mt-20">
        <AddForm></AddForm>
      </h2>

    </main>
  );
}

export default App;


/* <img src={logo} className="App-logo" alt="logo" />
      <img src={TestImage} className="Funny" alt="Maid" />
      <h2> *Hey, it's a HOME Automation System, and who takes care of homes? Maids, of course! </h2>
      <h1> Home Automation System </h1>
      <div className="flex-container">
        <Button text="Application" />
      </div> */