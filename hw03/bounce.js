console.log("hello");
var c = document.getElementById("canvas");
var circle_botton = document.getElementById("circle");
var DVD = document.getElementById("DVD");
var stop = document.getElementById("stop");
var ctx = canvas.getContext("2d");
var requestID;

var size = 0;
var size_dir = 1;
var x = Math.round((Math.random() * 400) + 1);
var y = Math.round((Math.random() * 400) + 1);
var xdir = 1;
var ydir = -1;
var function_type = false;
var function_on = false;

circle.addEventListener("click",function(e){function_type = false;function_on=true;});
DVD.addEventListener("click",function(e){function_type=true;function_on=true;});
stop.addEventListener("click", function(e){function_on=false;});

var next = function(e){
    if(function_on){
	if(function_type){
	    ctx.fillStyle = "#ffffff";
	    ctx.fillRect(0,0,500,500);
	    if (x >= (canvas.width - 60) || x <= 0 ) {
		xdir = -xdir;
	    } 
	    if ( y >= (canvas.height - 40) || y <= 0 ) {
		ydir = -ydir;
		console.log(ydir);
	    }else{
		ydir += .1;
	    }
	    x += xdir;
	    y += ydir;
	    var logo = new Image();
	    logo.src = "logo_dvd.jpg";
	    ctx.drawImage(logo,x,y,60,40);
	}else{
	    ctx.fillStyle = "#ffffff";
	    ctx.fillRect(0,0,500,500);
	    if(size > 200){
		size_dir = -1
	    }
	    if(size < 1){
		size_dir = 1;
	    }
	    size+=size_dir;
	    console.log(size);
	    ctx.beginPath();
	    ctx.fillStyle = "#123456";
	    ctx.arc(canvas.width/2, canvas.height/2, size, 0, 2*Math.PI);
	    ctx.fill();
	}
    }
    window.setTimeout(next,10);
}

next();
