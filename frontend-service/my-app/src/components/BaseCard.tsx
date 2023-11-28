import React from "react";
import { useState } from "react";
import ButtonGrid from "./ButtonGrid";

interface Props {
  Name: string;
  Text: string;
  ID: number;
}

function BaseCard({ Name, Text, ID }: Props) {
  return (
    <div className="">
      <h1 className="text-xl text-blue-600 bg-red-900 border-2 border-red-900 rounded-t">
        {Name}
      </h1>
      <p className="pt-2 pb-8 text-lg text-violet-600 bg-red-900 border-2 border-red-900">
        {Text}
      </p>
      <div className="text-base text-black-600 bg-red-900 border-2 border-red-900 rounded-b">
        <ButtonGrid id={ID} />
      </div>
    </div>
  );
}

export default BaseCard;
