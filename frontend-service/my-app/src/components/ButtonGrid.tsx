import React from 'react';
import logo from './logo.svg';
import './ButtonGrid.css';
import {useState} from 'react';

interface Props {
    id: number,
}

function ButtonGrid(props : Props) {

        const [state, toggle] = useState("OFF");

        const toggleOn = () => {
            toggle("ON");
            console.log('TURNING ON');
        };

        const toggleOff = () => {
            toggle("OFF");
            console.log('TURNING OFF');
        };

  return (
    <div className='Grid-Container'>
            <div className="row">
            <h2 id="b1"> {state}</h2>
        </div>
        {/* <div className="row">
            <h2 id="b1">Light #{props.id}: {state}</h2>
        </div> */}

        <div className="row">
            <div className ="hover:text-green-900"><button onClick = {toggleOn} className="on">On</button></div>
            <div className ="col"><button onClick = {toggleOff} className="off">Off</button></div>
        </div>

    </div> 
  );
}

export default ButtonGrid;
