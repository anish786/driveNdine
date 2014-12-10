#!/usr/local/bin/python

import cgi, Cookie, os, subprocess

form = cgi.FieldStorage()
source = form.getvalue('from')
dest = form.getvalue('to')

execfile('../p2.py')
execfile('../p3.py')

src_coord = addressToCoordinates(source)
dest_coord = addressToCoordinates(dest)

recommended = run(source, dest)

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
	
print ".hidden {"
print "display: none;"
print "}"

print "body {"
print "background-image: url(\"../Road.jpg\");"
print "background-color: #cccccc;"
print "}"
	
print ".textStuff {"
print "width: 48%;"
print "display: inline-block;"
print "}"
	
print ".submit_button {"
print "border:1px solid #707070;-webkit-box-shadow: #B7B8B8 0px 1px 0px inset;-moz-box-shadow: #B7B8B8 0px 1px 0px inset; box-shadow: #B7B8B8 0px 1px 0px inset; -webkit-border-radius: 3px; -moz-border-radius: 3px;border-radius: 3px;font-size:12px;font-family:arial, helvetica, sans-serif; padding: 10px 10px 10px 10px; text-decoration:none; display:inline-block;text-shadow: -1px -1px 0 rgba(0,0,0,0.3);font-weight:bold; color: #000000;"
print "background-color: #707070; background-image: -webkit-gradient(linear, left top, left bottom, from(#a5b8da), to(#333333));"
print "background-image: -webkit-linear-gradient(top, #707070, #333333);"
print "background-image: -moz-linear-gradient(top, #707070, #333333);"
print "background-image: -ms-linear-gradient(top, #707070, #333333);"
print "background-image: -o-linear-gradient(top, #707070, #333333);"
print "background-image: linear-gradient(to bottom, #707070, #333333);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#707070, endColorstr=#333333);"
print "width: 20%;"
print "height: 35px;"
print "color: #FFFF00;"
print "}"

print ".buttons{"
print "display: inline-block;"
print "width: 48%;"
print "height: 20px;"
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
print "lat: %s," %str(src_coord[0])
print "lng: %s" %str(src_coord[1])
print "});"
	
print "map.addMarker({"
print "lat: %s," %str(src_coord[0])  
print "lng: %s," %str(src_coord[1])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>Source</p>'"
print "}"
print "});"
		
print "map.addMarker({"
print "lat: %s," % str(dest_coord[0])
print "lng: %s," %str(dest_coord[1])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>Destination</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[0][0]['latitude'])
print "lng: %s," % str(recommended[0][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#1</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[1][0]['latitude'])
print "lng: %s," % str(recommended[1][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#2</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[2][0]['latitude'])
print "lng: %s," % str(recommended[2][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#3</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[3][0]['latitude'])
print "lng: %s," % str(recommended[3][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#4</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[4][0]['latitude'])
print "lng: %s," % str(recommended[4][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#5</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[5][0]['latitude'])
print "lng: %s," % str(recommended[5][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#6</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[6][0]['latitude'])
print "lng: %s," % str(recommended[6][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#7</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[7][0]['latitude'])
print "lng: %s," % str(recommended[7][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#8</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[8][0]['latitude'])
print "lng: %s," % str(recommended[8][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#9</p>'"
print "}"
print "});"

print "map.addMarker({"
print "lat: %s," % str(recommended[9][0]['latitude'])
print "lng: %s," % str(recommended[9][0]['longitude'])
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>#10</p>'"
print "}"
print "});"

print "map.drawRoute({"
print "origin: [%s, %s]," % (str(src_coord[0]), str(src_coord[1]))
print "destination: [%s, %s]," % (str(dest_coord[0]), str(dest_coord[1]))
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

print "<div class='textStuff'>"
print "<p id='results1'> This path goes from %s to %s </p>" % (source, dest)
print "<p id='results2'> 1. %s </p>" %recommended[0][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[0][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[0][0]['full_address']

print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[0][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[0][0]['stars'])


print "<p id='results2'> 2.  %s </p>" %recommended[1][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[1][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[1][0]['full_address']

print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[1][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[1][0]['stars'])
	
print "<p id='results2'> 3. %s </p>" %recommended[2][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[2][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[2][0]['full_address']

print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[2][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[2][0]['stars'])
	
print "<p id='results2'> 4. %s </p>" %recommended[3][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[3][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[3][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[3][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[3][0]['stars'])
	
print "<p id='results2'> 5. %s </p>" %recommended[4][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[4][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[4][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[4][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[4][0]['stars'])
	
print "<p id='results2'> 6. %s </p>" %recommended[5][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[5][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[5][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[5][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[5][0]['stars'])
	
print "<p id='results2'> 7 %s </p>" %recommended[6][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[6][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[6][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[6][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[6][0]['stars'])
	
print "<p id='results2'> 8. %s </p>" %recommended[7][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[7][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[7][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[7][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[7][0]['stars'])

print "<p id='results2'> 9. %s </p>" %recommended[8][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[8][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[8][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[8][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[8][0]['stars'])

print "<p id='results2'> 10. %s </p>" %recommended[9][0]['name'] 
print "</div>"
print "<div class='buttons'>"
print "<form action='/cgi-bin/third.py' method='post'> "
print "<input name='sourceAddress' class='hidden' type='text' value='%s'>" % source
print "<input name='destAddress' class='hidden' type='text' value='%s'>" % dest
print "<input name='rest1' class='hidden' type='text' value='%s'>" % recommended[9][0]['name']
print "<input name='sourceLat' class='hidden' type='text' value='%s'>" % (str(src_coord[0]))
print "<input name='sourceLong' class='hidden' type='text' value='%s'>" % (str(src_coord[1]))
print "<input name='destLat' class='hidden' type='text' value='%s'>" % (str(dest_coord[0]))
print "<input name='destLong' class='hidden' type='text' value='%s'>" % (str(dest_coord[1]))
print "<input name='restAddress' class='hidden' type='text' value='%s'>" % recommended[9][0]['full_address']


print "<input class='submit_button' type='submit' value='Eat Here!'>"
print "</form>"
print "</div>"
print "<div class='textStuff'>"
print "<p id='results2'> %s </p>" % recommended[9][0]['full_address']
print "<p id='results3'> Yelp Rating: %s/5.0 .</p>"  % str(recommended[9][0]['stars'])

print "</div>"

print "</div>"
print "<form class='back' action='/cgi-bin/third.py' method='post'>"
	
print "<input type='submit' class='Search_button' value='New Search'>"
		
print "</form>"
	
print "</body>"

print "</html>"
