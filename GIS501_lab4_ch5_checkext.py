#GIS 501 Lab 4 CH 5 Problem 4
import arcpy
from arcpy import env
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise05/Exercise05"
list_ext = ["3D", "Network", "Spatial"]
print "The following extensions are available:"
for extension in list_ext:	
	if arcpy.CheckExtension(extension) == "Available":
		print "ArcGIS" + " " + extension + " " + "Analyst"
