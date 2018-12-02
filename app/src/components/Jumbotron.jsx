import React, { Component } from "react";
import './Jumbotron.css'

class Jumbotron extends Component {
  render() {
    return (
        <div className="jumbotron">
          <div className="container">
            <h1 className="display-5">GasMe</h1>
            <p className="lead">
              Helping You Spend Less on Gas!
            </p>
          </div>
        </div>

    );
  }
}

export default Jumbotron;
