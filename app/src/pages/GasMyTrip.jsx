import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import IconLabelTabs from "../components/InputTab";

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
        <IconLabelTabs />
      </div>
    );
  }
}

export default GasMyTrip;
