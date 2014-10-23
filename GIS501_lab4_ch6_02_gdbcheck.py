#GIS 501 Lab 4 CH 6 Problem 2
#create file geodatabase NM and 
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise06/Exercise06"
#create file geodatabase in exercise 06 folder
arcpy.management.CreateFileGDB("C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise06/Exercise06/Results", "NM_new.gdb")
#list only polygon feature classes found in Exercise06
fclist = arcpy.ListFeatureClasses(feature_type = 'polygon')
#iterate through polygon feature classes and save to gdb
for fc in fclist:
	fcdesc = arcpy.Describe(fc)
	#Save features into new gbd: NM_new.gdb
	arcpy.management.CopyFeatures(fc, "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise06/Exercise06/Results/NM_new.gdb/" + fcdesc.basename)