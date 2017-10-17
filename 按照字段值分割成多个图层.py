#coding=utf-8
from arcpy import env
import time
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')

InputFeature = arcpy.GetParameterAsText(0)
field = arcpy.GetParameterAsText(1)
SavePath = arcpy.GetParameterAsText(2)

env.workspace = SavePath

print '程序开始：' + str(time.ctime())
values = [row[0] for row in arcpy.da.SearchCursor(InputFeature, (field))]
fieldArr = set(values)
for value in fieldArr:
    os.makedirs(SavePath+"\\"+value)
    arcpy.Select_analysis (InputFeature, SavePath+"\\"+value+"\\"+value+".shp", '"'+field+'" = \''+value+'\'')
print '程序结束：' + str(time.ctime())

