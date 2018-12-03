import React, { Component } from "react";
import brandLogo from "../img/gasMe.png";
import "./Navbar.css";
import new_trip_btn from "../img/new_trip.png";
import { Tooltip, OverlayTrigger } from "react-bootstrap";

class Navbar extends Component {
  state = {};
  render() {
    const tooltip = (
      <Tooltip placement="left" className="in" id="tooltip-left">
        Tooltip left
      </Tooltip>
    );
    return (
      <nav className="navbar navbar-expand-md navbar-light bg-light fixed-top">
        <a className="navbar-brand" href="/">
          <img src={brandLogo} className="App-logo" alt="logo" />
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarsExampleDefault"
          aria-controls="navbarsExampleDefault"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>

        <div className="collapse navbar-collapse" id="navbarsExampleDefault">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <a className="nav-link" href="/">
                Home <span className="sr-only">(current)</span>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/GasMyTrip">
                Gas My Trip
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/About">
                About
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/Contact">
                Contact
              </a>
            </li>
            <li>
              <OverlayTrigger placement="right" overlay={tooltip}>
                <a href="/GasMyTrip" alt=" new trip">
                  <img src={new_trip_btn} style={{width:"6vh", height:"6vh"}} alt="new trip button"/>
                </a>
              </OverlayTrigger>
            </li>
          </ul>

          <form className="form-inline my-2 my-lg-0">
            <input
              className="form-control mr-sm-2"
              type="text"
              placeholder="Search"
              aria-label="Search"
            />
            <button
              className="btn btn-outline-success my-2 my-sm-0"
              type="submit"
            >
              Search
            </button>
          </form>
          <button type="button" className="btn btn-link">
            SIGN UP
          </button>
          <button type="button" className="btn btn-link">
            LOG IN
          </button>
        </div>
      </nav>
    );
  }
}

export default Navbar;
