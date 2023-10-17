// This button is for learning purposes only and will not be on the final website: Go to App.tsx and uncomment the button to see and play with it
import './ButtonGrid.css'; 
import { useState } from 'react'; // useState is a React hook (just think of it as a function that returns an array with 2 elements)

interface Props{
  title: String,
  statingValue: number
}
function TestButton({title, statingValue}: Props) {
    const [changingNumberVar, changeNumFunction] = useState(0); // changingNumberVar is the variable that will change when clicking the button (set to 0)
                                                                // changeNumFunction is the function that will be called to change changingNumberVar

    const someFunction = () => {
        console.log('OMG they clicked the button'); // Call whatever you want, but the next line actually changes the var
        changeNumFunction(changingNumberVar + 1); // Updates the state 
    };
    
  return (
    <div>
      <button onClick={someFunction}> {title}: {changingNumberVar + statingValue} </button> {/*This creates the button and sets it with an EVENT called onClick*/}
      {/*Events in react are usually ways the user interacts with a website. Link of common events will be posted when I find one*/}
    </div>

  );
} 

export default TestButton;