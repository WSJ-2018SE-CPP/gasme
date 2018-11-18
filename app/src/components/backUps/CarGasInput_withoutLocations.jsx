import React, { Component } from 'react';
// import { DropdownButton, MenuItem, ButtonToolbar } from 'react-bootstrap';
import ReactDOM from 'react-dom';
import './CarGasInput.css';
import Select from 'react-select';
// import Select from '@material-ui/core/Select';
import 'react-select/dist/react-select.css';
import { Button } from 'react-bootstrap';

class Inputbar extends React.Component {
	state = {
		selectedCarBrand: '',
		selectedMake: '',
		selectedGas: '',
		selectedYear: '',
		selectedLocal: '',
		selectedHwy: '',
		selectedGas: '',
		which_make: [],
		cars: [ { value: 'Toyota', label: 'Toyota' }, { value: 'Honda', label: 'Honda' } ],
		Toyota: [ { value: 'Camry', label: 'Camry' }, { value: 'Crown', label: 'Crown' } ],
		Honda: [ { value: 'Civic Tourer', label: 'Civic Tourer' }, { value: 'FR-V', label: 'FR-V' } ]
	};

	bindCarMade = (selectedOption, event) => {
		if(selectedOption.value === null){
			this.setState({ selectedCarBrand: "" });
		}else{
			this.setState({ selectedCarBrand: selectedOption.value });
		}
		console.log(`Selected: ${selectedOption.label}`);
		if (selectedOption.label === 'Toyota') {
			this.setState({ which_make: this.state.Toyota });
			console.log(`Yes Selected: ${'Toyota'}`);
		} else {
			this.setState({ which_make: this.state.Honda });
			console.log(`Yes Selected: ${'Honda'}`);
		}
	};

	handleChange = (event) => {
		console.log(`Selected: ${event.target.value}`);
	};

	updateMade = (selectedOption) => {
		this.setState({ selectedMake: selectedOption.value });
		console.log(`Selected: ${selectedOption.label}`);
	};

	updateGas = (selectedOption) => {
		this.setState({ selectedGas: selectedOption.value });
		console.log(`Selected: ${selectedOption.label}`);
	};

	getDropListYear = () => {
		const year = new Date().getFullYear() + 1;
		return Array.from(new Array(50), (v, i) => (
			<option key={i} value={year - i}>
				{year - i}
			</option>
		));
	};

	getDropListGas = () => {
		const base = 15;
		return Array.from(new Array(20), (v, i) => (
			<option key={i} value={base + i}>
				{base + i}
			</option>
		));
	};

	postItems = () => {
		console.log(`posting to python with ${this.state.selectedMake}`);
		fetch('http://localhost:5000', {
			method: 'post',
			//mode: 'no cors',
			headers: {
				Accept: 'application/json, text/plain, */*',
				'Content-Type': 'application/json'
			},
			// body: JSON.stringify({ a: 7, str: 'Some string: &=&' })
			body: JSON.stringify(this.state)
		})
			.then((res) => res.json())
			.then((res) => console.log(res));
	};

	render() {
		const gas = [ { value: 'Shell', label: 'shell' }, { value: '76', label: '76' } ];
		return (
			<div>
				<div>
					<span>================== CAR ==========================</span>
					<Select
						name="cars"
						value={this.state.selectedCarBrand}
						onChange={this.bindCarMade}
						options={this.state.cars}
						placeholder="brand"
					/>
					<Select
						name="made"
						value={this.state.selectedMake}
						onChange={this.updateMade}
						options={this.state.which_make}
						placeholder="made"
					/>
					<select onChange={this.handleChange} value={this.selectedYear}>
						{this.getDropListYear()}
					</select>
				</div>

				<div>
					<span>================== gas consumption ==============</span>
					<p />
					<label>local</label>
					<select onChange={this.handleChange} value={this.selectedLocal}>
						{this.getDropListGas()}
					</select>mile/gal
					<br />
					<label>high way</label>
					<select onChange={this.handleChange} value={this.selectedHwy}>
						{this.getDropListGas()}
					</select>mile/gal
				</div>

				<div>
					<span>================== gas brand ==============</span>
					<Select
						name="gas"
						value={this.state.selectedGas}
						onChange={this.updateGas}
						options={gas}
						placeholder="brand"
					/>
				</div>
				<Button bsStyle="primary" bsSize="small" onClick={() => this.postItems()}>
					SUBMIT
				</Button>
			</div>
		);
	}
}

ReactDOM.render(<Inputbar />, document.getElementById('root'));

export default Inputbar;
