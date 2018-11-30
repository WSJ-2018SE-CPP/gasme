import React, { Component } from "react";
import "./GoogleMapDirection.css";
import PopOver from "../components/PopOver";

class GoogleMapDirection extends Component {
  state = {
    count: 0,//flag for render
    res_status: [],
    res_gas_price: this.props.listFromParent.gas_price,
    res_mileage: [],
    res_time: [],
    res_trip1: this.props.listFromParent.trip1,
    res_cost: [],
    res_gallons_to_fuel: [],
    res_station_brand: [],
    isLoaded: false,
    center: { lat: 34.052235, lng: -118.243683 } //LA
  };

  // check when to render
  shouldComponentUpdate(nextProps, nextState){
    //render for the first time we click path to go
    if(this.state.count == 0){
      this.renderMap()
      this.setState({ count: 1});
    }
    //otherwise, check if current state is the same as the next one
    if(this.state.res_trip1 === nextProps.listFromParent.trip1) {
      return false;
    }
    else {
      this.renderMap()
      return true;
    }
  }

  componentWillReceiveProps(nextProps) {
    this.setState({ res_trip1: nextProps.listFromParent.trip1 });
    this.setState({ res_gas_price: nextProps.listFromParent.gas_price });
  }

  renderMap = () => {
    var API_key = "AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY";
    loadScript(
      "https://maps.googleapis.com/maps/api/js?key=" +
        API_key +
        "&callback=initMap"
    );
    window.initMap = this.initMap;
  };

  initMap = () => {
    // Create A Map
    var map = new window.google.maps.Map(document.getElementById("map"), {
      center: this.state.center,
      zoom: 14
    });

    var directionsService = new window.google.maps.DirectionsService();
    var directionsDisplay = new window.google.maps.DirectionsRenderer({
      suppressMarkers: true
    });
    directionsDisplay.setMap(map);

    this.calculateAndDisplayRouteWayPoints(
      map,
      directionsService,
      directionsDisplay
    );

    this.setMarkers(map);
  };

  calculateAndDisplayRouteWayPoints(map, directionsService, directionsDisplay) {
    var waypts = [];
    var origin;
    var destination;
    for (var i = 0; i < this.state.res_trip1.length; i++) {
      var item = this.state.res_trip1[i];
      var location = new window.google.maps.LatLng(item.lat, item.long);
      if (i !== 0 && i !== this.state.res_trip1.length - 1) {
        waypts.push({
          location: location,
          stopover: true
        });
      } else if (i === 0) {
        origin = location;
      } else {
        destination = location;
      }
    }

    directionsService.route(
      {
        origin: origin,
        destination: destination,
        waypoints: waypts,
        optimizeWaypoints: false,
        travelMode: "DRIVING"
      },
      function(response, status) {
        if (status === "OK") {
          directionsDisplay.setDirections(response);
          var leg = response.routes[0].legs[0];
          //setMarker(map, leg.start_location, 'title', '0');
          //setMarker(map, leg.end_location, 'title', '0');
        } else {
          window.alert("Directions request failed due to " + status);
        }
      }
    );
  }

  setMarkers = map => {
    // Adds markers to the map.

    // Marker sizes are expressed as a Size of X,Y where the origin of the image
    // (0,0) is located in the top left of the image.

    // Origins, anchor positions and coordinates of the marker increase in the X
    // direction to the right and in the Y direction down.
    var icon = {
      url:
        "http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png",
      //url: "gasStop.png",
      size: new window.google.maps.Size(20, 32),
      origin: new window.google.maps.Point(0, 0),
      anchor: new window.google.maps.Point(0, 32),
      labelOrigin: new window.google.maps.Point(9, -10)
    };
    // Shapes define the clickable region of the icon. The type defines an HTML
    // <area> element 'poly' which traces out a polygon as a series of X,Y points.
    // The final coordinate closes the poly by connecting to the first coordinate.
    var shape = {
      coords: [1, 1, 1, 20, 18, 20, 18, 1],
      type: "poly"
    };

    for (var i = 0; i < this.state.res_trip1.length; i++) {
      var place = this.state.res_trip1[i];
      var gasPrice = this.state.res_gas_price[i];
      const lat = this.state.res_trip1[i].lat;
      const long = this.state.res_trip1[i].long;
      if (this.state.res_trip1[i].is_gas_station === 0) {
        var marker = new window.google.maps.Marker({
          position: { lat: lat, lng: long },
          map: map,
          label: {
            text: (i + 1).toString(),
            color: "white",
            fontWeight: "bold",
            fontSize: "16px"
          }
          //title: beach[0]
        });
      } else {
        var marker = new window.google.maps.Marker({
          position: { lat: lat, lng: long },
          map: map,
          icon: icon,
          label: {
            text: gasPrice.toString(),
            color: "red",
            fontWeight: "bold",
            fontSize: "16px"
          }
        });
      }
    }
  };

  render() {
    return (
      <div>
        <div id="map">{this.renderMap()}</div>
      </div>
    );
  }
}

export default GoogleMapDirection;

function loadScript(url) {
  var index = window.document.getElementsByTagName("script")[0];
  var script = window.document.createElement("script");
  script.src = url;
  script.async = true;
  script.defer = true;
  index.parentNode.insertBefore(script, index);
}
