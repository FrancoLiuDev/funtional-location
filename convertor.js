const tw = require("./tw")
var fs = require("fs")

var citys = {}
var areas = {}

tw.forEach(location => {
	var code = location.Zip5
	var Zip3 = code.substring(0, 3)

	if (citys[location.City]) {
		citys[location.City][Zip3] = location.Area
	} else {
		citys[location.City] = {}
		citys[location.City][Zip3] = location.Area
	}

	if (areas[Zip3]) {
		areas[Zip3][code] = {
			city: location.City,
			area: location.Area,
			road: location.Road,
			scope: location.Scope
		}
	} else {
		areas[Zip3] = {}
		areas[Zip3][code] = {
			city: location.City,
			area: location.Area,
			road: location.Road,
			scope: location.Scope
		}
	}

	console.log("location", location)
})

fs.writeFile("citys.json", JSON.stringify(citys), function(err) {
	if (err) {
		return console.log(err)
	}

	console.log("The file was saved!")
})

fs.writeFile("aras.json", JSON.stringify(areas), function(err) {
	if (err) {
		return console.log(err)
	}

	console.log("The file was saved!")
})
