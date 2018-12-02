import React from "react";
import PropTypes from "prop-types";
import Paper from "@material-ui/core/Paper";
import { withStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import CarIcon from "@material-ui/icons/DirectionsCar";
import Navigation from "@material-ui/icons/Navigation";
import UserInput from "../components/UserInput";
import Typography from "@material-ui/core/Typography";
import PathToGo from "../components/PathTogo";
import GoogleMapDirection from "../components/GoogleMapDirection";
import "./InputTab.css";

const styles = {
  root: {
    flexGrow: 1,
    width: 350,
    height: "81.5vh",
    backgroundColor: "#eef8fd",
    display: "block"
  },
  header: {
    backgroundColor: "White"
  }
};

function TabContainer(props) {
  return (
    <Typography component="div" style={{ padding: 1 }}>
      {props.children}
    </Typography>
  );
}

class IconLabelTabs extends React.Component {
  state = {
    value: 0,
    //rechieving response from backend

    //Changed to fix initial state for pathToGo
    response: {
      status: 0,
      gas_price: [],
      mileage: [],
      trip1: [],
      time: [],
      gallons_to_fuel: [],
      cost: []
    },
    userinput: {
      isLoading: false,
      selectedCarBrand: "",
      selectedMake: "",
      selectedGas: "",
      selectedYear: "2019",
      selectedLocal: "15",
      selectedHwy: "24",
      selectedGas: "Top",
      selectedGasLevel: "100",
      selectedTankCapacity: "15",
      locaitonsComponent: [],
      locaitons: [],
      gas: [
        { value: "Top", label: "Shell, Arco, 76" },
        { value: "Shell", label: "Shell" },
        { value: "Any", label: "Any" }
      ]
    }
  };

  //Added to automatically show map
  componentDidMount() {
    this.setState({ value: 0 });
  }

  handleChange = (event, value) => {
    this.setState({ value });
  };

  //use the data from the child
  response_to_state = (dataFromChild1, dataFromChild2) => {
    console.log(dataFromChild1);
    this.setState({ response: dataFromChild1, userinput: dataFromChild2 });
    console.log(this.state.response);
    console.log(this.state.userinput);
    //Make sure pathToGo is rerendered even when currently at pathToGo Tab
    this.setState({ value: 1 });
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;
    var response = this.state.response;
    var userinput = this.state.userinput;
    console.log("inputTab is created: hwy" + this.state.userinput.locaitons);
    return (
      <div>
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-3">
              <div className="float" styles={{ position: "absolute" }}>
                <Paper square className={classes.root}>
                  <Tabs
                    className={classes.header}
                    value={this.state.value}
                    onChange={this.handleChange}
                    fullWidth
                    indicatorColor="secondary"
                    textColor="secondary"
                  >
                    <Tab icon={<CarIcon />} label="Trip Info" />
                    <Tab icon={<Navigation />} label="Path to Go" />
                  </Tabs>

                  {value === 0 && (
                    <TabContainer>
                      <UserInput
                        key="1"
                        callBackFromParent={this.response_to_state}
                        listFromParent={userinput}
                      />
                    </TabContainer>
                  )}
                  {value === 1 && (
                    <TabContainer>
                      {<PathToGo listFromParent={response} />}
                    </TabContainer>
                  )}
                </Paper>
              </div>
            </div>
            <div className="col-md-9">
              <GoogleMapDirection listFromParent={response} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

IconLabelTabs.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(IconLabelTabs);
