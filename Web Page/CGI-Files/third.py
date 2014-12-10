#!/usr/local/bin/python

import cgi, Cookie, os

form = cgi.FieldStorage()
source = form.getvalue('sourceAddress')
dest = form.getvalue('destAddress')
source_lat = form.getvalue('sourceLat')
source_long = form.getvalue('sourceLong')
dest_lat = form.getvalue('destLat')
dest_long  = form.getvalue('destLong')
rest_address = form.getvalue('restAddress')
rest1 = form.getvalue('rest1') 

execfile('../p2.py')
execfile('../p3.py')

rest_coord = addressToCoordinates(rest_address)

print "Content-type:text/html\r\n\r\n"
print"<html>"

print"<head>"
print"<title>Directions</title>"

print "<script type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js\"></script>"
print "<script type=\"text/javascript\" src=\"http://maps.google.com/maps/api/js?sensor=true\"></script>"
print "<script type=\"text/javascript\" src=\"../gmaps-master/gmaps.js\"></script>"
	
print"<style>"
	
print".map_canvas {"

print"height: 350px;"
print"width: 96%;"
print"margin-left: 2%;"
print"margin-top: 1%;"
print"margin-bottom: 20px;"

print"}"

print"#map {"
print"height: 350px;"
print"width: 96%;"
print"margin-left: 2%;"
print"margin-top:1%;"
print"margin-bottom: 20px;"
print"background-color: black"
print"}"
		
print"#instructions {"
print"background-color: white;"
print"color: black;"
print"width: 96%;"
print"margin-left: 2%;"
print"padding-bottom: 10px;"
print"padding-top: 10px;"
print"overflow: auto;"
print"}"

print"body {"
print"background-image: url(\"../Road.jpg\");"
print"background-color: #cccccc;"
		
print"}"
		
		
print".Search_button{"
			
print"border:1px solid #000000;-webkit-box-shadow: #B7B8B8 0px 1px 0px inset;-moz-box-shadow: #B7B8B8 0px 1px 0px inset; box-shadow: #B7B8B8 0px 1px 0px inset; -webkit-border-radius: 3px; -moz-border-radius: 3px;border-radius: 3px;font-size:12px;font-family:arial, helvetica, sans-serif; padding: 10px 10px 10px 10px; text-decoration:none; display:inline-block;text-shadow: -1px -1px 0 rgba(0,0,0,0.3);font-weight:bold; color: #000000;"
print"background-color: #FFFFCC; background-image: -webkit-gradient(linear, left top, left bottom, from(#a5b8da), to(#FFFF00));"
print"background-image: -webkit-linear-gradient(top, #FFFFCC, #FFFF00);"
print"background-image: -moz-linear-gradient(top, #FFFFCC, #FFFF00);"
print"background-image: -ms-linear-gradient(top, #FFFFCC, #FFFF00);"
print"background-image: -o-linear-gradient(top, #FFFFCC, #FFFF00);"
print"background-image: linear-gradient(to bottom, #FFFFCC, #FFFF00);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#FFFFCC, endColorstr=#FFFF00);"
print"margin-left: 45%;"
print"width: 10%;"
print"text-align: center;"
print"margin-top: 20px;"
		
print"}"

print".Search_button:hover{"
		
print"border:1px solid #000000;"
print"background-color: #F2F280; background-image: -webkit-gradient(linear, left top, left bottom, from(#F2F280), to(##E6E600));"
print"background-image: -webkit-linear-gradient(top, ##F2F280, ##E6E600);"
print"background-image: -moz-linear-gradient(top, #F2F280, ##E6E600);"
print"background-image: -ms-linear-gradient(top, #F2F280, ##E6E600);"
print"background-image: -o-linear-gradient(top, #F2F280, ##E6E600);"
print"background-image: linear-gradient(to bottom, #F2F280, ##E6E600);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#F2F280, endColorstr=##E6E600);"
		
print"}"
	
print"</style>"

print"<script type=\"text/javascript\">"
print"var map;"
print"$(document).ready(function(){"
print"map = new GMaps({"
print"el: '#map',"
print"lat: %s," % source_lat
print"lng: %s" % source_long
print"});"
			
print"map.travelRoute({"
print"origin: [%s, %s]," %(source_lat, source_long)
print"destination: [%s, %s]," %(rest_coord[0], rest_coord[1])
print"travelMode: 'driving',"
print"step: function(e){"
print"$('#instructions').append('<li>'+e.instructions+'</li>');"
print"$('#instructions li:eq('+e.step_number+')').delay(450*e.step_number).fadeIn(200, function(){"
print"map.drawPolyline({"
print"path: e.path,"
print"strokeColor: '#131540',"
print"strokeOpacity: 0.6,"
print"strokeWeight: 6"
print"});"
print"});"
print"}"
print"});"

print"map.travelRoute({"
print"origin: [%s, %s]," %(rest_coord[0], rest_coord[1])
print"destination: [%s, %s]," %(dest_lat, dest_long)
print"travelMode: 'driving',"
print"step: function(e){"
print"$('#instructions').append('<li>'+e.instructions+'</li>');"
print"$('#instructions li:eq('+e.step_number+')').delay(450*e.step_number).fadeIn(200, function(){"
print"map.drawPolyline({"
print"path: e.path,"
print"strokeColor: '#131540',"
print"strokeOpacity: 0.6,"
print"strokeWeight: 6"
print"});"
print"});"
print"}"
print"});"
	
print"map.addMarker({"
print"lat: %s," % source_lat
print"lng: %s," % source_long
print"title: 'Marker with InfoWindow',"
print"infoWindow: {"
print"content: '<p>%s</p>'" % source
print"}"
print"});"

	
print"map.addMarker({"
print"lat: %s," % rest_coord[0]
print"lng: %s," % rest_coord[1]
print"title: 'Marker with InfoWindow',"
print"infoWindow: {"
print"content: '<p>%s</p>'" % rest1
print"}"
print"});"

print"map.addMarker({"
print"lat: %s," % dest_lat
print"lng: %s," % dest_long
print"title: 'Marker with InfoWindow',"
print"infoWindow: {"
print"content: '<p>%s</p>'" % dest
print"}"
print"});"
print"});"

print"</script>"
print"</head>"

print"<body>"
print"<div class=\"row\">"
print"<div class=\"span11\">"
print"<div id=\"map\"></div>"
print"<ul id=\"instructions\">"
print"</ul>"
print"<ul id=\"instructions2\">"
print"</ul>"
print"</div>"
print"</div>"
	
print"<form class='back' action='drivendine.py' method='post'>"
	
print"<input type='submit' class='Search_button' value='New Search'>"
print"</form>"

print"</body>"

print"</html>"
