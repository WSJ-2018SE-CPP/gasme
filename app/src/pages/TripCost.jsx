import React, { Component } from 'react';
import axios from 'axios';
import './TripCost.css';
import Footer from '../components/Footer';
import Navbar from '../components/Navbar';
// import destIcon from '../img/destS.png';
import gasIconPurple from '../img/gasPurple.png';
import gasIconGreen from '../img/gasStationGreen.png';

class googleMapDirection extends Component {
	constructor() {
		super();

		this.state = {
			pyResp: [],
			trip: [ { route: 1, cost: 345.2, dist: 300, time: 5.1 }, { route: 2, cost: 306.2, dist: 320, time: 6.2 } ],
			beaches: [
				[ 'Coogee Beach', -33.923036, 151.259052, 5, 0, 1.9 ],
				[ 'Bondi Beach', -33.890542, 151.274856, 4, 0, 0 ],
				[ 'Maroubra Beach', -33.950198, 151.259302, 1, 1, 2.9 ],
				[ 'Cronulla Beach', -34.028249, 151.157507, 3, 1, 2.5 ],
				[ 'Manly Beach', -33.80010128657071, 151.28747820854187, 2, 0, 0 ]
			],
			center: { lat: -33.9, lng: 151.2 }
			//center: { lat: 34.052235, lng: -118.243683 }, //LA
		};
	}

	componentDidMount() {
		//this.getItems();
		//this.postItems();
	}

	postItems() {
		console.log('posting to python');
		fetch('http://localhost:5000', {
			method: 'post',
			//mode: 'no cors',
			headers: {
				Accept: 'application/json, text/plain, */*',
				'Content-Type': 'application/json'
			},
			//body: JSON.stringify({ a: 7, str: 'Some string: &=&' })
			body: JSON.stringify(this.state.trip)
		})
			.then((res) => res.json())
			.then((res) => console.log(res));
	}

	//in testing with flask, not working
	postItems_notworking() {
		console.log('posting to python');
		axios({
			method: 'post',
			url: 'http://localhost:5000',
			data: this.state.trip,

			// {
			// title: 'Fred',
			// 'lastName': 'Flintstone'
			// },
			headers: {
				'Content-Type': 'text/plain;charset=utf-8'
			}
		})
			.then(function(response) {
				console.log(response);
			})
			.catch(function(error) {
				console.log(error);
				console.log(error.response.data);
			});
	}

	getItems() {
		console.log('fetching python localhost');
		fetch('http://localhost:5000', {
			method: 'GET',
			//mode: 'no-cors',//matters
			dataType: 'json',
			async: true //doesn't matter
		})
			.then((results) => results.json())
			.then((results) => {
				this.setState({
					pyResp: results
				});
			})
			.catch((err) => console.log(err));
	}

	renderMap = () => {
		var API_key = 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY';
		loadScript('https://maps.googleapis.com/maps/api/js?key=' + API_key + '&callback=initMap');
		window.initMap = this.initMap;
	};

	initMap = () => {
		// Create A Map
		var map = new window.google.maps.Map(document.getElementById('map'), {
			center: this.state.center,
			zoom: 14
		});

		// Create An InfoWindow
		var infowindow = new window.google.maps.InfoWindow();

		var directionsService = new window.google.maps.DirectionsService();
		var directionsDisplay = new window.google.maps.DirectionsRenderer({ suppressMarkers: true });
		directionsDisplay.setMap(map);

		var origin = '1419 Westwood Blvd, Los Angeles, CA 90024-4911'; //'{{origin.address}}',
		var destination = '3799 S Las Vegas Blvd, Las Vegas, NV 89109';
		var start = new window.google.maps.LatLng('37.7683909618184', '-122.51089453697205');
		var end = new window.google.maps.LatLng('41.850033', '-87.6500523');
		//this.calculateAndDisplayRoute(directionsService, directionsDisplay, start, end);
		//this.calculateAndDisplayRoute(directionsService, directionsDisplay, origin, destination);
		this.calculateAndDisplayRouteWayPoints(map, directionsService, directionsDisplay);

		this.setMarkers(map);
	};
	//using waypoints: https://developers.google.com/maps/documentation/javascript/examples/directions-waypoints
	// calculateAndDisplayRoute = (directionsService, directionsDisplay, origin, destination) => {
	// 	directionsService.route(
	// 		{
	// 			origin: origin,
	// 			destination: destination,
	// 			//waypoints: waypts,
	// 			optimizeWaypoints: true,
	// 			travelMode: 'DRIVING'
	// 		},
	// 		function(response, status) {
	// 			if (status === 'OK') {
	// 				directionsDisplay.setDirections(response);
	// 			} else {
	// 				window.alert('Directions request failed due to ' + status);
	// 			}
	// 		}
	// 	);
	// };

	calculateAndDisplayRouteWayPoints(map, directionsService, directionsDisplay) {
		var waypts = [];
		var origin;
		var destination;
		for (var i = 0; i < this.state.beaches.length; i++) {
			var item = this.state.beaches[i];
			var location = new window.google.maps.LatLng(item[1], item[2]);
			if (i !== 0 && i !== this.state.beaches.length - 1) {
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

		//var origin = '1419 Westwood Blvd, Los Angeles, CA 90024-4911'; //'{{origin.address}}',
		//var destination = '3799 S Las Vegas Blvd, Las Vegas, NV 89109';
		directionsService.route(
			{
				origin: origin,
				destination: destination,
				waypoints: waypts,
				optimizeWaypoints: true,
				travelMode: 'DRIVING'
			},
			function(response, status) {
				if (status === 'OK') {
					directionsDisplay.setDirections(response);
					var leg = response.routes[0].legs[0];
					//setMarker(map, leg.start_location, 'title', '0');
					//setMarker(map, leg.end_location, 'title', '0');
				} else {
					window.alert('Directions request failed due to ' + status);
				}
			}
		);
	}

	setMarkers = (map) => {
		// Adds markers to the map.

		// Marker sizes are expressed as a Size of X,Y where the origin of the image
		// (0,0) is located in the top left of the image.

		// Origins, anchor positions and coordinates of the marker increase in the X
		// direction to the right and in the Y direction down.
		var icon = {
			url: 'http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png',
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
			coords: [ 1, 1, 1, 20, 18, 20, 18, 1 ],
			type: 'poly'
		};
		for (var i = 0; i < this.state.beaches.length; i++) {
			var beach = this.state.beaches[i];
			//var whatIcon = beach[4] === 0 ? destIcon : gasIconGreen;
			var gasPrice = beach[5];

			if (beach[4] === 0) {
				var marker = new window.google.maps.Marker({
					position: { lat: beach[1], lng: beach[2] },
					map: map,
					label: {
						text: (i + 1).toString(),
						color: 'white',
						fontWeight: 'bold',
						fontSize: '16px'
					},
					title: beach[0]
				});
			} else {
				var marker = new window.google.maps.Marker({
					position: { lat: beach[1], lng: beach[2] },
					map: map,
					icon: icon,
					label: {
						text: gasPrice.toString(),
						color: 'red',
						fontWeight: 'bold',
						fontSize: '16px'
					},
					title: beach[0]
				});
			}
		}
	};

	render() {
		var divStyle = {
			paddingTop: '265px'
		};
		return (
			<div>
				{/* <Navbar /> */}
				<button onClick={() => this.getItems()}>getFromPython</button>
				<button onClick={() => this.postItems()}>check terminal</button>
				<p>{this.state.pyResp.orig}</p>
				<p>{this.state.pyResp.dest}</p>

				<div id="map">
					{this.renderMap()}
				</div>
				<Footer />
			</div>
		);
	}
}

function directionServiceGoogleMap(directionsService, directionsDisplay) {
	var start = '37.7683909618184, -122.51089453697205';
	var end = '41.850033, -87.6500523';
	var request = {
		origin: start,
		destination: end,
		travelMode: window.google.maps.DirectionsTravelMode.DRIVING
	};
	directionsService.route(request, function(response, status) {
		if (status == window.google.maps.DirectionsStatus.OK) {
			directionsDisplay.setDirections(response);
			var myRoute = response.routes[0];
			var txtDir = '';
			for (var i = 0; i < myRoute.legs[0].steps.length; i++) {
				txtDir += myRoute.legs[0].steps[i].instructions + '<br />';
			}
			document.getElementById('directions').innerHTML = txtDir;
		}
	});
}

function loadScript(url) {
	var index = window.document.getElementsByTagName('script')[0];
	var script = window.document.createElement('script');
	script.src = url;
	script.async = true;
	script.defer = true;
	index.parentNode.insertBefore(script, index);
}

// function setMarker(map, position, title, gasprice) {
// 	var icon = {
// 		url: 'http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png',
// 		//url: "gasStop.png",
// 		// This marker is 20 pixels wide by 32 pixels high.
// 		size: new window.google.maps.Size(20, 32),
// 		// The origin for this image is (0, 0).
// 		origin: new window.google.maps.Point(0, 0),
// 		// The anchor for this image is the base of the flagpole at (0, 32).
// 		anchor: new window.google.maps.Point(0, 32),
// 		//label
// 		labelOrigin: new window.google.maps.Point(9, -10)
// 	};

// 	var marker = new window.google.maps.Marker({
// 		position: position,
// 		map: map,
// 		icon: icon,
// 		//icon:icon,
// 		label: {
// 			text: gasprice.toString(),
// 			color: 'red',
// 			fontWeight: 'bold',
// 			fontSize: '16px'
// 		},
// 		title: title
// 	});
// }

export default googleMapDirection;
