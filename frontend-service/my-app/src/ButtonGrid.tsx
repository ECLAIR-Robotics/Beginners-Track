import React from 'react';
import logo from './logo.svg';
import './ButtonGrid.css';

function Component() {
  return (
    <div>
        <header>
            <h1 id="Title">Hello World</h1>
        </header>

        <div className='Grid-Container'>
            <div className="row">
                <div className ="col"><button>1</button></div>
                <div className ="col"><button>2</button></div>
            </div>

            <div className="row">
                <div className ="col"><button>1</button></div>
                <div className ="col"><button>2</button></div>
            </div>

            <div className="row">
                <div className ="col"><button>1</button></div>
                <div className ="col"><button>2</button></div>
            </div>
        </div> 
    </div>
  );
}

export default Component;
