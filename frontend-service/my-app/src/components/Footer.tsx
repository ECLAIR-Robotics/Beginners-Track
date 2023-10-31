// import React from 'react';
// import './Footer.css';
// // <!-- we need links to eclair, github, and logo -->
// // to make a comment int the div, use {} like this {/* this is a comment */}
//  //<img src="" alt="png image of the eclair number"></img>
// function Footer() {

  
//     const thing1 = "html";

//     function stuff() {
//       console.log("stuff")
//     }



//   return(

//   <div className="Footer">
//         <footer>
//             <p>
//             <a href="https://eclairrobotics.web.app/">Link to Eclair website</a>
//             </p>
            
//             <a href="https://github.com/ECLAIR-Robotics">Link to GitHub</a>
           
//             <p>{thing1}</p>
//             <p>Made by Eclair</p>
//             <p>Contact info for Eclair:</p>
//         </footer>
//     </div>
    
//   )


// }


// export default Footer;
// flex items-center

import React from 'react';
import './Footer.css';
import logo from './logo.png';


function Footer() {  
  return (
      <footer className="bg-slate-900 text-white fixed p-4 bottom-0 left-0 w-full">
      <div className=" flex items-center">
        <div className="basis-1/2">
          <a href="https://eclairrobotics.web.app/" className="hover:scale-125">
            <img src={logo} alt="ECLAIR" className="h-10 w-auto hover:scale-150"/>
          </a>
        </div>
        <div className="basis-1/2">
        <a href="https://github.com/ECLAIR-Robotics">View ECLAIR's GitHub</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;