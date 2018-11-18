import React from "react";
import PlacesAutocomplete, {
  geocodeByAddress,
  getLatLng
} from "react-places-autocomplete";
import LocationSearchInput from "../../components/LocationSearchInput";
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
      origin: [],
      destination:[],
      documents:[]
    };

    this.addASearchBar = this.addASearchBar.bind(this);
    this.add = this.add.bind(this);
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
    // var locations = this.state.locaitons.concat(LocationSearchInput);
    // this.setState({ locaitons: locations });
    // console.log("first: " + locaitons.length.toString());
    // var locationss = locaitons.concat(LocationSearchInput);
    
    //TODO: it can't create two 
    var newArray = this.state.locaitons.slice();    
    newArray.push(LocationSearchInput); 
    // newArray.push(LocationSearchInput);     
    this.setState({ locaitons: newArray });

    // var docs = this.state.documents.concat(DocumentInput);
    //testing another component
    var docs = this.state.documents.slice();    
    docs.push(DocumentInput); 
    docs.push(DocumentInput);  
    this.setState({documents:docs });

    //new trial
    const origin = this.state.origin.concat(LocationSearchInput);
    this.setState({origin:origin});

    const destination = this.state.destination.concat(LocationSearchInput);
    this.setState({destination:destination});
  }
  
  add() {
    var docs = this.state.documents.concat(DocumentInput);
    this.setState({documents:docs });
  }

  addASearchBar() {
    console.log("add div is clicked");
    var locations = this.state.locaitons.concat(LocationSearchInput);
    this.setState({ locaitons: locations });
  }

  deleteASearchBar = () => {
    console.log("delete div is clicked");
    console.log("checking: " + this.state.locaitons[0].props.adress);
  };

  render() {
    const origin = this.state.origin.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    const destination = this.state.destination.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    const locaitons = this.state.locaitons.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    const documents = this.state.documents.map((Element, index) => {
      return <Element key={index} index={index} />;
    });

    console.log("in render: location#: " + this.state.locaitons.length.toString());
    console.log("in render: origin#: " + this.state.origin.length.toString());
    console.log("in render: destination#" + this.state.destination.length.toString());
    if(this.state.destination.length === 1){
      // console.log("in render: destination#" + this.state.destination[0].props);
    }

    return (
      <div>
        {/* {this.state.gmapsLoaded && <LocationSearchInput />} */}
        {/* <div>origin: {origin}</div> */}
        <div>{locaitons}</div>
        {/* <div>destination: {destination}end of destination</div> */}
        <p>================================</p>
        <p>testing adding 2 components at an array in a state</p>
        <div>{documents}</div>
        <button onClick={this.add}>add</button>
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
