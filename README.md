driveNdine
==========

CSCE 470 Project


For our CSCE 470 Project, we decided to tackle the yelp dataset challenge.
We took the business.json file and extracted all the restaurants from the
file and made it into a new json file that we use to get restaurant data
from. 

Our application takes a two places, and gives you the best rated
restaurants that are the closest to your route and then gives you
directions from your source, to the restaurant, and then to your destination.

For our project we used the gmaps API to calculate time traveled as well as
to load maps and directions to restaurants. We used a python class called
Pygeocoder which translates addresses into GPS coordinates which we use to
interact with gmaps API.

In order to use the python code we developed to implement our recommender, 
we used a file type called CGI (Common-Gateway-Interface) to create dynamic
html files that a web browser could read. In order to run these CGI files
we downloaded and configured an Apache2 server to run the CGI files and 
hosted it locally for use. 

In order to run on your own system you would have to download the apache 
server software and configure your server to run CGI files. Also, you would
have to correctly place all the python code and other various files in the 
correct directories with the correct permissions. This information can all
be found online.

For our python we used python 2.7.8. 

If you have any questions feel free to email DriveNDine@gmail.com.