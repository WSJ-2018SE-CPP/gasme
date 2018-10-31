import React, { Component } from 'react';
import Navbar from '../components/Navbar';
import Inputbar from '../components/Inputbar';
import Footer from '../components/Footer';
class test extends Component {
	state = {};
	render() {
		var divStyle = {
			paddingTop: '165px'
		};
		return (
			<div>
				<Navbar />
				<div style={divStyle}>
					<Inputbar />
				</div>
				<Footer />
			</div>
		);
	}
}

export default test;
