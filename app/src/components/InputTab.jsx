import React from "react";
import PropTypes from "prop-types";
import Paper from "@material-ui/core/Paper";
import { withStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import CarIcon from "@material-ui/icons/DirectionsCar";
// import Map from "@material-ui/icons/Map";
import Navigation from "@material-ui/icons/Navigation";
// import CarGasInput from "./UserInput";
import UserInput from "../components/UserInput";
import Typography from "@material-ui/core/Typography";
// import Tripplan from "../components/backUps/Tripplan";
import PathToGo from "../components/PathTogo";
import "./InputTab.css"

const styles = {
  root: {
    flexGrow: 1,
    maxWidth: 310,
    height: "80vh",
    backgroundColor: "#eef8fd",

    // position: 'absolute',
    // left: 0,
    // right: 0,
    // bottom: 0,
    // background: "#ff4444",
    // padding: "3px 8px",
    // color: "#fff",
    // zindex: "1"
  },
  header: {
    backgroundColor: "White"
  }
};

function TabContainer(props) {
  return (
    <Typography component="div" style={{ padding: 8 * 3 }}>
      {props.children}
    </Typography>
  );
}

class IconLabelTabs extends React.Component {
  state = {
    value: 0
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;

    return (
      <div className="float">
      <Paper square className={classes.root}>
        <Tabs
          className={classes.header}
          value={this.state.value}
          onChange={this.handleChange}
          fullWidth
          indicatorColor="secondary"
          textColor="secondary"
        >
          <Tab icon={<CarIcon />} label="Car&Gas&Destination" />
          {/* <Tab icon={<Map />} label="Trip Plan" /> */}
          <Tab icon={<Navigation />} label="Path to Go" />
        </Tabs>
      
        {value === 0 && (
          <TabContainer>
            <UserInput />
            {/* <CarGasInput /> */}
          </TabContainer>
        )}
        {/* {value === 1 && <TabContainer><Tripplan /></TabContainer>} */}
        {value === 1 && <TabContainer>{<PathToGo />}</TabContainer>}
      </Paper>
      {/* <GoogleMapDirection/> */}
      </div>
    );
  }
}

IconLabelTabs.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(IconLabelTabs);
