var mousePoint = view.center;
var amount = 25;
var colors = ['red', 'white', 'blue', 'white'];

var rect = new Rectangle([0, 0], [25, 25]);
	rect.center = mousePoint;
	var path = new Path.Rectangle(rect, 3);
	path.fillColor = colors[2 % 4];
	


