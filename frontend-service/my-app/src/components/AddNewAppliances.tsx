import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./AddNewAppliances.css";
import { Link, useNavigate } from "react-router-dom";
import backendURL from "../config";

function ANA() {
  // const nameTextBox = document.createElement("input")
  // nameTextBox.type = "text"
  // nameTextBox.placeholder = "Enter new appliance"

  const [name, setName] = useState<String>("");
  const [desc, setDesc] = useState<String>("");
  const [id, setID] = useState<String>("");

  const callBackend = () => {
    console.log("backend:");
    fetch(`${backendURL}/relay/add`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        desc: desc,
        id: id,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data["message"]);
      });
  };

  // useEffect(()=>{
  //   console.log('name:', name)
  //   console.log('desc:', desc)
  //   console.log('id:', id)
  // }, [name, desc, id])

  const nav = useNavigate();
  const changePage = () => {
    nav("/");
  };
  return (
    <div className="">
      <header>
        <h1 className="text-3xl font-bold underline #0f172a">
          Add new appliances here
        </h1>
      </header>

      <div className="mx-1 bg-[#9C9DAA] rounded py-2 pb-3">
        <div className="mx-3">
          <div className=".row mt-3">
            <div className="flex">
              <div className="basis-1/4 text-left">{"Name:"}</div>
              <input
                className="name-input basis-5/6"
                onChange={(e) => setName(e.target.value)}
                type="text"
                placeholder="Enter appliance name"
              />
            </div>
          </div>

          <div className=".row mt-3">
            <div className="Appliance Description flex">
              <div className="basis-1/4 text-left">Description: </div>
              <input
                className="description-input basis-5/6"
                onChange={(e) => setDesc(e.target.value)}
                type="text"
                placeholder="Enter description"
              />
            </div>
          </div>

          <div className=".row mt-3">
            <div className="Appliance ID flex">
              <div className="basis-1/4 text-left">ID: </div>
              <input
                className="id-input basis-5/6"
                onChange={(e) => setID(e.target.value)}
                type="number"
                placeholder="Enter appliance ID"
              />
            </div>
          </div>
        </div>
      </div>

      <button className="bg-gray-500 mt-4" onClick={callBackend}>
        Submit
      </button>

      <button className="bg-rose-300" onClick={changePage}>
        Go to Main Page
      </button>
    </div>
  );
}

export default ANA;
