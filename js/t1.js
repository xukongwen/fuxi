
//相当于是python里的print()
console.log("hi");

//所以弧度与角度的转化是
//1rad = 180/π
//那么360°就是四个PI
//360°用弧度计算就是2*PI个弧度，这样也挺好，相当于是1个单位就是180°

//测试用的卦的数组
var gua_1 = [1,-1]
var gua_2 = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
var gua_3 = [
	[1, 1, 1],
	[-1, 1, 1],
	[1, -1, 1],
	[-1, -1, 1],
	[1, 1, -1],
	[-1, 1, -1],
	[1, -1, -1],
	[-1, -1, -1]
]

//Path.Arc(arcValues) 这个方法画arc就是三个点，一个起始，一个结束，一个中间点

var PI = Math.PI

//一些文字的设置
var text = new PointText(new Point(30, 30));
var text_list = new PointText(new Point(30, 60));
text.fillColor = 'black';
text_list.fillColor = 'black';

text.content = '测试';

//获取鼠标坐标
function onMouseMove(event) {
    text.content = '鼠标坐标: ' + event.point.toString();
}


//通过弧度，中心点，半径坐标画圆弧
//这里1就是180°，2就是360°
function getCreateArcInfo(degrees,center,radius,color,width){
    return {
        from: {
            x:center.x + radius,
            y: center.y
        },
        through: {
            x: center.x + Math.cos(degrees*PI/2) * radius,
            y: center.y + Math.sin(degrees*PI/2) * radius
        },
        to: {
            x: center.x + Math.cos(degrees*PI) * radius,
            y: center.y + Math.sin(degrees*PI) * radius
        },
        strokeColor: color,
		strokeWidth:  width,
		//new_path: Path.Arc(from, through, to)
	
    }
}

function darw_arc(lad,center,radius,color,width){
	var arcValues = getCreateArcInfo(lad, center, radius,color,width)
	var myArc = new Path.Arc(arcValues)
}

darw_arc(-1, view.center, 180,'black',30)
darw_arc(-0.5, view.center, 220,'black',15)
darw_arc(-0.5, view.center, 220,'black',15)

//js从组里取数值的方法真奇怪

function draw_gua(){
	for (var i = 0; i < gua_1.length; i++){
		//text_list.content = gua_1[i]
		var gua = gua_1[i]
		console.log(gua);
		if (gua == 1) {
			darw_arc(-1, view.center, 180,'red')
		}
		if (gua == -1) {
			darw_arc(1, view.center, 180,'black')
		}
		
	}
}

//draw_gua()

//他这个貌似是把一个圆弧add到一个path上面，那么这样很好，画圆弧就只管画一个对的弧度，然后其他用add来解决
function larg_arc(){
	var values = {
		points: 20,
		radius: 20,
		initialRadius: 10
	};
	for (var i = 0; i < 20; i++) {
		var path = new Path({
			fillColor: i % 2 ? 'red' : 'black',
			closed: true
		});

		var point = new Point({
			length: values.initialRadius + values.radius * i,
			angle: 0
		});
		for (var j = 0; j <= values.points; j++) {
			point.angle += 360 / values.points;
			if (j == 0) {
				path.add(view.center + point);
			} else {
				path.arcTo(view.center + point);
			}
		}
		project.activeLayer.insertChild(0, path);
	}
}

larg_arc()

//draw_arc()

