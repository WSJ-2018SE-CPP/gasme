import React, { Component } from "react";
import TimeIcon from "@material-ui/icons/AccessTime";
import GasCostIcon from "@material-ui/icons/LocalGasStation";
import PlaceIcon from "@material-ui/icons/Place";
import ArrowDropDownIcon from "@material-ui/icons/ArrowDropDown";
import ArrowRightIcon from "@material-ui/icons/ArrowRight";
// import * as data from "./backUps/data.json";
import * as data from "./backUps/la_lv.json";

var bgColors = {
  Default: "#81b71a",
  Blue: "#D6EAF8",
  Cyan: "#37BC9B",
  Green: "#8CC152",
  Red: "#F9EBEA",
  Yellow: "#F9E79F",
  Gray: "#EAEDED"
};

class PathToGo extends Component {
  state = {
    status: data.status,
    gas_price: data.gas_price,
    mileage_in_word: data.mileage,
    mileage_in_digits: [],
    time_in_word: data.time,
    time_in_digits: [],
    trip1: data.trip1,
    openTrip1: 0,
    openTrip2: 0
  };

  componentDidMount() {
    this.convertTimes();
    this.convertMileages();
  }

  convertTimes(hr_token = "hour", min_token = "min") {
    var times = [];
    for (var i = 0; i < this.state.time_in_word.length; i++) {
      times.push(converTime(this.state.time_in_word[i], hr_token, min_token));
    }
    this.setState({ time_in_digits: times });
  }

  convertMileages(mi_token = "mi") {
    var miles = [];
    for (var i = 0; i < this.state.mileage_in_word.length; i++) {
      miles.push(converMileage(this.state.mileage_in_word[i], mi_token));
    }
    this.setState({ mileage_in_digits: miles });
  }

  test() {
    console.log("in testing converMile->" + converMileage("7 mi") + "<-");
    console.log(
      "in testing convertTime ->" + converTime("1 min", "hour", "min") + "<-"
    );
  }

  //   handleIconFlip(props) {
  //     if (props.openTrip) {
  //       return <ArrowDropDownIcon />;
  //     } else {
  //       return <ArrowRightIcon />;
  //     }
  //   }

  handleIconFlip() {
    if (this.state.openTrip1 === 1) {
        this.setState({openTrip1 : 0});
      return <ArrowDropDownIcon />;
    } else {
        this.setState({openTrip1 : 1});
      return <ArrowRightIcon />;
    }
  }

  render() {
    var total_gas_price = getTotal(this.state.gas_price);
    // this.convertTimes();
    var total_time = getTotal(this.state.time_in_digits);
    var total_mileage = getTotal(this.state.mileage_in_digits).toLocaleString();
    var total_stop = 0;
    this.test();
    return (
      <div>
        <div style={{ backgroundColor: bgColors.Blue }}>
          {/* <this.handleIconFlip openTrip = {false}/> */}
          <ArrowRightIcon/>
          <label style={{ fontSize: "16px" }}>Trip</label> <TimeIcon />
          {Math.floor(total_time / 60)}:{total_time % 60}
          <PlaceIcon />
          {total_mileage}
          {" mi "}
          <GasCostIcon />${total_gas_price.toFixed(2).toLocaleString()}
        </div>
      </div>
    );
  }
}

function getTotal(ones) {
  var total = 0;
  for (var i = 0; i < ones.length; i++) {
    total += ones[i];
  }
  return total;
}

function converTime(time, hr_token = "hour", min_token = "min") {
  //example: 7 hours 36 mins
  //use the space index to get the digits
  var index = 0,
    spaces = [];
  while ((index = time.indexOf(" ", index + 1)) > 0) {
    spaces.push(index);
  }
  var hr_digit = 0,
    min_digit = 0;
  if (time.search(hr_token) > -1) {
    hr_digit = time.substring(0, spaces[0]);
  }
  if (time.search(min_token) > -1) {
    min_digit = time.substring(spaces[1] + 1, spaces[2]);
  }
  //   console.log("int converTime: " + (parseInt(hr_digit) * 60 + parseInt(min_digit)));
  return parseInt(hr_digit) * 60 + parseInt(min_digit);
}

function converMileage(mileage, mi_token = "mi") {
  //example: 399 mi
  var mi_index = mileage.search(mi_token);
  const mi_digit = mileage.substring(0, mi_index - 1);
  return parseInt(mi_digit);
}

export default PathToGo;
