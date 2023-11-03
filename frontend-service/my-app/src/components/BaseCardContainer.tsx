import React from 'react';
import BaseCard from './BaseCard';


function BaseCardContainer() {
  return (
   <div className = "grid grid-cols-3 gap-4">
    <BaseCard Name = "Light1" Text = "Light2" ID = {3}/>
    <BaseCard Name = "Light1" Text = "Light2" ID = {3}/>
    <BaseCard Name = "Light1" Text = "Light2" ID = {3}/>
    <BaseCard Name = "Light1" Text = "Light2" ID = {3}/>
   </div>
  );
};

export default BaseCardContainer;