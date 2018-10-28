import React, { Component } from 'react';
import brandLogo from "../img/gasMe.png";
import './Navbar.css';

class Navbar extends Component {
    state = {  }
    render() { 
        return ( 
            //navbar navbar-expand-lg navbar-light bg-light
            <nav className="navbar navbar-expand-md navbar-light bg-light fixed-top">
                <a className="navbar-brand" href="/" ><img src={brandLogo} className="App-logo" alt="logo" /></a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarsExampleDefault">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <a className="nav-link" href="/">Home <span className="sr-only">(current)</span></a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/TripCost">Gas My Trip</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/About">About</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/Contact">Contact</a>
                    </li>

                    <li className="nav-item">
                        <a className="nav-link" href="/TripCost1">TEST</a>
                    </li>
                
                    </ul>
                    <form className="form-inline my-2 my-lg-0">
                    <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"/>
                    <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </nav>
         );
    }
}
 
export default Navbar;