import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";

class About extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <Jumtotron title="About" subtitle="something about"/>
          <h2>About</h2>
          <p>
            think something, write something
          </p>
        </div>
        <Footer/>
      </div>
    );
  }
}

export default About;
