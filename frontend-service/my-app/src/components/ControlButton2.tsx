import React, { useState } from 'react';
import '../styles/button.css';

type Props = React.ButtonHTMLAttributes<HTMLButtonElement>


export const ControlButton2 = (props: Props) => {
    let [buttonStatus, setButtonStatus] = useState(false);

    console.log(buttonStatus);

    if (buttonStatus) {
        return (
            <div className="innerContainer">
                <h4>{props.value}</h4>
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
                <h4>{props.value}</h4>
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

export default ControlButton2;