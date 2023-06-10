// import * as RouRob from "./RouRob.js";

// variables
var process = [];

// add the process into the simulation
// basically just process the inputs
// todo:
//   -- get the inputs and add to variable
//   -- add a div element in html to display the process
function AddProcess() {
    var new_process = {
        length: document.getElementById("len").value,
        arrival: document.getElementById("AT").value,
		name: null,
		completion: null,
		progress: 0
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
	progressElement.setAttribute("value", "0"); // Set the current progress value
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

	// disable this
	document.getElementById("add-process").disabled = true;
	document.getElementById("algo").disabled = true;
	document.getElementById("quantum").disabled = true;

	// enable this
	document.getElementById("play").disabled = false;
	document.getElementById("incr").disabled = false;

}

// Increment the Simulation by 1
function Increment() {

}

// just constantly plays the simulation
// just loop the increment until it ends i guess
function Play() {

}

// resets the simulation
function Reset(){
	
	// remove the divs
	var elements = document.querySelectorAll(".process-div");

	for (var i = 0; i < elements.length; i++) {
		var element = elements[i];
		element.parentNode.removeChild(element);
	}

	// reset the process
	process = [];
	console.log(process);

	// re-enables everything that was disabled
	document.getElementById("add-process").disabled = false;
	document.getElementById("algo").disabled = false;
	document.getElementById("quantum").disabled = false;

	document.getElementById("play").disabled = true;
	document.getElementById("incr").disabled = true;

}

// event listener hehehe
document.addEventListener('DOMContentLoaded', function() {

	document.getElementById("add-process").addEventListener("click", AddProcess);
	document.getElementById("reset").addEventListener("click", Reset);
	document.getElementById("start").addEventListener("click", Start);

    });
