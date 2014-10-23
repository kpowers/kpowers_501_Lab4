#GIS 501 Lab 4 CH 7 Problem 2 

import arcpy
from arcpy import env
#env.overwriteOutput = True
env.workspace = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise07/Exercise07"
#define input file
fc = "C:/Users/Kelsey/Documents/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_4/exercise07/Exercise07/roads.shp"
newfield = "FERRY"
field_type = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.management.AddField(fc, newfield, field_type)
# cursor = arcpy.da.UpdateCursor(fc, ["FERRY"])
# for row in cursor:
# 	if "FEATURE" == "Ferry Crossing":
# 		row[0] = 'YES'
#         cursor.updateRow(row)
# 	else:
# 		row[0] = 'NO'
# 		cursor.updateRow(row)
# del row
# del cursor
