import React, { Component } from "react";
import "./Footer.css";
class Footer extends Component {
  state = {};
  render() {
    return (
      <footer className="footer">
        <div className="container">
          <span className="text-muted">GasMe.se18cpp; {new Date().getFullYear()}</span>
        </div>
      </footer>
    );
  }
}

export default Footer;
