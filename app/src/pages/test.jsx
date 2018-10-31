import React, { Component } from 'react';
import Navbar from '../components/Navbar';
import Inputbar from '../components/Inputbar';
class test extends Component {
	state = {};
	render() {
        var divStyle = {
            paddingTop: "165px"
          };
		return (
			<div>
				<Navbar />
				<div style={divStyle}>
					<Inputbar />
				</div>
			</div>
		);
	}
}

export default test;
