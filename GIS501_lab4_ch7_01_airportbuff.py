
#GIS 501 Lab 4 CH 7 Problem 1 
import arcpy
from arcpy import env
#env.overwriteOutput = True
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise07/Exercise07"
#input shapefile for both buffers
fc = "airports.shp"
#Select airports from
arcpy.analysis.Select(fc, "Results/temp_airports.shp",  "\"FEATURE\" = 'Airport'")
#Buffer airports to 15000 meters

arcpy.analysis.Buffer("Results/temp_airports.shp", "Results/airport_buffer", "15000 METERS", "FULL","ROUND","")

#Select seaplane bases
arcpy.analysis.Select(fc, "Results/temp_sea.shp", "\"FEATURE\" = 'Seaplane Base'")

#Buffer seaplane bases to 7500m
arcpy.analysis.Buffer("Results/temp_sea.shp", "Results/seaplane_buffer", "7500 METERS", "FULL", "ROUND", "")
