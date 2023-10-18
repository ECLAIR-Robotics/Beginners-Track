import React from 'react';
import ReactDOM from 'react-dom/client';
import Footer from './Footer';
import ButtonGrid from './ButtonGrid';
import TestButton from './TestButton';
import BaseCard from './BaseCard';

function MainPage() {
    
  return (
    <div>
      {/* <TestButton title = {"Cool Button"} statingValue= {5}/>remove this and import when you are done using it*/ }
        {/* <TestButton title = {"Bad Button"} statingValue= {25}/>remove this and import when you are done using it*/ }
        {/* <ButtonGrid id={1}/>
        <ButtonGrid id={2}/>
        <ButtonGrid id={3}/> */}
        <BaseCard Name = {"Light1"} Text = {"Light1"} ID = {1}/>
        <Footer/> 
    </div>

  );
} 

export default MainPage;

