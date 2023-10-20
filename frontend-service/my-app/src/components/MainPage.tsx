import React from 'react';
import ReactDOM from 'react-dom/client';
import Footer from './Footer';
import ButtonGrid from './ButtonGrid';
import TestButton from './TestButton';
import BaseCard from './BaseCard';
import { Routes, Route } from "react-router-dom"
import ANA from './AddNewAppliances'
import { Link, useNavigate } from 'react-router-dom';


function MainPage() {
    const nav = useNavigate()
    const changePage = () => {
      nav('/ANA')
    }
  return (
    <div>
      {/* <TestButton title = {"Cool Button"} statingValue= {5}/>remove this and import when you are done using it*/ }
        {/* <TestButton title = {"Bad Button"} statingValue= {25}/>remove this and import when you are done using it*/ }
        {/* <ButtonGrid id={1}/>
        <ButtonGrid id={2}/>
        <ButtonGrid id={3}/> */}
        <h1 className="text-3xl font-bold underline text-green-600 ">The thing is long </h1>
        <BaseCard Name = {"Light1"} Text = {"Light1"} ID = {1}/>
        <Footer/> 
        <div>
        <Link to="/ANA" onClick={changePage}>Click to view the ANA page</Link> 
        <button onClick={changePage} className='hover:text-green-900 transition-all'>Go to ANA</button>
        </div>
    </div>

  );
} 

export default MainPage;

