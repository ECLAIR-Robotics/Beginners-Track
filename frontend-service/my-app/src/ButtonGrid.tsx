import React from 'react';
import logo from './logo.svg';
import './ButtonGrid.css';

function ButtonGrid() {
  return (
    <div>
        <header>
            <h1 id="Title">A very cool website</h1>
        </header>

        <div className='Grid-Container'>
            
            <div className="row">
                <h2>Light #1</h2>
            </div>

            <div className="row">
                <div className ="col"><button className="on">On</button></div>
                <div className ="col"><button className="off">Off</button></div>
            </div>

            <div className="row">
                <h2>Light #2</h2>
            </div>

            <div className="row">
                <div className ="col"><button className="on">On</button></div>
                <div className ="col"><button className="off">Off</button></div>
            </div>

            <div className="row">
                <h2>Light #3</h2>
            </div>

            <div className="row">
                <div className ="col"><button className="on">On</button></div>
                <div className ="col"><button className="off">Off</button></div>
            </div>
        </div> 
    </div>
  );
}

export default ButtonGrid;
