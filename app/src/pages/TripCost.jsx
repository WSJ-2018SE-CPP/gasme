import React, { Component } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import axios from 'axios';
//import googleMap from '../components/googleMap';
import { Map, InfoWindow, Marker, GoogleApiWrapper } from 'google-maps-react';

class TripCost extends Component {
	state = {};

	constructor() {
		super();

		this.state = {
			pyResp: [],
			trip: [ { route: 1, cost: 345.2, dist: 300, time: 5.1 }, { route: 2, cost: 306.2, dist: 320, time: 6.2 } ]
		};
	}

	componentDidMount() {
		//this.getItems();
		//this.postItems();
	}

	// postItems() {
	// 	console.log('posting to python');
	// 	fetch('http://localhost:5000', {
	// 		method: 'post',
	// 		//mode: 'no cors',
	// 		headers: {
	// 			Accept: 'application/json, text/plain, */*',
	// 			'Content-Type': 'application/json'
	// 		},
	// 		body: JSON.stringify({ a: 7, str: 'Some string: &=&' })
	// 	})
	// 		.then((res) => res.json())
	// 		.then((res) => console.log(res));
	// }

	//in testing with flask
	postItems() {
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
	//				<button onClick={() => this.postItems()}>check terminal</button>

	render() {
		return (
			<div className="container">
				{/* <h1>Blockchain Voter</h1>
				<button onClick={() => this.getItems()}>getFromPython</button>
				<button onClick={() => this.postItems()}>check terminal</button>

				<p>{this.state.pyResp.orig}</p>
				<p>{this.state.pyResp.dest}</p> */}

				{/* <form id="postData">
					<div>
						<input type="text" name="" id="tittle" />
					</div>
					<div>
						<textarea name="" id="body" cols="20" rows="5" />
					</div>
					<input type="submit" value="SEND POST" />
				</form> */}

				{/* <googleMap/> */}
				<Map google={this.props.google} zoom={14}>
					<Marker onClick={this.onMarkerClick} name={'Current location'} />

					<InfoWindow onClose={this.onInfoWindowClose}>
						<div>
							<h1>{this.state.selectedPlace.name}</h1>
						</div>
					</InfoWindow>
				</Map>
				<Footer />
			</div>
		);
	}
}

//export default TripCost;
export default GoogleApiWrapper({
	apiKey: 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
})(TripCost);
