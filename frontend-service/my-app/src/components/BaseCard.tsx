import React from 'react';
import {useState} from 'react';
import ButtonGrid from './ButtonGrid';

interface Props{
    Name : string
    Text : string
    ID : number
}

function BaseCard({Name, Text, ID} : Props) {

  
  return (
    <div className = "Container">
        <h1 className = "Header">    
           {Name} 
        </h1>
        <p className = "Description">
            {Text}
        </p>
        <div className = "id">   
        <ButtonGrid id = {ID}/>    
        </div>
    </div>
  );
}

export default BaseCard;
