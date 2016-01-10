$(document).ready(function () {

	document.goBlend = function () {
		var file = $("input#upload")[0].files[0];
		var reader = new FileReader();
		$("div#cont").remove();
		reader.onload = function (e) {
			var data = atob(reader.result.replace("data:;base64,", ""));
			var newf = main(data);
			$("a#dl")[0].setAttribute("href", 'data:text/plain;charset=utf-8,' + encodeURIComponent(newf));
			$("a#dl")[0].setAttribute("download", file.name);
		}
		reader.readAsDataURL(file);
		$("button#dlb").show();
	}
	
	$("button#dlb").hide()

});