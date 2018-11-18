import React, { Component } from "react";
import Navbar from "../components/Navbar";
import IconLabelTabs from "../components/InputTab";
import Footer from "../components/Footer";
import GoogleMapDirection from "../components/GoogleMapDirection";
import TestFloat from "../components/TestFloat";

class test extends Component {
  state = {};
  render() {
    var divStyle = {
      paddingTop: "115px"
    };
    return (
      <div>
        <Navbar />
        <Footer />
        {/* <div style={divStyle}> */}
        <IconLabelTabs />
        {/* </div> */}
        <GoogleMapDirection />
      </div>
    );
  }
}

export default test;
