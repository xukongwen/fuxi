
//首先要理清楚整体的逻辑
//先把圆环的渐变色做出来，这个是先天八卦最核心思想

var path = null;

var mousePoint = view.center;
var amount = 25;
//一个阴阳格子的大小
var box_length = 25;
var gap = 35;
var test_list = [1,1,-1];

var gua1 = [[1], [-1]];
var gua2 = [[1, 1], [-1, 1], [1, -1], [-1, -1]];
var gua3 = [[1, 1, 1],
[-1, 1, 1],
[1, -1, 1],
[-1, -1, 1],
[1, 1, -1],
[-1, 1, -1],
[1, -1, -1],
[-1, -1, -1]];
var gua4 = [[1, 1, 1, 1],
[-1, 1, 1, 1],
[1, -1, 1, 1],
[-1, -1, 1, 1],
[1, 1, -1, 1],
[-1, 1, -1, 1],
[1, -1, -1, 1],
[-1, -1, -1, 1],
[1, 1, 1, -1],
[-1, 1, 1, -1],
[1, -1, 1, -1],
[-1, -1, 1, -1],
[1, 1, -1, -1],
[-1, 1, -1, -1],
[1, -1, -1, -1],
[-1, -1, -1, -1]];
var gua5 = [[1, 1, 1, 1, 1],
[-1, 1, 1, 1, 1],
[1, -1, 1, 1, 1],
[-1, -1, 1, 1, 1],
[1, 1, -1, 1, 1],
[-1, 1, -1, 1, 1],
[1, -1, -1, 1, 1],
[-1, -1, -1, 1, 1],
[1, 1, 1, -1, 1],
[-1, 1, 1, -1, 1],
[1, -1, 1, -1, 1],
[-1, -1, 1, -1, 1],
[1, 1, -1, -1, 1],
[-1, 1, -1, -1, 1],
[1, -1, -1, -1, 1],
[-1, -1, -1, -1, 1],
[1, 1, 1, 1, -1],
[-1, 1, 1, 1, -1],
[1, -1, 1, 1, -1],
[-1, -1, 1, 1, -1],
[1, 1, -1, 1, -1],
[-1, 1, -1, 1, -1],
[1, -1, -1, 1, -1],
[-1, -1, -1, 1, -1],
[1, 1, 1, -1, -1],
[-1, 1, 1, -1, -1],
[1, -1, 1, -1, -1],
[-1, -1, 1, -1, -1],
[1, 1, -1, -1, -1],
[-1, 1, -1, -1, -1],
[1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1]];
var gua6 = [[1, 1, 1, 1, 1, 1],
[-1, 1, 1, 1, 1, 1],
[1, -1, 1, 1, 1, 1],
[-1, -1, 1, 1, 1, 1],
[1, 1, -1, 1, 1, 1],
[-1, 1, -1, 1, 1, 1],
[1, -1, -1, 1, 1, 1],
[-1, -1, -1, 1, 1, 1],
[1, 1, 1, -1, 1, 1],
[-1, 1, 1, -1, 1, 1],
[1, -1, 1, -1, 1, 1],
[-1, -1, 1, -1, 1, 1],
[1, 1, -1, -1, 1, 1],
[-1, 1, -1, -1, 1, 1],
[1, -1, -1, -1, 1, 1],
[-1, -1, -1, -1, 1, 1],
[1, 1, 1, 1, -1, 1],
[-1, 1, 1, 1, -1, 1],
[1, -1, 1, 1, -1, 1],
[-1, -1, 1, 1, -1, 1],
[1, 1, -1, 1, -1, 1],
[-1, 1, -1, 1, -1, 1],
[1, -1, -1, 1, -1, 1],
[-1, -1, -1, 1, -1, 1],
[1, 1, 1, -1, -1, 1],
[-1, 1, 1, -1, -1, 1],
[1, -1, 1, -1, -1, 1],
[-1, -1, 1, -1, -1, 1],
[1, 1, -1, -1, -1, 1],
[-1, 1, -1, -1, -1, 1],
[1, -1, -1, -1, -1, 1],
[-1, -1, -1, -1, -1, 1],
[1, 1, 1, 1, 1, -1],
[-1, 1, 1, 1, 1, -1],
[1, -1, 1, 1, 1, -1],
[-1, -1, 1, 1, 1, -1],
[1, 1, -1, 1, 1, -1],
[-1, 1, -1, 1, 1, -1],
[1, -1, -1, 1, 1, -1],
[-1, -1, -1, 1, 1, -1],
[1, 1, 1, -1, 1, -1],
[-1, 1, 1, -1, 1, -1],
[1, -1, 1, -1, 1, -1],
[-1, -1, 1, -1, 1, -1],
[1, 1, -1, -1, 1, -1],
[-1, 1, -1, -1, 1, -1],
[1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, 1, -1],
[1, 1, 1, 1, -1, -1],
[-1, 1, 1, 1, -1, -1],
[1, -1, 1, 1, -1, -1],
[-1, -1, 1, 1, -1, -1],
[1, 1, -1, 1, -1, -1],
[-1, 1, -1, 1, -1, -1],
[1, -1, -1, 1, -1, -1],
[-1, -1, -1, 1, -1, -1],
[1, 1, 1, -1, -1, -1],
[-1, 1, 1, -1, -1, -1],
[1, -1, 1, -1, -1, -1],
[-1, -1, 1, -1, -1, -1],
[1, 1, -1, -1, -1, -1],
[-1, 1, -1, -1, -1, -1],
[1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1]]




// 画基本的横向阴阳渐变图 
var topLeft = [20, 80];
var bottomRight = [1000, 50];//这里竟然是增加的值

// Create a rectangle shaped path between
// the topLeft and bottomRight points:
var path = new Path.Rectangle(topLeft, bottomRight);

// 由什么颜色渐变成什么颜色
var gradient = new Gradient(['white', 'black']);

// 在何种方向和形状上渐变
var gradientColor = new Color(gradient, topLeft, bottomRight);

// 应用这个渐变设置
path.fillColor = gradientColor;



// 画基本的圆渐变，这是先天八卦的本意（吗）
var circle = new Path.Circle(mousePoint, 200);
var gradientColorCircle = new Color(gradient, [circle.position.x,circle.position.y-200], [circle.position.x,circle.position.y+200]);
circle.strokeColor = gradientColorCircle;
circle.strokeWidth = 50;









//这是如何读json 
var url = "data/gua-3.json"/*json文件url，本地的就写本地的位置，如果是服务器的就写服务器的路径*/
var request = new XMLHttpRequest();
var gua_data = [];
	request.open("get", url);/*设置请求方法与路径*/
	request.send(null);/*不发送数据到服务器*/
	request.onload = function () {/*XHR对象获取到返回信息后执行*/
			if (request.status == 200) {/*返回状态为200，即为数据获取成功*/
				var json = JSON.parse(request.responseText);
				//gua_data = json;
				for(var i=0;i<json.length;i++){
					//console.log(json[i]);
					gua_data.push(json[i]);//放入一个空的组
				}
				
			}
		}


//console.log(gua_data);
//console.log(gua3);

//画一个阳
function draw_yin(x,y){
	var rect = new Rectangle(x,y,box_length,box_length);
	var path = new Path.Rectangle(rect,3);
	path.fillColor = 'black';
	path.removeOnDrag();
}
//画一个阴
function draw_yang(x,y){
	var rect = new Rectangle(x,y,box_length,box_length);
	var path = new Path.Rectangle(rect,3);
	path.fillColor = 'white';
	path.strokeColor = 'black';
	path.removeOnDrag();


}

//画一个卦
function draw_one_gua(x,y,list){
	var total = 1;
	for (var i=0; i<list.length; i++){
		if (list[i]==1){
			draw_yang(x,y+(gap*total));
			total = total + 1;
		};

		if (list[i]==-1){
			draw_yin(x,y+(gap*total));
			total = total + 1;
		}
	}
}

//画一组卦
function draw_all_gua(x,y,list){
	var total = 1;
	for (var i=0; i<list.length; i++){
		draw_one_gua(x+(gap*total),y,list[i]);
		total = total + 1;
	}
}



//draw_all_gua(mousePoint.x,10,gua1);
//draw_all_gua(mousePoint.x - (1*gap),(gap+box_length-10),gua2);
//draw_all_gua(mousePoint.x - (3*gap),200,gua3);
//draw_all_gua(10,200,gua6);




function onMouseDrag(event) {
	//console.log(event.point.x)
	//draw_all_gua(event.point.x,event.point.y,gua6);
	//draw_yin(event.point.x,event.point.y)
	//path.removeOnDrag();
}


// 现实鼠标所在坐标 item at {x: 30, y: 30}:
var text = new PointText(new Point(30, 30));
text.fillColor = 'black';

text.content = '移动鼠标以查看位置坐标';

function onMouseMove(event) {
    // Each time the mouse is moved, set the content of
    // the point text to describe the position of the mouse:
    text.content = '鼠标坐标: ' + event.point.toString();
}


//我发现可能先天八卦需要用弧线的黑白来表示可能才更准确，而不是黑白点

function getCreateArcInfo(degrees,center,radius){
    return {
        from: {
            x:center.x + radius,
            y: center.y
        },
        through: {
            x: center.x + Math.cos(degrees/2) * radius,
            y: center.y + Math.sin(degrees/2) * radius
        },
        to: {
            x: center.x + Math.cos(degrees) * radius,
            y: center.y + Math.sin(degrees) * radius
        },
        strokeColor: 'black'
    }
}
//var arcValues = getCreateArcInfo(1.5708, {x:253,y:334}, 160)
//var myArc = new Path.Arc(arcValues)
//myArc.strokeWidth = 10