#GIS 501 Lab 4 CH 5 Problem 4
import arcpy
from arcpy import env
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise05/Exercise05"
ch_files = arcpy.ListFeatureClasses()
for shape in ch_files:
	file_type = arcpy.Describe(shape)
	print shape + " " + "is a" + " " + file_type.dataType