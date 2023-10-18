import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Footer from './components/Footer'; 
import ButtonGrid from './components/ButtonGrid';
import reportWebVitals from './reportWebVitals';
import TestButton from './components/TestButton';
import BaseCard from './components/BaseCard';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
     {/* <TestButton title = {"Cool Button"} statingValue= {5}/>remove this and import when you are done using it*/ }
     {/* <TestButton title = {"Bad Button"} statingValue= {25}/>remove this and import when you are done using it*/ }
    {/* <ButtonGrid id={1}/>
    <ButtonGrid id={2}/>
    <ButtonGrid id={3}/> */}
    <BaseCard Name = {"Light1"} Text = {"Light1"} ID = {1}/>
    <Footer/> 
    
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
