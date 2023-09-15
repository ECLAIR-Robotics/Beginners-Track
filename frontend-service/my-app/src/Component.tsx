import React from 'react';
import logo from './logo.svg';
import './Component.css';

function Component() {
  return (
    <div>
        <header>
            <h1 id="Title">Hello World</h1>
        </header>

        <div className='Grid-Container'>
            <div className="row">
                <div className ="item1"><button>1</button></div>
                <div className ="item2"><button>2</button></div>
            </div>
            
            <div className ="grid-item"><button>3</button></div>
            <div className ="grid-item"><button>4</button></div>
            <div className ="grid-item"><button>5</button></div>
            <div className ="grid-item"><button>6</button></div>
        </div>

        
    </div>
    



  );
}

export default Component;
