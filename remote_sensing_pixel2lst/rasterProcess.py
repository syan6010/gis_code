import arcpy
from arcpy.sa import *

arcpy.env.workspace = r"D:\onedrive\學校課件\110下\遙感探測\作業4\test2\data"
file_name = "LC08_L1TP_117044_20210321_20210401_02_T1_B{}.TIF"
# file_name = "LC08_L2SP_117043_20210321_20210401_02_T1_{}_B{}.TIF"
#band名稱轉換
def b(code):
    # if code < 8 and code >0:
    return file_name.format(code)
    # elif(code == 10):
    #     return file_name.format("ST", code)
    # else:
        # print("error")

# 合並所有的band（range的延展性還是死的）
arcpy.CompositeBands_management("{};{};{};{};{};{};{};{}".format(b(1), b(2), b(3), b(4),b(5), b(6), b(7), b(10)),"compbands.tif")
print("finish1")

# 產出LST
try:
    RasterCalculator([b(10)], ["band10"] ,"0.0003342 * band10 + 0.1 -0.29").save("TOA.TIF")
    RasterCalculator(["TOA.TIF"], ["TOA"] ,"(1321.0789 / Ln((774.8853 / TOA ) + 1 )) - 273.15").save("BT.TIF")
    RasterCalculator([b(4), b(5)], ["band4", "band5"] ," Float(band5 - band4) / Float(band5 + band4)").save("NVDI.TIF")
    NVDI = arcpy.Raster ("NVDI.TIF")
    if(NVDI.minimum < 0):
        PV_EXPRESSION = "Square((NVDI + {}) / ({} + {}))".format(-NVDI.minimum, NVDI.maximum, -NVDI.minimum)
    else:
        PV_EXPRESSION = "Square((NVDI - {}) / ({} - {}))".format(-NVDI.minimum, NVDI.maximum, -NVDI.minimum)
        
    print(PV_EXPRESSION)
    RasterCalculator(["NVDI.TIF"], ["NVDI"] , PV_EXPRESSION).save("PV.TIF")
    RasterCalculator(["PV.TIF"], ["PV"] ,"0.004 * PV + 0.986").save("E.TIF")
    # lst是地表溫度，非空氣溫度
    RasterCalculator(["BT.TIF", "E.TIF"], ["BT", "E"] ,"BT / (1 + ((10.895 * BT / 14388) *  Ln(E)))").save("LST.TIF")
    print('finish2')
except ValueError as msg:   
    print(msg)
