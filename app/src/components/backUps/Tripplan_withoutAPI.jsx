import React from "react";
import PlacesAutocomplete, {
  geocodeByAddress,
  getLatLng
} from "react-places-autocomplete";
import LocationSearchInput from "../components/LocationSearchInput";
// import CarIcon from '@material-ui/icons/DirectionsCar';
import AddIcon from "@material-ui/icons/AddCircle";
import CancelIcon from "@material-ui/icons/Cancel";


class DocumentInput extends React.Component {
  render() {
    return <input type="file" name={`document-${this.props.index}-document`} />;
  }
}

class Tripplan extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      // gmapsLoaded: false,
      locaitons: [],
	  documents: [],
    };

    this.addASearchBar = this.addASearchBar.bind(this);
  }

  //   initMap = () => {
  //     this.setState({
  //       gmapsLoaded: true
  //     });
  //   };

  //   componentDidMount() {
  //     window.initMap = this.initMap;
  //     const gmapScriptEl = document.createElement("script");
  //     const API_key = "AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY";
  //     gmapScriptEl.src =
  //       "https://maps.googleapis.com/maps/api/js?key=" +
  //       API_key +
  //       "&libraries=places&callback=initMap";
  //     document
  //       .querySelector("body")
  //       .insertAdjacentElement("beforeend", gmapScriptEl);
  //   }
  componentDidMount() {
    const locations = this.state.locaitons.concat(LocationSearchInput);
	this.setState({ locaitons:locations });
  }

  addASearchBar() {
	this.state.is_add = true
    console.log("add div is clicked");
    const locations = this.state.locaitons.concat(LocationSearchInput);
    this.setState({ locaitons:locations });
    console.log(this.state.locaitons.length);
  }
  
  deleteASearchBar = () => {
    console.log("delete div is clicked");
  };


  render() {
	// console.log("checking: " + this.state.locaitons.state);
	
    const locaitons = this.state.locaitons.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    const documents = this.state.documents.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    return (
      <div>
        <div className="inputs">{documents}</div>{" "}
        {/* {this.state.gmapsLoaded && <LocationSearchInput />} */}
        <div>{locaitons}</div>
        <div>
          <AddIcon color="primary" onClick={this.addASearchBar} />
        </div>
        <div>
          <CancelIcon onClick={this.deleteASearchBar} />
        </div>
      </div>
    );
  }
}
export default Tripplan;
