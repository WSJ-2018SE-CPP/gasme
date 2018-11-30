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
    maxWidth: 380,
    height: "80vh",
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
    response: {
      status: 0,
      gas_price: [0.0],
      mileage: ["0 mi"],
      trip1: [],
      time: ["0 min"],
      gallons_to_fuel: [0.0],
      cost: [0.0]
    }
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  //use the data from the child
  response_to_state = dataFromChild => {
    console.log(dataFromChild);
    this.setState({ response: dataFromChild });
    console.log(this.state.response);
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;
    var response = this.state.response;

    return (
      <div>
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-3">
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
            <div class="col-md-9">
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
