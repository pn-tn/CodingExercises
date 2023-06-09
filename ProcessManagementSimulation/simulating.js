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

	var process_div = document.createElement("div");
	process_div.classList.add("process-div");

	var pLength = document.createElement("p");
	pLength.textContent = "Length: " + new_process.length;

	var pArrival = document.createElement("p");
	pArrival.textContent = "Arrival: " + new_process.arrival;
	
	var progressElement = document.createElement("progress");
	progressElement.setAttribute("value", "1"); // Set the current progress value
	progressElement.setAttribute("max", new_process.length); // Set the maximum progress value
	
	process_div.appendChild(progressElement);
	process_div.appendChild(pLength);
	process_div.appendChild(pArrival);

	var process_container = document.getElementById("process-container");
	process_container.appendChild(process_div);
	
}

// Starts the simulation
// -- cannot add more processes
// -- allows incrementing and playing the simulation
function Start() {

}

// Increment the Simulation by 1
function Increment() {

}

// just constantly plays the simulation
function Play() {

}

// resets the simulation
function Reset(){
	
	// remove the divs
	var elements = document.querySelectorAll(".process-div");

	// Loop through the selected elements and remove them
	for (var i = 0; i < elements.length; i++) {
		var element = elements[i];
		element.parentNode.removeChild(element);
	}

	// reset the process
	process = [];
	console.log(process);

}

// event listener hehehe
document.addEventListener('DOMContentLoaded', function() {

	document.getElementById("add-process").addEventListener("click", AddProcess);
	document.getElementById("reset").addEventListener("click", Reset);

    });
