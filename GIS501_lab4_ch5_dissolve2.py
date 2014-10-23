#GIS 501 Lab 4 Ch 5 Problem 3
import arcpy
from arcpy import env
#set workspace to directory
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise05/Exercise05"
#multipart features are not allowed
arcpy.management.Dissolve("parks.shp", "Results/parks_dissolved.shp", "PARK_TYPE", "", "SINGLE_PART","")
