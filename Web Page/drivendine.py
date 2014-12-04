#!/usr/bin/python

import cgi, Cookie, os

print "Content-type:text/html\r\n\r\n"



print "<html>"
print "<head>"
print "<title>Drive N Dine Application</title>"
print "</head>"

print "<body>"

print 	"<h1 class=\"title\"> Drive N Dine </h1>"

print "<form class='label' action='/cgi-bin/results.py' method='post'> From<br>"

print 	"<input name='from' id=\"from\" class=\"inputs1\" type=\"text\" placeholder=\"918 Iron River Bend, Wanamingo, AZ\"><br>"
print 	"To<br>"
print 	"<input name='to' id=\"to\" class=\"inputs2\" type=\"text\" placeholder=\"795 Umber Pony Abbey, Buck Knob, AZ\"><br> "
	
print 	"<script>"

print 	"function testFunction(){"
print 		"var from = document.getElementById('from').value;"
print 		"var to = document.getElementById('to').value;"
print 		"var trip = 'Going from ' + from + ' to ' + to + '.';"

		
print 		"return trip;"
print 	"}"

print 	"</script>"

print 	"<input type='submit' class=\"GO_button\" value='GO!'>"

print "</form>"
		
print 	"<p id=\"output\" class=\"label\"></p>"


print "</body>"

print "<style>"

print "<style> "


print "@font-face {"
print "font-family: Turtles;"
print "src: url(Turtles.woff);"
print "}"

print ".options{"
print 	"color: white;"
print 	"text-align: center;"
print "}"

print ".black_overlay{"
print 	"display: none;"
print 	"position: absolute;"
print 	"top: 0%;"
print 	"left: 0%;"
print 	"width: 100%;"
print 	"height: 100%;"
print 	"background-color: black;"
print 	"z-index:1001;"
print 	"-moz-opacity: 0.8;"
print 	"opacity:.80;"
print 	"filter: alpha(opacity=80);"
print "}"
print ".white_content {"
print 	"display: none;"
print 	"position: absolute;"
print 	"top: 25%;"
print 	"left: 25%;"
print 	"width: 50%;"
print 	"height: 50%;"
print 	"padding: 16px;"
print 	"border: 4px solid yellow;"
print 	"background-color: white;"
print 	"z-index:1002;"
print 	"overflow: auto;"
print "}"

print "body {"
print     "background-image: url(\"../Road.jpg\");"
print     "background-color: #000000;"
print 	"color: white;"
print "}"


print "inputs:-webkit-input-placeholder {"
print     "color: #b5b5b5;"
print "}"

print "inputs-moz-placeholder {"
print     "color: #b5b5b5;"
print "}"

print ".inputs1 {"
print     "background: #f5f5f5;"
print     "font-size: 0.8rem;"
print     "-moz-border-radius: 3px;"
print     "-webkit-border-radius: 3px;"
print     "border-radius: 3px;"
print     "border: none;"
print     "padding: 13px 10px;"
print     "width: 270px;"
print     "margin-bottom: 30px;"
print     "box-shadow: inset 0 2px 3px rgba( 0, 0, 0, 0.1 );"
print     "clear: both;"
print 	"width: 70%;"
print 	"margin-bottom: 10%;"
	
print 	"text-align: right;"
print "}"

print ".inputs2 {"
print     "background: #f5f5f5;"
print     "font-size: 0.8rem;"
print     "-moz-border-radius: 3px;"
print     "-webkit-border-radius: 3px;"
print     "border-radius: 3px;"
print     "border: none;"
print     "padding: 13px 10px;"
print     "width: 270px;"
print     "margin-bottom: 20px;"
print     "box-shadow: inset 0 2px 3px rgba( 0, 0, 0, 0.1 );"
print     "clear: both;"
print 	"width: 70%;"
#print 	"margin-left: 15%;"
	
print 	"text-align: right;"
print "}"

print ".inputs:focus {"
print     "background: #fff;"
print     "box-shadow: 0 0 0 3px #fff38e, inset 0 2px 3px rgba( 0, 0, 0, 0.2 ), 0px 5px 5px rgba( 0, 0, 0, 0.15 );"
print     "outline: none;"
print "}"

print ".textbox {"
print     "height: 25px;"
print     "width: 70%;"
print     "border: solid 1px #E5E5E5;"
print     "outline: 0;"
print 	"margin-left: 15%;"
print 	"margin-bottom: 8%;"
print 	"text-align: right;"
print     "font: normal 18px/100% Verdana, Tahoma, sans-serif;"
print     "background: #FFFFFF url('bg_form.png') left top repeat-x;"
print     "background: -webkit-gradient(linear, left top, left 25, from(#FFFFFF), color-stop(4%, #EEEEEE), to(#FFFFFF));"
print     "background: -moz-linear-gradient(top, #FFFFFF, #EEEEEE 1px, #FFFFFF 25px);"
print     "box-shadow: rgba(0, 0, 0, 0.1) 0 0 8px;"
print     "-moz-box-shadow: rgba(0, 0, 0, 0.1) 0 0 8px;"
print     "-webkit-box-shadow: rgba(0, 0, 0, 0.1) 0 0 8px;"
print "}"

print ".textbox:focus {"
print     "border-color: #C9C9C9;"
print     "-webkit-box-shadow: rgba(0, 0, 0, 0.15) 0 0 8px;"
print "}"

print ".label {"
print 	"font-family: 'Turtles';"
print 	"font-size: 42px;"
print 	"text-align: center;"
print 	"color: #FFFF00;"
print 	"text-shadow: 5px 5px 5px #000000;"
print 	"margin-bottom: 5px;"


print "}"

print ".options {"
print 	"font-family: 'Turtles';"
print 	"font-size: 42px;"
print "color: #FFFF00;"
print 	"text-shadow: 2px 2px 2px #000000;"
print 	"margin-bottom: 5%;"
print "}"


print ".title {"
print 	"font-family: 'Turtles';"
print 	"font-size: 72px;"
print 	"text-align: center;"
print 	"margin-bottom: 25px;"
print 	"color: #FFFF00;"
print 	"text-shadow: 2px 2px 2px #000000;"

print "}"

print ".GO_button{"
print  "border:1px solid #000000;-webkit-box-shadow: #B7B8B8 0px 1px 0px inset;-moz-box-shadow: #B7B8B8 0px 1px 0px inset; box-shadow: #B7B8B8 0px 1px 0px inset; -webkit-border-radius: 3px; -moz-border-radius: 3px;border-radius: 3px;font-size:12px;font-family:arial, helvetica, sans-serif; padding: 10px 10px 10px 10px; text-decoration:none; display:inline-block;text-shadow: -1px -1px 0 rgba(0,0,0,0.3);font-weight:bold; color: #000000;"
print  "background-color: #FFFFCC; background-image: -webkit-gradient(linear, left top, left bottom, from(#a5b8da), to(#FFFF00));"
print  "background-image: -webkit-linear-gradient(top, #FFFFCC, #FFFF00);"
print  "background-image: -moz-linear-gradient(top, #FFFFCC, #FFFF00);"
print  "background-image: -ms-linear-gradient(top, #FFFFCC, #FFFF00);"
print  "background-image: -o-linear-gradient(top, #FFFFCC, #FFFF00);"
print  "background-image: linear-gradient(to bottom, #FFFFCC, #FFFF00);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#FFFFCC, endColorstr=#FFFF00);"

#print  "margin-left: 45%;"
print  "width: 10%;"
print  "text-align: center;"
print  "margin-top: 100px;"
print "}"

print ".GO_button:hover{"
print  "border:1px solid #000000;"
print  "background-color: #F2F280; background-image: -webkit-gradient(linear, left top, left bottom, from(#F2F280), to(##E6E600));"
print  "background-image: -webkit-linear-gradient(top, ##F2F280, ##E6E600);"
print  "background-image: -moz-linear-gradient(top, #F2F280, ##E6E600);"
print  "background-image: -ms-linear-gradient(top, #F2F280, ##E6E600);"
print "background-image: -o-linear-gradient(top, #F2F280, ##E6E600);"
print "background-image: linear-gradient(to bottom, #F2F280, ##E6E600);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr=#F2F280, endColorstr=##E6E600);"
print "}"


print "</style>"


print "</html>"