import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Footer from './components/Footer';
import App from './App';
import ANA from './components/AddNewAppliances';
import ButtonGrid from './components/ButtonGrid';
import reportWebVitals from './reportWebVitals';
import TestButton from './components/TestButton'; 

import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>

  // <React.StrictMode>
  //   <ANA />
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
