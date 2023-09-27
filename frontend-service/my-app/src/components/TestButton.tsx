import React, { useState } from 'react';
import logo from '.logo.svg';
import '../App.css';
import '../styles/testbutton.css'

interface TestButtonProps {
    text?: String;
}


function TestButton(props : TestButtonProps) {
    let [buttonStatus, setButtonStatus] = useState(false);

    console.log(buttonStatus);

    if (buttonStatus) {
        return (
            <div className="innerContainer">
                <h4>{props.text}</h4>
                <div className='testbutton-enabled' onClick={(event) => {
                    setButtonStatus(false);
                }} >
                    On
                </div>
            </div>
        )
    } else {
        return (
            <div className="innerContainer">
                <h4>{props.text}</h4>
                <div className='testbutton-disabled' onClick={(event) => {
                    console.log("clicked");
                    setButtonStatus(true);
                }}>
                    Off
                </div>
            </div>
        )
    }
}

export default TestButton;
