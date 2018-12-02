import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";
import "./Home.css";
import tripImg from "../img/compass.png";
import contactImg from "../img/email.png";
import aboutImg from "../img/user.png";

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
          <div className="container-fluid">
          <div className="paragraph">
          </div>
          <div className="row">
            <div className="col-md-4 third">
              <div>
                <a href="/gasMyTrip">
                  <img src={tripImg} className="icon"/>
                  <div className="title">
                    Gas My Trip
                  </div>
                </a>
              </div>
              <div>
                Ready to plan a trip? 
                Our trip planner can help you find the cheapest route with over 150,000 gas stations location around the U.S.A.
                Plan a trip <a href="gasMyTrip"> now</a>!
              </div>
            </div>
            <div className="col-md-4 third">
              <div>
                  <a href="/about">
                    <img src={aboutImg} className="icon"/>
                    <div className="title">
                      About Us
                    </div>
                  </a>
                </div>
                <div>
                  We are a group of developer who are inspired to solve the problems many commuters face. 
                  Read more about us <a href="/about"> here... </a>
                </div>
              </div>
            <div className="col-md-4 third">
              <div>
                <a href="/contact">
                  <img src={contactImg} className="icon"/>
                  <div className="title">
                     Contact Us
                  </div>
                </a>
              </div>
              <div>
                Are you having problem with our site and needing technical support?
                Or do you have any questions regarding our project?                
                We are one <a href="/contact"> click </a> away!
              </div>
            </div>
          </div>
        </div>
          </p>
        </div>
        <Footer/>
      </div>
    );
  }
}

export default Home;
