//Import subcomponets
import React from "react"
import Nav from "../components/nav"
import MapContainer from "../components/mapContainer"
import Form from "../components/form"

export default class Main extends React.Component {
  constructor(props) {
   super(props);
   
   //Here we bind these functions to this component (class) if you do not do this when babel compiles all the react componets into the one large bundle script, the browser will not know what "this" is referring to
   this.toggleNavBar = this.toggleNavBar.bind(this);
   this.handleInputChange = this.handleInputChange.bind(this);
   this.handleSubmit = this.handleSubmit.bind(this);
   this.resetDraw = this.resetDraw.bind(this);
    
   //set the state of this componet dictionary of data we want to store
   this.state = {
     sidebarOpen: false,
     start: '',
     stop: '',
     day: '',
     time: '',
     drawRoute: false
   };
 }

 //Gets input from form in Nav componet. This function is passed to the Nav componet below as a prop. ie. <Nav input={this.handleInputChange} />
 handleInputChange(event) {
   const target = event.target;
   const value = target.value;
   const name = target.name;
   this.setState({
     [name]: value
   });
 }

 // Handels submit event of form. This function is passed to the Nav componet below as a prop. ie. <Nav submit={this.handleSubmit} />
 handleSubmit(event) {
   alert('Submitted');
   event.preventDefault(); //stops default form submit which sends a http request and reloads the page.
   this.setState({
     drawRoute: true
   });
 }

 //After drawing a route, changes the state back to false. This function is passed to the MapContainer componet which will draw the route. ie. <MapContainer reset={this.resetDraw} />
 resetDraw(event) {
   this.setState({
     drawRoute: false
   });
 }

  //Funtion to toggle nav bar, this function is passed as a prop to the MapContainer component. ie. <MapContainer onClick={this.toggleNavBar} />
  toggleNavBar() {
    this.setState({sidebarOpen: !this.state.sidebarOpen}); //toggles sidebarOpen value
  }

  render() {
    //checks weather the sidebar is open or not in the state of this component and passes the variables as componets to the Nav and Mapcontainer to use in their CSS properties.
    let isSidebarOpen = this.state.sidebarOpen ? true : false;
    let isMapContainerWide = this.state.sidebarOpen ? true : false;

    return (
      <div>
        <Nav display={isSidebarOpen} submit={this.handleSubmit} input={this.handleInputChange} />
        <MapContainer display={isMapContainerWide} onClick={this.toggleNavBar} route={this.state} reset={this.resetDraw}/>
      </div>
    )
  }
}

