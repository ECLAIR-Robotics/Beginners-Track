import React from "react";
import logo from "./logo.svg";
import "./ButtonGrid.css";
import { useState } from "react";

interface Props {
  id: number;
}

function ButtonGrid(props: Props) {
  const [state, toggle] = useState("OFF");

  const toggleOn = () => {
    toggle("ON");
    console.log("TURNING ON");
  };

  const toggleOff = () => {
    toggle("OFF");
    console.log("TURNING OFF");
  };

  return (
    <div className="Grid-Container flex">
      <div className={`row `}>
        <h2
          id="b1"
          className={`font-bold ${
            state === "OFF" ? "text-black" : "text-white"
          }`}
        >
          {state}
        </h2>
      </div>

      <div className="grid grid-cols-2 gap-0">
        <div className="flex flex-wrap shrink justify-evenly gap-y-0">
          <button
            onClick={toggleOn}
            className="bg-red-500 hover:bg-red-700 transition-all"
          >
            On
          </button>
        </div>
        <div className="flex flex-wrap shrink justify-evenly gap-y-0">
          <button
            onClick={toggleOff}
            className="bg-green-500 hover:bg-green-700 transition-all"
          >
            Off
          </button>
        </div>
      </div>
    </div>
  );
}

export default ButtonGrid;
