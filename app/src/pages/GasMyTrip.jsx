import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import IconLabelTabs from "../components/InputTab";
import GoogleMapDirection from "../components/GoogleMapDirection";

class GasMyTrip extends Component {
  state = {};
  render() {
    var divStyle = {
      paddingTop: "115px"
    };
    return (
      <div>
        <Navbar />
        <Footer />
        <GoogleMapDirection/>
        {/* <div style={divStyle}>
          <IconLabelTabs />
        </div> */}

      </div>
    );
  }
}

export default GasMyTrip;
