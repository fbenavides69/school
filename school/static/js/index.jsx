// index.jsx
import React from "react";
import ReactDOM from "react-dom";
import Welcome from "./welcome";
import Table from "./table";

ReactDOM.render(<Welcome />, document.getElementById("react-welcome"));
ReactDOM.render(<AlumniTable />, document.getElementById("react-alumni-table"));
