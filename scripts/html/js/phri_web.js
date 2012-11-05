var console = null;
var msgbox = null;
var hmsg_timeout;
var mtimer_on =false;
var connection;
var last_webmsg;
var last_bsmsg;
var in_circ = false;
var circle;
var tcirc;
var messageLayer;
var circleLayer;

function nop() {} //empty function (useful later)

function ws_connect(address, port) {
    try {
        connection = new ros.Connection('ws://' + address + ':' + port);
    } catch (err) {
        msg_fade('Problem creating proxy connection object!');
        log('Problem creating proxy connection object!');
        return;
    }
    msg_fade('Connecting to ' + address + ' on port ' + port + '...');
    log('Connecting to ' + address + ' on port ' + port + '...');

    connection.setOnClose(function (e) {
		$(".need-ros").fadeOut('fast');
		$(".ros_conn").show('fast');
        msg_fade('Rosbridge is not running');
        log('Rosbridge is not running');
    });

    connection.setOnError(function (e) {
        msg_fade('Error!');
    });

    connection.setOnOpen(function (e) {
        msg_fade('Connected to Rosbridge');
		log('Connected to Rosbridge');

		//first publish doesn't seem to work, so publishing a dummy message 
		//so that the first button click publlish works
		connection.publish('/speech', 'std_msgs/String', '{"data":""}');
		connection.publish('/head', 'std_msgs/UInt8', '{"data":0}');
		connection.publish('/larm', 'std_msgs/UInt8', '{"data":0}');
		connection.publish('/rarm', 'std_msgs/UInt8', '{"data":0}');
		connection.publish('/cmd_vel', 'geometry_msgs/Twist', '{"linear":{"x":0,"y":0,"z":0}, "angular":{"x":0,"y":0,"z":0}}');


		//subscribe to web_message (later we'll make this some filtered form of rosout
		sub_to_webmsg();
		sub_to_ballbot_state();
		sub_to_slider();
		$(".ros_col").hide('slow');
    });
}

$( document ).delegate("#main_page", "pageinit", function() {
    console = document.getElementById('console');
    msgbox = document.getElementById('hmsg');
	msg_fade('DOM Ready');
	log('DOM Ready');

	ws_connect("192.168.1.1", "9090");

	$( "#slider1" ).bind( "change", function(event, ui) {
		connection.publish('/head', 'std_msgs/UInt8', '{"data":' + $('#slider1')[0].value + '}');	});
	$( "#slider2" ).bind( "change", function(event, ui) {
		connection.publish('/larm', 'std_msgs/UInt8', '{"data":' + $('#slider1')[0].value + '}');	});
	$( "#slider3" ).bind( "change", function(event, ui) {
		connection.publish('/rarm', 'std_msgs/UInt8', '{"data":' + $('#slider1')[0].value + '}');	});

    var stage = new Kinetic.Stage({
        container: 'kintest',
		width: 300,
		height: 320
    });
    circleLayer = new Kinetic.Layer();
    messageLayer = new Kinetic.Layer();

    circle = new Kinetic.Circle({
        x: stage.getWidth() / 2,
        y: stage.getHeight() / 2 + 10,
        radius: (stage.getHeight()/2) - 10,
        fill: 'SlateGray',
        stroke: 'black',
        strokeWidth: 4,
		opacity: 0.7
    });

	tcirc = new Kinetic.Circle({
        x: stage.getWidth() / 2,
        y: stage.getHeight() / 2 + 10,
        radius: 30,
        fill: 'black',
        stroke: 'black',
        strokeWidth: 4
    });

    circle.on('mousedown', function() {
		in_circ = true;
        var mousePos = stage.getMousePosition();
		touchCircleTwist(mousePos.x, mousePos.y);
    });

    circle.on('touchstart', function() {
		in_circ = true;
        var mousePos = stage.getTouchPosition();
		touchCircleTwist(mousePos.x, mousePos.y);
    });

    circle.on('mouseup touchend mouseout touchout', function() {
		in_circ = false;
		if($( "#radio-choice-a1" )[0].checked){
			stopDrive();
		}
    });

    circle.on('mousemove', function() {
		if(in_circ){
			var mousePos = stage.getMousePosition();
			touchCircleTwist(mousePos.x, mousePos.y);
		}
    });
    circle.on('touchmove', function() {
		if(in_circ){
			var mousePos = stage.getTouchPosition();
			touchCircleTwist(mousePos.x, mousePos.y);
		}
    });

    circleLayer.add(tcirc);
    circleLayer.add(circle);
    stage.add(circleLayer);
    stage.add(messageLayer);

	msg_fade('Kinetic Ready');
	log('Kinetic Ready');
});

function touchCircleTwist(x,y){
	var nx = (x - circle.getX())/circle.getRadius();
    var ny = -(y - circle.getY())/circle.getRadius();
	d = (nx*nx) + (ny*ny);
	if( d < .95){
		nx = Math.round(nx*100.0)/100.0
		ny = Math.round(ny*100.0)/100.0
		writeMessage(messageLayer, 'x: ' + nx + ', y: ' + ny);
		tcirc.setPosition(x,y);
		circleLayer.draw();		
	    connection.publish('/cmd_vel', 'geometry_msgs/Twist', '{"linear":{"x":' + ny + ',"y":0,"z":0}, "angular":{"x":0,"y":0,"z":' + (-nx) + '}}');
	}else{
		if($( "#radio-choice-a1" )[0].checked){
			stopDrive();
		}
	}
}

function stopDrive(){
	writeMessage(messageLayer, 'Stopped');
	tcirc.setPosition( circle.getX(), circle.getY());
	circleLayer.draw();	
	connection.publish('/cmd_vel', 'geometry_msgs/Twist', '{"linear":{"x":0,"y":0,"z":0}, "angular":{"x":0,"y":0,"z":0}}');
}

function sayHi(){
	log("saying: Hello Illah");
	connection.publish('/speech', 'std_msgs/String', '{"data":"Hello Illah"}');
}

function sayNSH(){
	log("saying: Will you take me to the NSH Atrium?");
	connection.publish('/speech', 'std_msgs/String', '{"data":"Will you take me to the NSH Atrium?"}');
}

function writeMessage(messageLayer, message) {
    var context = messageLayer.getContext();
    messageLayer.clear();
    context.font = '18pt Calibri';
    context.fillStyle = 'black';
    context.fillText(message, 10, 25);
}

function log(msg) {
	//print message to our console div (stays until cleared with button)
	console.innerHTML = console.innerHTML + msg + "<br/>";
	//cool animated scoll to bottom of console on addition of more content
	$(console).animate({ scrollTop: $(console).attr("scrollHeight") }, 200);
}

function clear_log() {
	//clear the console
	console.innerHTML = "";
}

function msg_fade(msg) {
	//show the msg(string) in the hsmg div for 1.5 seconds
	//if a message is hasn't faded yet, append new msg to the end and restart countdown
	if($(msgbox).is(":hidden")){
		$(msgbox).show('fast');
		msgbox.innerHTML = msg + "<br/>";
	}
	else{
		msgbox.innerHTML = msgbox.innerHTML + msg + "<br/>";
	}
	if(mtimer_on){clearTimeout(hmsg_timeout);}

	hmsg_timeout = setTimeout(function() {
		$(msgbox).fadeOut('fast');
		mtimer_on = true;
	}, 1500);
}


