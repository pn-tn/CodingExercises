// import * as RouRob from "./RouRob.js";

// variables
var process = [];

// add the process into the simulation
// basically just process the inputs
// todo:
//   -- get the inputs and add to variable
//   -- add a div element in html to display the process
//   -- set the input boxes back to empty
function AddProcess() {
    var new_process = {
        length: document.getElementById("len").value,
        arrival: document.getElementById("AT").value
    };
    process.push(new_process);
	console.log(process);
}

// Starts the simulation
// -- cannot add more processes
// -- allows incrementing and playing the simulation
function Start() {

}

// Increment the Simulation by 1
function Increment() {

}


// event listener hehehe
document.addEventListener('DOMContentLoaded', function() {

	document.getElementById("add-process").addEventListener("click", AddProcess);

    });
