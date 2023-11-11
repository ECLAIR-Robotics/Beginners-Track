import React, { useState } from 'react';
import logo from '.logo.svg';
import '../App.css';
import '../styles/button.css'

interface ButtonProps {
    text?: String;
}


function Button(props: ButtonProps) {
    let [buttonStatus, setButtonStatus] = useState(false);

    console.log(buttonStatus);

    if (buttonStatus) {
        return (
            <div className="innerContainer">
                <h4>{props.text}</h4>
                <div className='button-enabled button' onClick={(event) => {
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
                <div className='button-disabled button' onClick={(event) => {
                    console.log("clicked");
                    setButtonStatus(true);
                }}>
                    Off
                </div>
            </div>
        )
    }
}

export default Button;
