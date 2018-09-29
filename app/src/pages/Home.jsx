import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";

class Home extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <Jumtotron title="Welcome" subtitle="something witty"/>
          <h2>Welcome</h2>
          <p>
            lslslsllslslslslslslsslslslsls gas gas gas money money electric
            carsssssss
          </p>
        </div>
        <Footer/>
      </div>
    );
  }
}

export default Home;
