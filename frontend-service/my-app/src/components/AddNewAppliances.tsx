import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './AddNewAppliances.css';
import { Link, useNavigate } from 'react-router-dom';

function ANA() {
  // const nameTextBox = document.createElement("input")
  // nameTextBox.type = "text"
  // nameTextBox.placeholder = "Enter new appliance"

  const [name, setName] = useState<String>('')
  const [desc, setDesc] = useState<String>('')
  const [id, setID] = useState<String>('')

  const callBackend = () => {
    console.log("backend:")
    fetch(`http://10.159.65.255:5000/relay/add`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              'name': name,
              'desc': desc,
              'id': id
          }
          )
        }
    )
        .then(response => response.json())
        .then(data => {
            console.log(data["message"])
        })
  }

  function handleClick() {
    console.log('Submitted name:', name);
    console.log('Submitted desc:', desc);
    console.log('Submitted ID:', id);
  }

  function handleInput() {
    // TODO: Make this later, check if input is valid
  }
  
  // useEffect(()=>{
  //   console.log('name:', name)
  //   console.log('desc:', desc)
  //   console.log('id:', id)
  // }, [name, desc, id])

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
                Description: <input className="description-input" onChange={e => setDesc(e.target.value)} type="text" placeholder="Enter description" />
            </div> 
          </div>

          <div className =".row">
            <div className='Appliance ID'>
                ID: <input className="id-input" onChange={e => setID(e.target.value)} type="number" placeholder="Enter appliance ID" />
            </div> 
          </div>

        <button className='bg-gray-500' onClick={callBackend}>Submit</button>

        <button className='bg-rose-300' onClick={changePage}>Go to Main Page</button>
      </div>
    );
  }
  
export default ANA
  