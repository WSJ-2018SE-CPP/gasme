import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

class TripCost extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          
        </div>
        <Footer/>
      </div>
    );
  }
}

export default TripCost;
