import React, { Component } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Jumtotron from "../components/Jumbotron";
import './Contact.css';
import img from "../img/gasMe.png";

class Contact extends Component {
  state = {};
  handleSubmit() {
    alert('Sent')
  }
  render() {
    return (
      <div>
        <div className="container">
          <Navbar />
          <Jumtotron title="Contact" subtitle="our contact" />
          <h2>Contact Us</h2>
          <div className="row flex">
            <div className="col-md-1 flex">
            </div>
            <div className="col-md-3 form flex">
              <form>
                <div>
                  <div>
                    Name:
                    </div>
                  <div>
                    <input type="text" name="name" style={{ width: "300px" }} />
                  </div>
                </div>
                <div>
                  <div>
                    Email:
                    </div>
                  <div>
                    <input type="text" name="email" style={{ width: "300px" }} />
                  </div>
                </div>
                <div>
                  <div>
                    Message:
                  </div>
                  <div>
                    <textarea className="message" type="text" name="message" style={{ height: "175px", width: "300px" }} />
                  </div>
                </div>
                <button onClick={() => this.handleSubmit()}>Submit</button>
              </form>
            </div>
            <div className="col-md-3 flex">
            </div>
            <div className="col-md-5 column flex location">
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
      </div >
    );
  }
}

export default Contact;
