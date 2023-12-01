import React from "react";
import ReactDOM from "react-dom/client";
import Footer from "./Footer";
import ButtonGrid from "./ButtonGrid";
import TestButton from "./TestButton";
import BaseCard from "./BaseCard";
import BaseCardContainer from "./BaseCardContainer";
import { Routes, Route } from "react-router-dom";
import ANA from "./AddNewAppliances";
import { Link, useNavigate } from "react-router-dom";

function MainPage() {
  const nav = useNavigate();
  const changePage = () => {
    nav("/ANA");
  };
  return (
    <div>
      <h1 className="text-7xl md:text-3x1 font-bold text-[#81B29A]">
        Remote Electrical Controller{" "}
      </h1>
      <BaseCardContainer />
      {/* <Link to="/ANA" onClick={changePage}>
          Click to view the ANA page
        </Link> */}
      <button
        onClick={changePage}
        className="mt-4 px-6 bg-[#E07A5F] text-[#F4F1DE] text-2x1 hover:text-green-900 transition-all"
      >
        Go to ANA
      </button>
      <button className="py-4 px-8 bg-black">e</button>
      <Footer />
    </div>
  );
}

export default MainPage;
