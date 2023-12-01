import React, { useEffect } from "react";
import { useState } from "react";
import ButtonGrid from "./ButtonGrid";

interface Props {
  Name: string;
  Text: string;
  ID: number;
  state: boolean;
}

function BaseCard({ Name, Text, ID, state }: Props) {
  return (
    <div className="">
      <h1 className="text-xl text-blue-600 bg-red-900 border-2 border-red-900 rounded-t">
        {Name}
      </h1>
      <p className="pt-8 pb-8 text-lg text-violet-600 bg-red-900 border-2 border-red-900">
        {Text}
      </p>
      <div className="text-base text-black-600 bg-red-900 border-2 border-red-900 rounded-b">
        <ButtonGrid id={ID} state={state} />
      </div>
    </div>
  );
}

export default BaseCard;
