import React from 'react';
import logo from './logo.svg';
import './ButtonGrid.css';
import { Link, useNavigate } from 'react-router-dom';

function ANA() {
  const nav = useNavigate()
    const changePage = () => {
      nav('/')
    }
    return (
      <div>
          <header>
              <h1 id="Title">Add new appliances here</h1>
          </header>
  
          <div className='Add Appliances'>
            <input className="appliance-input" type="text" placeholder="Enter New Appliance" />
          </div> 
        <button onClick={changePage}>Go to Main Page</button>

      </div>
    );
  }
  
export default ANA
  