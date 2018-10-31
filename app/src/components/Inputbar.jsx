import React, { Component } from 'react';
import { DropdownButton, MenuItem, ButtonToolbar } from 'react-bootstrap';
import carInfo from '../components/carInfo';
import ReactDOM from 'react-dom';
import './Inputbar.css';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

class Inputbar extends React.Component {
	constructor(props) {
		super(props);
		this.showTripPlan = this.tripPlanClick.bind(this);
		this.showCarInfo = this.carInfoClick.bind(this);
		this.showPath = this.pathTogoClick.bind(this);
		this.state = {
			whichTab: 2,
			selectedOption: ''
		};
	}

	carInfoClick() {
		this.setState({ whichTab: 0 });
	}

	tripPlanClick() {
		this.setState({ whichTab: 1 });
	}

	pathTogoClick() {
		this.setState({ whichTab: 2 });
	}

	render() {
		const selectTab = this.state.whichTab;
		let button;
		console.log(selectTab);
		if (selectTab === 2) {
			button = <CarInfo onClick={this.showCarInfo} />;
		} else if (selectTab === 0) {
			button = <TripPlan onClick={this.showTripPlan} />;
		} else {
			button = <PathToGo onClick={this.showPath} />;
		}

		return (
			<div>
				{button}
				<div>
					<TabNav selectTab={selectTab} />
				</div>
			</div>
		);
	}
}

function handleChange(selectedOption) {
	//this.setState({ selectedOption });
	console.log(`Selected: ${selectedOption.label}`);
	return selectedOption;
}

function getDropListYear() {
	const year = new Date().getFullYear() + 1;
	return Array.from(new Array(50), (v, i) => (
		<option key={i} value={year - i}>
			{year - i}
		</option>
	));
}

function getDropListGas() {
	const base = 15;
	return Array.from(new Array(20), (v, i) => (
		<option key={i} value={base + i}>
			{base + i}
		</option>
	));
}

function bindCarMade(prop){
	const Toyota = [{ value: 'Camry', label: 'Camry' },{ value: 'Crown', label: 'Crown' }]
	const Honda = [{ value: 'Civic Tourer', label: 'Civic Tourer' },{ value: 'FR-V', label: 'FR-V' }]
	if(prop==='Toyota'){
		return Toyota;
	}else{
		return Honda;
	}
}

function CarInfoInput(props) {
	const cars = [ { value: 'Toyota', label: 'Toyota' }, { value: 'Honda', label: 'Honda' } ];
	const gas = [ { value: 'Shell', label: 'shell' }, { value: '76', label: '76' } ];
	

	var selectedOption = '';
	return (
		<div style={{ display: 'inline-block' }}>
			<div>Car</div>
			<Select name="cars" value={selectedOption} onChange={handleChange} options={cars} placeholder="brand" />
			{}
			<Select name="made" value={selectedOption} onChange={handleChange} options={cars} placeholder="made" />
			<select onChange={handleChange}>{getDropListYear()}</select>
			<div>gas consumption</div>
			<label>local</label>
			<select onChange={handleChange}>{getDropListGas()}</select>mile/gal
			<br />
			<label>high way</label>
			<select onChange={handleChange}>{getDropListGas()}</select>mile/gal
			<div>gas brand</div>
			<Select name="cars" value={selectedOption} onChange={handleChange} options={gas} placeholder="brand" />
		</div>
	);
}

function PlanMyTrip(props) {
	return <h1>plan my trip</h1>;
}

function ShowPathToGo(props) {
	return <h1>show my path</h1>;
}

function TabNav(props) {
	const selectTab = props.selectTab;
	if (selectTab === 2) {
		return <CarInfoInput />;
	} else if (selectTab === 0) {
		return <PlanMyTrip />;
	} else {
		return <ShowPathToGo />;
	}
}

function TripPlan(props) {
	return <button onClick={props.onClick}>Trip Plan</button>;
}

function CarInfo(props) {
	return <button onClick={props.onClick}>Car Info</button>;
}

function PathToGo(props) {
	return <button onClick={props.onClick}>Path To Go</button>;
}

ReactDOM.render(<Inputbar />, document.getElementById('root'));

// constructor(props, context) {
// 	super(props, context);

// 	this.handleSelect = this.handleSelect.bind(this);

// 	this.state = {
// 		key: 1
// 	};
// }

// handleSelect(key) {
// 	console.log(`selected ${key}`);
// 	this.setState({ key });
// 	if (this.state.key === 1) {
// 		console.log('car info');
// 		return <carInfo/>;
// 	} else if (this.state.key === 2) {
// 		console.log('Trip plan');
// 	} else {
// 		console.log('path to go');
// 	}
// }

// render() {
// 	return (
// 		<div>
// 			<Tabs activeKey={this.state.key} onSelect={this.handleSelect} id="controlled-tab-example">
// 				<Tab eventKey={1} title="Car Info" />
// 				<Tab eventKey={2} title="Trip Plan" />
// 				<Tab eventKey={3} title="Path to go" />
// 				<this.handleSelect />
// 			</Tabs>

// 		</div>
// 	);
// }
// }

export default Inputbar;
