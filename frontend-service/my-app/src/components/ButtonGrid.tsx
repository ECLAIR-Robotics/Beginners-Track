import React, { useEffect } from "react";
import logo from "./logo.svg";
import "./ButtonGrid.css";
import { useState } from "react";
import backendURL from "../config";

interface Props {
  id: number;
  state: boolean;
}

function ButtonGrid(props: Props) {
  const [state, toggle] = useState("OFF");
  const [id, setId] = useState(0);

  const toggleOn = () => {
    toggle("ON");
    callBackend();
    console.log("TURNING ON");
  };

  const toggleOff = () => {
    toggle("OFF");
    callBackend();
    console.log("TURNING OFF");
  };

  const callBackend = () => {
    fetch(`${backendURL}/relay/update`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        relayNumber: id,
        relayState: state === "ON",
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data["message"]);
      });
  };

  useEffect(() => {
    setId(props.id);
    if (props.state) {
      toggleOn();
    } else {
      toggleOff();
    }
  }, []);

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
