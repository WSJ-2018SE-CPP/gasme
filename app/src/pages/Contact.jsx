import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";
import './Contact.css';
import img from "../img/gasMe.png";

class Contact extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <Jumtotron title="Contact" subtitle="our contact" />
          <h2>Contact Us</h2>
          <div className="row">
          <div className="col-md-7 column">
            Google Map Pic Here
          </div>
          <div className="col-md-5 column">
            <img src={img} className="icon" alt="logo" />
            <div className="text">
              <div>
                Phone: (xxx) xxx - xxxx
                </div>
              <div>
                Fax: (xxx) xxx - xxxx
                </div>
              <div>
                Email: xxxxxxxxxx@xxxxxx.xxx
                </div>
              <div>
                Address: xxxxxxxxxxxxxxxx xxxxxxx xxxx, xxx
                </div>
            </div>
          </div>
          </div>
          
        </div>
        <Footer />
      </div>
    );
  }
}

export default Contact;
