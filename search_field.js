

function showMenu() {
	var menu_icon = document.getElementById("menu-items");
	if (menu_icon.style.display === "block") {
		menu_icon.style.display = "none";
	}
	else {
		menu_icon.style.display = "block";
	}
}


$(document).ready(function () {
	$("#menu-button").click(function () {
		var button_pos = document.getElementById("menu-icon-div");
		var menu = document.getElementById("menu");
		if (button_pos.style.left === "70%") {
			$("#menu").animate({ width: "0", height: "0" });
			$("#menu-icon-div").animate({ left: "0" });
		} else {
			$("#menu").animate({ width: "25%", height: "93%" });
			$("gen-img").animate({  });
			$("#menu-icon-div").animate({ left: "70%" });
		}
	});
});


$(document).ready(function () {
	$("#search-btn").click(function () {
		$("#search").animate({ width: "90%" });
		// $("#menu-img").animate({ width: "80%" });
		const s = document.getElementById("generated-image");
		s.style.visibility = visible;
	});
});

