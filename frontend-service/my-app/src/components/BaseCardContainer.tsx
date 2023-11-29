import BaseCard from "./BaseCard";
import React, { useEffect } from "react";
import { useState } from "react";
import backendURL from "../config";

function BaseCardContainer() {
  const [inputData, setInputData] = useState([
    {
      name: "",
      description: "",
      id: -1,
      state: false,
    },
  ]);
  useEffect(() => {
    callBackend();
  }, []);
  useEffect(() => {
    console.log(inputData);
  }, [inputData]);

  const callBackend = () => {
    console.log("backend:");
    fetch(
      `${backendURL}/getAll`, //TODO: Still need to make this IP not fixed and changeable depending on location
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        setInputData(data);
      });
  };
  return (
    <div className="grid grid-cols-3 gap-4 bg-violet-300 border-8 border-violet-300">
      {inputData.map((elem, ind) => {
        return (
          <BaseCard
            key={ind}
            Name={elem["name"]}
            Text={elem["description"]}
            ID={elem["id"]}
            state={elem["state"]}
          />
        );
      })}
      {/* <div>{inputData[0]["name"]}</div> */}
    </div>
  );
}

export default BaseCardContainer;
