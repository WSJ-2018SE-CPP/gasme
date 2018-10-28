import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import TripCost from "./pages/TripCost";
import TripCost1 from "./pages/TripCost.1"

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="/Contact" component={Contact} />
          <Route path="/TripCost" component={TripCost} />
          <Route path="/TripCost1" component={TripCost1} />
        </div>
      </Router>
    );
  }
}

export default App;
