import React from 'react';
import logo from './logo.svg';
import './ButtonGrid.css';
import { Link } from 'react-router-dom';

function ANA() {
    return (
      <div>
          <header>
              <h1 id="Title">Add new appliances here</h1>
          </header>
  
          <div className='Add Appliances'>
            <input className="appliance-input" type="text" placeholder="Enter New Appliance" />
          </div> 
      </div>
    );
  }
  
export default ANA
  