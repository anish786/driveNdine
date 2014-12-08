#!/usr/bin/python

import cgi, Cookie, os, subprocess

form = cgi.FieldStorage()
source = form.getvalue('from')
dest = form.getvalue('to')

execfile("../p3.py")

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head class=\"map_canvas\">"

print "<title>Algorithm Results</title>"
	
print "<script type=\"text/javascript\" src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js\"></script>"
print "<script type=\"text/javascript\" src=\"http://maps.google.com/maps/api/js?sensor=true\"></script>"
print "<script type=\"text/javascript\" src=\"../gmaps-master/gmaps.js\"></script>"

print "<style>"

print ".map_canvas {"

print "height: 350px;"
print "width: 96%;"
print "margin-left: 2%;"
print "margin-top: 1%;"
print "margin-bottom: 20px;"


print "}"

print "#map {"
print "height: 350px;"
print "width: 96%;"
print "margin-left: 2%;"
print "margin-top:1%;"
print "margin-bottom: 20px;"
print "background-color: Black;"
print "}"

print "#results {"
print "height: 250px;"
print "width: 96%;"
print "margin-left: 2%;"
print "background-color: white;"
print "color: black;"
print "overflow: auto;"
print "}"
	
print "#results1 {"
print "margin-top: 10px;"
print "margin-left: 10px;"
print "margin-bottom: 10px;"
print "color: black;"
print "}"
	
print "#results2 {"
print "margin-top: 0px;"
print "margin-left: 40px;"
print "margin-bottom: 0px;"
print "color: black;"
print "}"
	
print "#results3 {"
print "margin-top: 0px;"
print "margin-left: 40px;"
print "margin-bottom: 40px;"
print "color: black;"
print "}"
	
print "body {"
print "background-image: url(\"../Road.jpg\");"
print "background-color: #cccccc;"
print "}"
	
print ".Search_button{"
print "border:1px solid #000000;-webkit-box-shadow: #B7B8B8 0px 1px 0px inset;-moz-box-shadow: #B7B8B8 0px 1px 0px inset; box-shadow: #B7B8B8 0px 1px 0px inset; -webkit-border-radius: 3px; -moz-border-radius: 3px;border-radius: 3px;font-size:12px;font-family:arial, helvetica, sans-serif; padding: 10px 10px 10px 10px; text-decoration:none; display:inline-block;text-shadow: -1px -1px 0 rgba(0,0,0,0.3);font-weight:bold; color: #000000;"
print "background-color: #FFFFCC; background-image: -webkit-gradient(linear, left top, left bottom, from(#a5b8da), to(#FFFF00));"
print "background-image: -webkit-linear-gradient(top, #FFFFCC, #FFFF00);"
print "background-image: -moz-linear-gradient(top, #FFFFCC, #FFFF00);"
print "background-image: -ms-linear-gradient(top, #FFFFCC, #FFFF00);"
print "background-image: -o-linear-gradient(top, #FFFFCC, #FFFF00);"
print "background-image: linear-gradient(to bottom, #FFFFCC, #FFFF00);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#FFFFCC, endColorstr=#FFFF00);"

print "margin-left: 45%;"
print "width: 10%;"
print "text-align: center;"
print "margin-top: 15px;"
print "}"

print ".Search_button:hover{"
print "border:1px solid #000000;"
print "background-color: #F2F280; background-image: -webkit-gradient(linear, left top, left bottom, from(#F2F280), to(##E6E600));"
print "background-image: -webkit-linear-gradient(top, ##F2F280, ##E6E600);"
print "background-image: -moz-linear-gradient(top, #F2F280, ##E6E600);"
print "background-image: -ms-linear-gradient(top, #F2F280, ##E6E600);"
print "background-image: -o-linear-gradient(top, #F2F280, ##E6E600);"
print "background-image: linear-gradient(to bottom, #F2F280, ##E6E600);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#F2F280, endColorstr=##E6E600);"
print "}"
	
print "</style>"
print "<script>"
	
print "var map;"
print "$(document).ready(function(){"
print "map = new GMaps({"
print "el: '#map',"
print "lat: -12.043333,"
print "lng: -77.028333"
print "});"
	
print "map.addMarker({"
print "lat: -12.044012922866312,"
print "lng: -77.02470665341184,"
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>Source</p>'"
print "}"
print "});"
		
print "map.addMarker({"
print "lat: -12.090814532191756,"
print "lng: -77.02271108990476,"
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>Destination</p>'"
print "}"
print "});"
		
		
print "map.drawRoute({"
print "origin: [-12.044012922866312, -77.02470665341184],"
print "destination: [-12.090814532191756, -77.02271108990476],"
print "travelMode: 'driving',"
print "strokeColor: '#131540',"
print "strokeOpacity: 0.6,"
print "strokeWeight: 6"
print "});"
print "});"
		
print "</script>"
	
print "</head>"
	
print "<body>"
	
print "<div id='map'></div>"

print "<div id=\"results\">"

print "<p id='results1'> 1. This path goes from %s to %s </p>" % (source, dest)
print "<p id='results2'> On this line we would put the address of the restaurant. Testing: %s </p>" % (s1)
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 2. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 3. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 4. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 5. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 6. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 7. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 8. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 9. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"
		
print "<p id='results1'> 10. This should be the first ranked restaurant on this line right here. </p>"
print "<p id='results2'> On this line we would put the address of the restaurant </p>"
print "<p id='results2'> On this line we would put the additional time needed to drive here. </p>"
print "<p id='results3'> On this line we would put the yelp rating.</p>"

print "</div>"
	
print "<form class='back' action='/cgi-bin/third.py' method='post'>"
	
print "<input type='submit' class='Search_button' value='New Search'>"
		
print "</form>"
	
print "</body>"

print "</html>"