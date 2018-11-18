import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import CarIcon from '@material-ui/icons/DirectionsCar';
import Map from '@material-ui/icons/Map';
import Navigation from '@material-ui/icons/Navigation';
import Typography from '@material-ui/core/Typography';
import CarGasInput from '../components/CarGasInput';

function TabContainer(props) {
	return (
		<Typography component="div" style={{ padding: 8 * 3 }}>
			{props.children}
		</Typography>
	);
}

TabContainer.propTypes = {
	children: PropTypes.node.isRequired
};

const styles = (theme) => ({
	root: {
		flexGrow: 1,
		width: '100%',
		backgroundColor: theme.palette.background.paper
	}
});

class ScrollableTabsButtonForce extends React.Component {
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
			<div style={{ display: 'inline-block' }}>
				<div className={classes.root}>
					<AppBar position="static" color="default">
						<Tabs
							value={value}
							onChange={this.handleChange}
							scrollable
							scrollButtons="on"
							indicatorColor="primary"
							textColor="primary"
						>
							<Tab label="car & gas" icon={<CarIcon />} />
							<Tab label="trip plan" icon={<Map />} />
							<Tab label="path to go" icon={<Navigation />} />
						</Tabs>
					</AppBar>
					{value === 0 && (
						<TabContainer>
							<CarGasInput />
						</TabContainer>
					)}
					{value === 1 && <TabContainer>trip plan</TabContainer>}
					{value === 2 && <TabContainer>path to go</TabContainer>}
				</div>
			</div>
		);
	}
}

ScrollableTabsButtonForce.propTypes = {
	classes: PropTypes.object.isRequired
};

export default withStyles(styles)(ScrollableTabsButtonForce);
