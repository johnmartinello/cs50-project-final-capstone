
document.addEventListener("DOMContentLoaded", function () {
	document.querySelector("#menuButton").addEventListener("click", open_closeNav);
	document.querySelector("#pre-post").addEventListener("click", professor_post_open);
	document.querySelector("#cancel-button").addEventListener("click", professor_post_close);
	
	//assign a eventlistener for each assignment post
	const assignmentDiv = document.querySelectorAll(".assignment")
	assignmentDiv.forEach( (assignmentDiv) => {
    assignmentDiv.addEventListener("click", postLink);
});


	index();
});

//hide the sidenav on load
function index() {
	const sideNav = document.getElementById("sideNav");
	const content = document.getElementById("content");

	sideNav.style.width = "0";
	content.style.marginLeft = "0";
	sideNav.style.left = "-35px";
}


function open_closeNav() {
	const sideNav = document.getElementById("sideNav");
	const content = document.getElementById("content");

	if (sideNav.style.width === "25vh") {
		sideNav.style.width = "0";
		content.style.marginLeft = "0";
		sideNav.style.left = "-35px";
	} else {
		sideNav.style.width = "25vh";
		content.style.marginLeft = "25vh";
		sideNav.style.left = "0";
	}
}


function professor_post_open() {
	const professorPostDiv = document.getElementById("professor-post");
	const prePostDiv = document.getElementById("pre-post");

	if (prePostDiv.style.display !== "none") {
		professorPostDiv.style.display = "block";
		prePostDiv.style.display = "none";
	}
}

function professor_post_close() {
	const professorPostDiv = document.getElementById("professor-post");
	const prePostDiv = document.getElementById("pre-post");

	if (prePostDiv.style.display === "none") {
		professorPostDiv.style.display = "none";
		prePostDiv.style.display = "block";
	}
}

//links the user to the assignment post clicked
function postLink() {
	console.log("click");
	var link = this.getAttribute('data-link');
	if (link) {
		window.location.href = link;
	}
}