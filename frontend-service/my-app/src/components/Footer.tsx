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

import React from 'react';
import './Footer.css';
import logo from './logo.png';


function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-logo">
          <a href="https://www.example.com" className="button-link">
          <img src={logo} alt="ECLAIR" />
          </a>
        </div>
        <div className="footer-info">
        <a href="https://github.com/ECLAIR-Robotics">View ECLAIR's GitHub</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;