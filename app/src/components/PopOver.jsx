import React, { Component } from "react";
import gasBrandIcon from "../img/gas_station_building.jpg";
import homeImg from "../img/home_real.jpg";
import parkImg from "../img/park.jpg";

class PopOver extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const name = this.props.name;
    const address = this.props.address;
    const price = this.props.gas_price;
    const is_start = this.props.is_start;
    const is_end = this.props.is_end;
    const brand = this.props.brand;
    var thumbnail = gasBrandIcon;
    if (is_start) {
      thumbnail = homeImg;
    } else if (is_end) {
      thumbnail = parkImg;
    }
    return (
      <div class="map-popover-content">
        <div class="image">
          <img className="waypoint-icon" src={thumbnail} />
        </div>
        <div class="info">
          <div class="name">{address}</div>
          <div class="stats">
            <span class="attractions">{brand}</span>
            <span class="price-range">${price}</span>
          </div>
        </div>
      </div>
    );
  }
}

export default PopOver;
