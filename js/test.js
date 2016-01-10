var grouper = function (iterable, n, fillvalue) {
	var extra = iterable.length % n,
		result = [];
	while (extra) {
		iterable.push(fillvalue);
		extra--;
	}
	while (iterable.length) {
		elem = [];
		while (elem.length < n) {
			elem.push(iterable.pop())
		}
		elem.reverse()
		result.push(elem);
	}
	result.reverse()
	return result;
}

var flatten = function (lst) {
	var result = [];
	for (var i in lst) {
		if (!(lst[i] instanceof Array)) {
			result.push([lst[i]]);
		}
		else {
			result.push(flatten(lst[i]));
		}
	}
	return result.reduce(function (i, j) {
		return i.concat(j);
	});
}

var pnm_to_bin = function (p) {
	var w = parseInt(p[1].split(" ")[0]),
		h = parseInt(p[1].split(" ")[1]),
		data = p.slice(3).join(" ").replace("\n", " ").split(/\s+/g),
		bin = [];
	data = data.filter(function (i) {
		return i.length;
	}).map(function (i) {
		return parseInt(i);
	});
	var lines = grouper(data, w*3),
		i = 0;
	while (i < lines.length) {
		var lgroup = grouper(lines[i], 3),
			d = [],
			j = 0;
		while (j < lgroup.length) {
			d.push(lgroup[j]);
			j++;
		}
		bin.push(d);
		i++;
	}
	return bin;
}

var bin_to_pnm = function (b) {
	pnm = "P3 " + b[0].length + " " + b.length + " 255 ";
	b = flatten(b);
	pnm += b.map(function (i) {
		return i.toString();
	}).join(" ");
	return pnm;
}

var imageblender = function (img) {
	var h = img.length,
		w = img[0].length,
		x = 0,
		y = 0;
	nimg = new Array() .concat(img);
	while (y < w) {
		while (x < h) {
			var i = 0;
			while (i < 3) {
				val = Math.floor((img[x][y][i] + img[x][w+~y][i] + img[h+~x][y][i] + img[h+~x][w+~y][i]) / 4);
				nimg[x][y][i] = val;
				nimg[x][w+~y][i] = val;
				nimg[h+~x][y][i] = val;
				nimg[h+~x][w+~y][i] = val;
				i++;
			}
			x++;
		}
		y++;
	}
	return nimg;
}

var main = function (content) {
	b = pnm_to_bin(content.split("\n"));
	bin = imageblender(b);
	return bin_to_pnm(bin);
}

var go = function () {
	var file = $("input#upload")[0].files[0];
	var reader = new FileReader();
	reader.onload = function (e) {
		var data = reader.result;
		data = atob(data.replace("data:;base64,", ""));
		$("textarea#output").text(main(data));
	}
	reader.readAsDataURL(file);
}