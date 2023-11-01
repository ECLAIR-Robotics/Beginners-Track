import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './AddNewAppliances.css';
import { Link, useNavigate } from 'react-router-dom';

function ANA() {
  // const nameTextBox = document.createElement("input")
  // nameTextBox.type = "text"
  // nameTextBox.placeholder = "Enter new appliance"

  const [name, setName] = useState<String>('')
  
  useEffect(()=>{
    console.log(name)
  }, [name])

  const nav = useNavigate()
    const changePage = () => {
      nav('/')
    }
    return (
      <div>
          <header>
              <h1 className="text-3xl font-bold underline #0f172a">Add new appliances here</h1>
          </header>

          <div className =".row">
            <div className='Appliance Name'>
                Name: <input className="name-input" onChange={e => setName(e.target.value)} type="text" placeholder="Enter appliance name" />
            </div> 
          </div>

          <div className =".row">
            <div className='Appliance Description'>
                Description: <input className="description-input" type="text" placeholder="Enter description" />
            </div> 
          </div>

          <div className =".row">
            <div className='Appliance ID'>
                ID: <input className="id-input" type="text" placeholder="Enter appliance ID" />
            </div> 
          </div>

        <button className='bg-gray-500'>Submit</button>

        <button className='bg-rose-300' onClick={changePage}>Go to Main Page</button>
      </div>
    );
  }
  
export default ANA
  