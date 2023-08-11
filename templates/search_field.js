
$(document).ready(function () {
	$("#search-btn").click(function () {
		$("#search").animate({ width: "90%"});
		const s = document.getElementById("generated-image");
		s.style.visibility = "visible";
	});
});

