import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Footer from './components/Footer'; 
import ButtonGrid from './components/ButtonGrid';
import reportWebVitals from './reportWebVitals';
import TestButton from './components/TestButton';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
    <TestButton/> {/*remove this and import when you are done using it*/ }
    <ButtonGrid id={1}/>
    <ButtonGrid id={2}/>
    <ButtonGrid id={3}/>
    <Footer/> 
    
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
