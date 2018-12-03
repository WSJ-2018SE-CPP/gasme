import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import IconLabelTabs from "../components/InputTab";

class GasMyTrip extends Component {
  state = {};
  render() {
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
