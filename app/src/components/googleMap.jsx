import React, { Component } from 'react';

// import GoogleMapReact from 'google-map-react';

// const AnyReactComponent = ({ text }) => <div>{text}</div>;

// class googleMap extends Component {
//   static defaultProps = {
//     center: {
//       lat: 59.95,
//       lng: 30.33
//     },
//     zoom: 11
//   };

//   render() {
//     return (
//       // Important! Always set the container height explicitly
//       <div style={{ height: '100vh', width: '100%' }}>
//         <GoogleMapReact
//           bootstrapURLKeys={{ key: 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY' }}
//           defaultCenter={this.props.center}
//           defaultZoom={this.props.zoom}
//         >
//           <AnyReactComponent
//             lat={59.955413}
//             lng={30.337844}
//             text={'Kreyser Avrora'}
//           />
//         </GoogleMapReact>
//       </div>
//     );
//   }
// }

// export default googleMap;

import { Map, InfoWindow, Marker, GoogleApiWrapper } from 'google-maps-react';

class googleMap extends Component {
	render() {
		return (
			<div>
                <p>hello</p>
				<Map google={this.props.google} zoom={14}>
					<Marker onClick={this.onMarkerClick} name={'Current location'} />

					<InfoWindow onClose={this.onInfoWindowClose}>
						{/* <div>
              <h1>{this.state.selectedPlace.name}</h1>
            </div> */}
					</InfoWindow>
				</Map>
			</div>
		);
	}
}

export default GoogleApiWrapper({
	apiKey: 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
})(googleMap);
