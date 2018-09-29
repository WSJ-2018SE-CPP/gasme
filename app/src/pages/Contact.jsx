import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";

class Contact extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <Jumtotron title="Contact" subtitle="our contact"/>
          <h2>Contact</h2>
          <p>
            name address etc
          </p>
        </div>
        <Footer/>
      </div>
    );
  }
}

export default Contact;
