import React from "react";
import gasBrandIcon from "../img/gas_station_building.jpg";
import homeImg from "../img/home_real.jpg";
import parkImg from "../img/park.jpg";
import "./OneTrip.css";

class OneTrip extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      props: props, //doesn't work
      res_status: this.props.data.res_status,
      res_gas_price: this.props.data.res_gas_price,
      res_mileage: this.props.data.res_mileage,
      res_time: this.props.data.res_time,
      res_trip1: this.props.data.res_trip1,
      res_cost: this.props.data.res_cost,
      res_gallons_to_fuel: this.props.data.res_gallons_to_fuel,
      res_station_brand: this.props.data.res_station_brand
    };
  }

  construct_oneTrip(
    status,
    gas_price,
    mileage,
    time,
    trip,
    cost,
    gallon,
    brand
  ) {
    var indents = [];
    var cur_stop = 65;
    //changed to fix gas stop numbers
    var number_of_stops = 0;
    for (var i = 0; i < gas_price.length; i++) {
      var index = i;
      var thumbnail = gasBrandIcon;
      var ingoing_line = <div className="incoming-route-line" />;
      var outgoing_line = <div className="outgoing-route-line" />;
      if (parseInt(gas_price[i]) === 0) {
        //user input stop = A, B, C, ...
        //gas station = 1, 2, 3, ...
        index = String.fromCharCode(cur_stop);
        cur_stop += 1;
        if (i === 0) {
          thumbnail = homeImg;
          ingoing_line = null;
        } else if (i === gas_price.length - 1) {
          thumbnail = parkImg;
          outgoing_line = null;
        }
        // changed to fix image on stoppoints (NON-gas station)
        else if (!trip[i].is_gas_station) {
          thumbnail = homeImg;
        }
        number_of_stops += 1;
      } else {
        //This one if you want the format to be A,2,3,4,5,B,7,8,9,C
        //index = i + 1;
        //This one if you want the format to be A,1,2,3,4,B,5,6,7,C
        index = i + 1 - number_of_stops;
      }
      indents.push(
        <div className="waypoint-view" key={i}>
          <div className="waypoint poi">
            <div className="waypoint-card">
              <div className="waypoint-info">
                <div className="waypoint-image">
                  <img className="waypoint-icon" src={thumbnail} alt="location img"/>
                </div>
                {/* Added name and address */}
                <div className="waypoint-details">
                  <div className="details">
                    <div className="address">{trip[i].name}</div>
                  </div>
                  <p className="photo-name">{trip[i].address}</p>
                </div>
                <div className="waypoint-index locked">
                  <div className="index" role="button">
                    <div className="unrouted-icon">
                      <i className="icon-cat-nature" />
                    </div>
                    <span className="index-dig">{index}</span>
                  </div>
                </div>
              </div>
            </div>
            {ingoing_line}
            {outgoing_line}
            <div className="waypoint-leg">
              <div className="waypoint-break" />
              <div className="leg-stats">
                <span className="leg-trip-stat">{mileage[i]}</span>
                <span className="bullet">•</span>
                <span className="leg-trip-stat">
                  {Math.floor(time[i] / 60)}:{time[i] % 60}
                </span>
                <span className="bullet">•</span>
                <span className="leg-trip-stat">${gas_price[i]}</span>
                <span className="bullet">•</span>
                <span className="leg-trip-stat">
                  {parseFloat(gallon[i])
                    .toFixed(2)
                    .toLocaleString()}{" "}
                  gls
                </span>
                <span className="bullet">•</span>
                <span className="leg-trip-stat">
                  total: $
                  {parseFloat(cost[i])
                    .toFixed(2)
                    .toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        </div>
      );
    }
    return indents;
  }

  handleScrollToElement = e => {
    const elementTop = this.gate.offsetTop;
    window.scrollTo(0, elementTop);
  };

  render() {
    var res_status = this.props.data.res_status;
    var res_gas_price = this.props.data.res_gas_price;
    var res_mileage = this.props.data.res_mileage;
    var time_in_digits = this.props.data.time_in_digits;
    var res_trip1 = this.props.data.res_trip1;
    var res_cost = this.props.data.res_cost;
    var res_gallons_to_fuel = this.props.data.res_gallons_to_fuel;
    var res_station_brand = this.props.data.res_station_brand;
    var trips = this.construct_oneTrip(
      res_status,
      res_gas_price,
      res_mileage,
      time_in_digits,
      res_trip1,
      res_cost,
      res_gallons_to_fuel,
      res_station_brand
    );
    return <div className="scroll-view">{trips}</div>;
  }
}

export default OneTrip;
