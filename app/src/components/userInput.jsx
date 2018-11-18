import React, { Component } from "react";
import ReactDOM from "react-dom";
import "./UserInput.css";
import Select from "react-select";
import "react-select/dist/react-select.css";
import { Button } from "react-bootstrap";
import LocationSearchInput from "./LocationSearchInput";
import AddIcon from "@material-ui/icons/AddCircle";
import CancelIcon from "@material-ui/icons/Cancel";

class Inputbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedCarBrand: "",
      selectedMake: "",
      selectedGas: "",
      selectedYear: "2019",
      selectedLocal: "15",
      selectedHwy: "15",
      selectedGas: "",
      selectedGasLevel: "100",
      selectedTankCapacity: "30",
      which_make: [],
      locaitonsComponent: [],
      locaitons: [],
      cars: [
        { value: "Toyota", label: "Toyota" },
        { value: "Honda", label: "Honda" }
      ],
      Toyota: [
        { value: "Camry", label: "Camry" },
        { value: "Crown", label: "Crown" }
      ],
      Honda: [
        { value: "Civic Tourer", label: "Civic Tourer" },
        { value: "FR-V", label: "FR-V" }
      ],
      gas: [{ value: "Shell", label: "shell" }, { value: "76", label: "76" }]
    };
    this.addASearchBar = this.addASearchBar.bind(this);
    this.handleAddress = this.handleAddress.bind(this);
  }

  componentDidMount() {
    var locations = this.state.locaitonsComponent.concat(LocationSearchInput);
    this.setState({ locaitonsComponent: locations });
  }

  addASearchBar() {
    console.log("add div is clicked");
    var locations = this.state.locaitonsComponent.concat(LocationSearchInput);
    this.setState({ locaitonsComponent: locations });
    // if (this.state.locaitons.length < 4) {
    //   var locations = LocationSearchInput;
    //   this.setState({ locaitons: [...this.state.locaitons, locations] });
    //   //console.log(this.state.locaitons[0]);
    // }
  }

  deleteASearchBar = () => {
    console.log("delete div is clicked");
    //console.log("checking: " + this.state.locaitons[0].props.adress);
    // if (this.state.locaitonsComponent.length > 1) {
    //   var locations = this.state.locaitonsComponent;
    //   var lastelement = locaitonsComponent.pop();
    //   //console.log(lastelement.props);
    //   this.setState({ locaitonsComponent: locations });
    // }
  };

  bindCarMade = (selectedOption, event) => {
    this.setState({ selectedCarBrand: selectedOption.value });
    console.log(`Selected: ${selectedOption.label}`);
    if (selectedOption.label === "Toyota") {
      this.setState({ which_make: this.state.Toyota });
      console.log(`Yes Selected: ${"Toyota"}`);
    } else {
      this.setState({ which_make: this.state.Honda });
      console.log(`Yes Selected: ${"Honda"}`);
    }
  };

  handleChange = event => {
    console.log(`Selected: ${event.target.value}`);
  };

  updateMade = selectedOption => {
    this.setState({ selectedMake: selectedOption.value });
    console.log(`Selected: ${selectedOption.label}`);
  };

  updateGas = selectedOption => {
    this.setState({ selectedGas: selectedOption.value });
    console.log(`Selected: ${selectedOption.label}`);
  };

  updateYear = selectedOption => {
    this.setState({ selectedYear: selectedOption.target.value });
    console.log(`Selected: ${selectedOption.target.value}`);
  };

  updateHwy = selectedOption => {
    this.setState({ selectedHwy: selectedOption.target.value });
    console.log(`Selected: ${selectedOption.target.value}`);
  };

  updateLocal = selectedOption => {
    this.setState({ selectedLocal: selectedOption.target.value });
    console.log(`Selected: ${selectedOption.target.value}`);
  };

  updateCapacity = selectedOption => {
    this.setState({ selectedTankCapacity: selectedOption.target.value });
    console.log(`Selected: ${selectedOption.target.value}`);
  };

  updateGasLevel = selectedOption => {
    this.setState({ selectedGasLevel: selectedOption.target.value });
    console.log(`Selected: ${selectedOption.target.value}`);
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

  getDropListTank = () => {
    const base = 100;
    return Array.from(new Array(10), (v, i) => (
      <option key={i} value={base - i * 10}>
        {base - i * 10}
      </option>
    ));
  };

  getDropCapacity = () => {
    const base = 10;
    return Array.from(new Array(11), (v, i) => (
      <option key={i} value={base + i * 2}>
        {base + i * 2}
      </option>
    ));
  };

  postItems = () => {
    console.log(`posting to python with ${this.state.selectedGasLevel}`);
    fetch("http://54.183.10.84:5000/", {
      method: "post",
      //mode: 'no cors',
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(this.state)
    })
      .then(res => res.json())
      .then(res => console.log(res));
  };

  handleAddress(address) {
    console.log("in handleAddress: " + address);
    const addresses = this.state.locaitons.concat(address);
    this.setState({ locaitons: addresses });
  }

  render() {
    const locaitons = this.state.locaitonsComponent.map((Element, index) => {
      return (
        <Element key={index} index={index} handleAddress={this.handleAddress} />
      );
    });

    console.log(
      "in render: location component#" +
        this.state.locaitonsComponent.length.toString()
    );

    console.log("in render: locations#: " + this.state.locaitons.length.toString());
    console.log("in render: locations: " + this.state.locaitons);

    return (
      <div>
        <div>
          <div>Locations: {locaitons}</div>
          <div>
            <AddIcon color="primary" onClick={this.addASearchBar} />
            <CancelIcon onClick={this.deleteASearchBar} />
          </div>
        </div>
        <div>
          <span>======== Car Information ========</span>
          <Select
            name="cars"
            value={this.state.selectedCarBrand}
            onChange={this.bindCarMade}
            options={this.state.cars}
            placeholder="Car Brand"
          />
          <Select
            name="made"
            value={this.state.selectedMake}
            onChange={this.updateMade}
            options={this.state.which_make}
            placeholder="Car Made"
          />
          <select onChange={this.updateYear} value={this.selectedYear}>
            {this.getDropListYear()}
          </select>
        </div>

        <div>
          <span>======= Gas Consumption =======</span>
          <p />
          <label>Local</label>{" "}
          <select onChange={this.updateLocal} value={this.selectedLocal}>
            {this.getDropListGas()}
          </select>{" "}
          Mile(s)/Gallon
          <br />
          <label>Highway</label>{" "}
          <select onChange={this.updateHwy} value={this.selectedHwy}>
            {this.getDropListGas()}
          </select>{" "}
          Mile(s)/Gallon
          <br />
          <label>Tank Capacity</label>{" "}
          <select
            onChange={this.updateCapacity}
            value={this.selectedTankCapacity}
          >
            {this.getDropCapacity()}
          </select>{" "}
          Gallons
          <br />
          <label>Initial Gas Level </label>{" "}
          <select onChange={this.updateGasLevel} value={this.selectedGasLevel}>
            {this.getDropListTank()}
          </select>{" "}
          %
        </div>

        <div>
          <span>========= Gas Brand =========</span>
          <Select
            name="gas"
            value={this.state.selectedGas}
            onChange={this.updateGas}
            options={this.state.gas}
            placeholder="Gas Brand"
          />
        </div>
        <Button
          bsStyle="primary"
          bsSize="small"
          onClick={() => this.postItems()}
        >
          SUBMIT
        </Button>
      </div>
    );
  }
}

ReactDOM.render(<Inputbar />, document.getElementById("root"));

export default Inputbar;
