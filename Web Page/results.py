print "<html>"
print "<head class='map_canvas'>"
print "<title></title>"
#print "<script src='http://maps.google.com/maps/api/js?sensor=true'></script>"
#print "<script src='/gmaps-master/gmaps.js'></script>"

print "<style type='text/css'>"

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
print "}"

print "#results {"

print "height: 300px;"
print "width: 96%;"
print "margin-left: 2%;"
print "background-color: white;"
print "color: black;"
print "overflow: auto;"
print "font-size: 120%;"
print "}"

print "body {"
print "background-image: url('asphault_plain.jpg');"
print "background-color: #cccccc;"
print "color: white;"
print "}"


print "</style>"

print "</head>"
print "<body>"
print "<div id='map'></div>"

"""print "<script>"

print "var map = new GMaps({"
print "el: '#map',"
print "lat: -12.043333,"
print "lng: -77.028333"
print "});"
print "map.addMarker({"
print "lat: -12.043333,"
print "lng: -77.03,"
print "title: 'Lima',"
print "details: {"
print "database_id: 42,"
print "author: 'HPNeo'"
print "},"
print "click: function(e){"
print "if(console.log)"
print "console.log(e);"
print "alert('You clicked in this marker');"
print "},"
print "mouseover: function(e){"
print "if(console.log)"
print "console.log(e);"
print "}"
print "});"
print "map.addMarker({"
print "lat: -12.042,"
print "lng: -77.028333,"
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>HTML Content</p>'"
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
print "map.addMarker({"
print "lat: -12.044012922866312,"
print "lng: -77.02470665341184,"
print "title: 'Marker with InfoWindow',"
print "infoWindow: {"
print "content: '<p>HTML Content</p>'"
print "}"
print "});"

print "</script>"
"""

print "<script>"
print "function myFunction() {"
print "document.getElementById('results').style.outline = 'thick solid #000000';"
print "}"
print "</script>"

print "<div id='results'>"

print "<table style='width:96%;'>"
print "<tr>"
print "<td>Jill</td>"
print "<td>Smith</td> "
print "<td>50</td>"
print "</tr>"
print "<tr>"
print "<td>Eve</td>"
print "<td>Jackson</td>"
print "<td>94</td>"
print "</tr>"
print "</table>"

print "</div>"
print "</body>"

print "</html>"