import React from "react";
import ReactDOM from "react-dom";
import "./UserInput.css";
import Select from "react-select";
import "react-select/dist/react-select.css";
import { Button } from "react-bootstrap";
import LocationSearchInput from "./LocationSearchInput";
import AddIcon from "@material-ui/icons/AddCircle";
import CancelIcon from "@material-ui/icons/Cancel";
import { ReactLoadingView } from "react-spinner-component";
import logoImg from "../img/gasMe.png";

class Inputbar extends React.Component {
  constructor(props) {
    var selectedHwy = "28";
    var selectedGas = "Top";
    var selectedGasLevel = "100";
    var selectedTankCapacity = "15";
    var locaitonsComponent = [];
    var locaitons = [];
    if (props.listFromParent) {
      selectedHwy = props.listFromParent.selectedHwy;
      selectedGas = props.listFromParent.selectedGas;
      selectedGasLevel = props.listFromParent.selectedGasLevel;
      selectedTankCapacity = props.listFromParent.selectedTankCapacity;
      locaitonsComponent = props.listFromParent.locaitonsComponent;
      locaitons = props.listFromParent.locaitons;
    }
    super(props);
    this.state = {
      // selectedLocal: "15",
      fromParent: false, //for active rerender
      isRerender: true, //to avoid rerender
      isLoading: false,
      selectedCarBrand: "",
      selectedMake: "",
      selectedYear: "2019",
      selectedLocal: "15",
      selectedHwy: selectedHwy,
      selectedGas: selectedGas,
      selectedGasLevel: selectedGasLevel,
      selectedTankCapacity: selectedTankCapacity,
      locaitonsComponent: locaitonsComponent,
      locaitons: locaitons,
      gas: [
        { value: "Top", label: "Shell, Arco, 76" },
        { value: "Shell", label: "Shell" },
        { value: "Any", label: "Any" }
      ]
    };
    this.addASearchBar = this.addASearchBar.bind(this);
    this.handleAddress = this.handleAddress.bind(this);
  }

  // componentDidMount() {
  //   if (
  //     this.props.listFromParent &&
  //     this.props.listFromParent.locaitons.length > 1
  //   ) {
  //     this.setState({ fromParent: true });
  //   }
  // }

  componentDidMount(){
    //to remove the troublesome location history from last search
    if (this.state.isRerender) {
      this.setState({ locaitons: [], locaitonsComponent: [] });
    }
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log("in shouldComponentUpdate");
    return this.state.isRerender;
  }

  //Removed to avoid "invisible input bar"
  /*
  componentDidMount() {
    var locations = this.state.locaitonsComponent.concat(LocationSearchInput);
    this.setState({ locaitonsComponent: locations });

    this.setState({ locaitons: [""] });
  }*/

  //Modified to make each input bar correspond to each location
  addASearchBar() {
    console.log("add div is clicked");
    //add a locationSearch component
    var locations = this.state.locaitonsComponent.concat(LocationSearchInput);
    this.setState({ locaitonsComponent: locations });

    //add a valid location
    const locate = this.state.locaitons;
    locate.push("");
    this.setState({ locations: locate });
  }

  //Modified to make each input bar correspond to each location
  deleteASearchBar = () => {
    console.log("delete div is clicked");
    //Modified to allow removing all input bar completely instead of leaving of at least one
    if (this.state.locaitonsComponent.length > 0) {
      //pop a locationSearch component
      var locations = this.state.locaitonsComponent;
      locations.pop();
      this.setState({ locaitonsComponent: locations });

      //pop a valid location
      const locate = this.state.locaitons;
      locate.pop();
      this.setState({ locations: locate });
    }
  };

  updateGas = selectedOption => {
    this.setState({ selectedGas: selectedOption.value });
    console.log(`Selected: ${selectedOption.label}`);
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

  getDropListGas = () => {
    const base = 24;
    return Array.from(new Array(6), (v, i) => (
      <option key={i} value={base + i * 2}>
        {base + i * 2 + " MPG"}
      </option>
    ));
  };

  getDropListTank = () => {
    const base = 100;
    return Array.from(new Array(10), (v, i) => (
      <option key={i} value={base - i * 10}>
        {base - i * 10 + " %"}
      </option>
    ));
  };

  getDropCapacity = () => {
    const base = 15;
    return Array.from(new Array(11), (v, i) => (
      <option key={i} value={base + i * 1}>
        {base + i * 1 + " Gals"}
      </option>
    ));
  };

  postItems = () => {
    console.log(`posting to python with ${this.state.selectedGasLevel}`);
    //Check number of locations on front end instead of checking response
    if (this.state.locaitons.length < 2) {
      alert("[001] Less than 2 Locations are given!");
    } else if (this.state.locaitons.includes("")) {
      alert("[003] One or more of the input bar(s) are empty.");
    } else {
      this.setState({ isLoading: true, isRerender: false });
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
        .then(res => {
          //error handling
          this.setState({ isLoading: false });
          console.log(res);
          if (res["status"] === 2) {
            alert(
              "[002] One or more of the given location(s) do NOT exist or exist outside of the USA."
            );
          } else {
            //pass the data to parent: InputTab
            this.props.callBackFromParent(res, this.state);
            console.log(res);
          }
        });
    }
  };

  //Modified to make each input bar correspond to each location
  handleAddress(key, address) {
    console.log("in handleAddress: " + address);
    const addresses = Array.from(this.state.locaitons);
    addresses[key] = address;
    //const addresses = this.state.locaitons.concat(address);
    this.setState({ locaitons: addresses });
  }

  render() {
    console.log(
      "in Userinput: location len: " +
        this.state.locaitons.length +
        "| are you proped?: " +
        this.state.fromParent
    );
    var locations = [];
    //to rerender
    // if (this.state.fromParent === true) {
    //   console.log("this.state.fromParent === true");
    //   // for(var i = 0; i < this.state.locaitons.length; i++){
    //   //   locations.push(<LocationSearchInput props={this.state.locaitons[i]}/>)
    //   // }
    //   locations = this.state.locaitonsComponent;
    //   console.log("done");
    // } else {
    locations = this.state.locaitonsComponent.map((Element, index) => {
      return (
        //Modified to make each input bar correspond to each location
        <Element
          key={index}
          index={index}
          handleAddress={this.handleAddress.bind(this, index)}
        />
      );
    });
    // }

    return (
      <div className="filter">
        <div className="input-sec">
          <h3 className="heading-first">Locations</h3>
          <div>{locations}</div>
          <div>
            <AddIcon color="primary" onClick={this.addASearchBar} />
            <CancelIcon onClick={this.deleteASearchBar} />
          </div>
        </div>

        <div className="input-sec">
          <h3 className="heading-first">Gas</h3>
          <div key="fuel eco">
            <label className="line">
              <div className="line-text">Fuel Economy</div>
              <select
                className="select"
                onChange={this.updateHwy}
                defaultValue={this.state.selectedHwy}
              >
                {this.getDropListGas() /* {getDropList(
                  24,
                  36,
                  2,
                  parseInt(this.state.selectedHwy),
                  " MPG"
                )} */}
              </select>
            </label>
          </div>
          <div key="tank">
            <label className="line">
              <div className="line-text">Tank Capacity</div>
              <select
                className="select"
                onChange={this.updateCapacity}
                defaultValue={this.state.selectedTankCapacity}
              >
                {this.getDropCapacity() /* {getDropList(
                  15,
                  25,
                  2,
                  parseInt(this.state.selectedTankCapacity),
                  " gals"
                )} */}
              </select>
            </label>
          </div>

          <div key="gas Init">
            <label className="line">
              <div className="line-text">Current Gas Level</div>
              <select
                className="select"
                onChange={this.updateGasLevel}
                defaultValue={this.state.selectedGasLevel}
              >
                {this.getDropListTank() /* {getDropList(
                  100,
                  10,
                  -10,
                  parseInt(this.state.selectedGasLevel),
                  " %"
                )} */}
              </select>
            </label>
          </div>
        </div>

        <div className="input-sec">
          <h3 className="heading-first">Gas Brand</h3>

          <Select
            name="gas"
            value={this.state.selectedGas}
            onChange={this.updateGas}
            options={this.state.gas}
            placeholder="Gas Brand"
          />
        </div>
        <div className="submit">
          <Button
            bsStyle="primary"
            bsSize="small"
            onClick={() => this.postItems()}
          >
            SUBMIT
          </Button>
        </div>
        {this.state.isLoading && (
          <ReactLoadingView
            loading={true}
            bgColor="#f1f1f1"
            spinnerColor="steelblue"
            textColor="#676767"
            textStyle="80"
            logoSrc={logoImg}
            LoaderView="ball-beat"
            customheight="100%"
            text="Calculating Route..."
            customClassAdd="class"
          />
        )}
      </div>
    );
  }
}

ReactDOM.render(<Inputbar />, document.getElementById("root"));

export default Inputbar;

function getDropList(base, max, interval, cur, unit) {
  var loop = Math.abs((max - cur) / interval);
  var intents = [];
  //add the option from the current selectedHwy
  intents.push(
    Array.from(new Array(loop + 1), (v, i) => (
      <option key={i} value={cur + i * interval}>
        {cur + i * interval + unit}
      </option>
    ))
  );

  //now add the rest
  loop = Math.abs((cur - base) / interval);
  intents.push(
    Array.from(new Array(loop), (v, i) => (
      <option key={i} value={base + i * interval}>
        {base + i * interval + unit}
      </option>
    ))
  );

  return intents;
}
