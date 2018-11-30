import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import GasMyTrip from "./pages/GasMyTrip";

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="/Contact" component={Contact} />
          <Route path="/GasMyTrip" component={GasMyTrip} />
        </div>
      </Router>
    );
  }
}

export default App;
