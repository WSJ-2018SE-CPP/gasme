import React, { Component } from "react";
import TimeIcon from "@material-ui/icons/AccessTime";
import GasCostIcon from "@material-ui/icons/LocalGasStation";
import PlaceIcon from "@material-ui/icons/Place";
import ArrowDropDownIcon from "@material-ui/icons/ArrowDropDown";
import ArrowRightIcon from "@material-ui/icons/ArrowRight";
import OneTrip from "../components/OneTrip";

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
    res_status: this.props.listFromParent.status,
    res_gas_price: this.props.listFromParent.gas_price,
    res_mileage: this.props.listFromParent.mileage,
    res_time: this.props.listFromParent.time,
    res_trip1: this.props.listFromParent.trip1.map(number => number),
    res_cost: this.props.listFromParent.cost,
    res_gallons_to_fuel: this.props.listFromParent.gallons_to_fuel,
    res_station_brand: [],

    mileage_in_digits: [],
    time_in_digits: [],

    openTrip1: 0,
    openTrip2: 0
  };

  componentWillMount() {
    this.convertMileages();
    this.convertTimes();
  }

  convertTimes(hr_token = "hour", min_token = "min") {
    console.log("in converTime");
    var times = [];
    for (var i = 0; i < this.state.res_time.length; i++) {
      times.push(converTime(this.state.res_time[i], hr_token, min_token));
    }
    this.setState({ time_in_digits: times });
  }

  convertMileages(mi_token = "mi") {
    console.log("in convertMileages");
    var miles = [];
    for (var i = 0; i < this.state.res_mileage.length; i++) {
      miles.push(converMileage(this.state.res_mileage[i], mi_token));
    }
    this.setState({ mileage_in_digits: miles });
  }

  test() {
    console.log(this.state.mileage_in_digits);
    console.log("in testing converMile->" + converMileage("7 mi") + "<-");
    console.log(
      "in testing convertTime ->" + converTime("1 min", "hour", "min") + "<-"
    );
  }

  handleIconFlip() {
    if (this.state.openTrip1 === 1) {
      this.setState({ openTrip1: 0 });
      return <ArrowDropDownIcon />;
    } else {
      this.setState({ openTrip1: 1 });
      return <ArrowRightIcon />;
    }
  }

  trip_summary(total_gas_price, total_time, total_mileage, total_stop) {
    var indents = [];
    //control to show only when there is a route, otherwise no trip summary or details
    if (this.state.res_trip1.length > 1) {
      indents.push(
        <div>
          <div style={{ backgroundColor: bgColors.Blue }}>
            <ArrowDropDownIcon />
            <label style={{ fontSize: "16px" }}>Trip</label> <TimeIcon />
            {Math.floor(total_time / 60)}:{total_time % 60}
            <PlaceIcon />
            {total_mileage}
            {" mi "}
            <GasCostIcon />${total_gas_price.toFixed(2).toLocaleString()}
          </div>
          <OneTrip data={this.state} />
        </div>
      );
    }
    return indents;
  }

  render() {
    var total_gas_price = getTotal(this.state.res_cost);
    var total_time = getTotal(this.state.time_in_digits);
    var total_mileage = getTotal(this.state.mileage_in_digits).toLocaleString();
    var total_stop = 0;
    return this.trip_summary(
      total_gas_price,
      total_time,
      total_mileage,
      total_stop
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
  //return 7*60 + 36
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
  return parseInt(hr_digit) * 60 + parseInt(min_digit);
}

function converMileage(mileage, mi_token = "mi") {
  //ex mileage: 399 mi
  //result: 399
  var mi_index = mileage.search(mi_token);
  const mi_digit = mileage.substring(0, mi_index - 1);
  return parseInt(mi_digit);
}

export default PathToGo;
