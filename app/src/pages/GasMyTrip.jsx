import React, { Component } from "react";
import Navbar from "../components/Navbar";
import IconLabelTabs from "../components/InputTab";
import Footer from "../components/Footer";

class GasMyTrip extends Component {
  state = {};
  render() {
    var divStyle = {
      paddingTop: "115px"
    };
    return (
      <div>
        <Navbar />
        <div style={divStyle}>
          <IconLabelTabs />
        </div>

        <Footer />
      </div>
    );
  }
}

export default GasMyTrip;
