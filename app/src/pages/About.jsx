import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import "./About.css";
class About extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <h2>About</h2>
          <p>think something, write something</p>
        </div>
        <div className="jumbo">
          <span className="jumbotron-text">
            <h2 className="title">PLAN SMART, SAVE GAS COST.</h2>
            <h5>
              Wonder all the time where and when to fuel your car during daily
              commute or long trips? Our trip planner can help you find the
              cheapest route with over 150,000 gas stations in the U.S.
            </h5>
            <h4>
              Plan your trip{" "}
              <a href="http://www.gasmeonline.com/">
                <span class="link">now</span>
              </a>
              !
            </h4>
          </span>
        </div>
        <Footer />
      </div>
    );
  }
}

export default About;
