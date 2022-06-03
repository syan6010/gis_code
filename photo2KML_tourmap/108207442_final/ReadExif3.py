# -*- coding: big5
# 若程式中有使用中文，必須指明使用BIG5碼，前述的字碼定義必須在程式的第一或第二行
# 字碼定義的方式可參考：http://www.python.org/dev/peps/pep-0263/
# Python支援的字碼： http://www.python.org/doc/2.4/lib/standard-encodings.html

""" 此程式示作為檢查航照影像是否涵蓋機敏區的程式之GUI介面 """

import os, sys, time
import wx
import exifread
import datetime as dt
from PIL import Image
import shutil


import glob
#import datetime
#import numpy as np
#from skimage import io
#from skimage.transform import resize

# some global variables
inDir = ""
currDir = os.getcwd()
outFile = ""
kmlFile = ""

imgWidthId = 256
imgLengthId = 257
pixelDix = 40962
pixelDiy = 40963
imgTimeId = 306
orientationId = 274
gpsTagId = 34853



# KML header, trailer, and template for placemark
kml_header = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2"  xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom ">
<Folder>
'''
place_mark = '''<Placemark>  
  <name>{}</name>  
  <description>{} 
    <p><img alt="" src="reImg/re_{}" width="{}" height="{}" /></p> 
    <p><a href="http://www.nccu.edu.tw/">http://www.nccu.edu.tw/</a></p>  
  </description> 
  <Point>  
    <coordinates>{},{},0</coordinates>  
  </Point>  
</Placemark>  
'''
kml_trailer = '''</Folder>
</kml>
'''

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        #建造一個新的 Frame
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title="EXIF Reader", size=(540,550),
                style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)

        #logo_path = resource_path("nccu_logo.bmp")
        #self.window.iconbitmap(image_path)
        ico_img = Image.open('nccu_logo.bmp')
        ico_img.save('ico_nccu.ico',format = 'ICO', sizes=[(32,32)])
        ico = wx.Icon("ico_nccu.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
                
        # 加入一個 Panel
        panel = wx.Panel(self, wx.ID_ANY)
        
        wx.StaticText(parent=panel, label="輸入資料夾:", pos=(15,10))
        self.a = wx.TextCtrl(parent=panel,pos=(140,10),size=(325,20))
        self.btn1 = wx.Button(parent=panel,label="...",pos=(480,10),size=(40,20))
        self.Bind(wx.EVT_BUTTON, self.OnBtn1, self.btn1)

        wx.StaticText(parent=panel, label="輸出資料檔:", pos=(15,40))
        self.b = wx.TextCtrl(parent=panel,pos=(140,40),size=(325,20))
        self.btn2 = wx.Button(parent=panel,label="...",pos=(480,40),size=(40,20))
        self.Bind(wx.EVT_BUTTON, self.OnBtn2, self.btn2)

        self.btn3 = wx.Button(parent=panel,label=" 清除訊息 ",pos=(15,70),size=(100,20))
        self.Bind(wx.EVT_BUTTON, self.OnBtn3, self.btn3)

        self.btn4 = wx.Button(parent=panel,label=" 確定 ",pos=(460,70),size=(60,20))
        self.Bind(wx.EVT_BUTTON, self.OnBtn4, self.btn4)

        self.txtCtrl = wx.TextCtrl(panel, id=wx.ID_ANY, style=wx.TE_MULTILINE, pos=(10,110), size=(510,390))

        #self.readConfigFile()
#            self.writeConfigFile()

    def OnBtn1(self, evt):
        global inDir
        # In this case we include a "New directory" button. 
        dlg = wx.DirDialog(
            self, message="選擇輸入資料夾:",
            style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST
            )
                     
        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPath()
            self.a.SetValue(path)
            inDir = self.a.GetValue()
            inDir = inDir.replace('\\', '/')
            
        # Only destroy a dialog after you're done with it.
        dlg.Destroy()

    def OnBtn2(self, evt):
        global outFile
        
        # Choose the output file. 
        dlg = wx.FileDialog(
            self, message="選擇輸出資料檔:",
            defaultDir=currDir, 
            defaultFile="",
            wildcard="*.csv",
            style= wx.FD_OVERWRITE_PROMPT | wx.FD_SAVE
            )
                     
        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPath()
            self.b.SetValue(path)
            outFile = self.b.GetValue()
            outFile = outFile.replace('\\', '/')
            
        # Only destroy a dialog after you're done with it.
        dlg.Destroy()

    def OnBtn3(self, evt):
        
        self.txtCtrl.Clear()

    def OnBtn4(self, evt):
        
        try:
            self.txtCtrl.WriteText('輸入資料夾： %s\n' % inDir)
            self.read_exif()
            
            self.txtCtrl.WriteText('輸出檔案： %s, %s\n' % (outFile, kmlFile))
            self.txtCtrl.WriteText('成功!\n')
        except:
            print('失敗!')
        
    def read_exif(self):
        global kmlFile, outFile
        
        kmlFile = outFile[:-3] + 'kml'
            
        img_list = glob.glob("%s/*.jpg" % inDir)
        
        num_img = len(img_list)
        
        if num_img == 0:
            self.txtCtrl.WriteText('找不到 JPG 影像檔!\n')
            return
        
        fout = open(outFile, 'w')
        header = '檔案名稱,拍攝時間,經度,緯度\n'
        fout.write(header)
        
        kml_out = open(kmlFile, 'w')
        kml_out.write(kml_header)
        

        if os.path.exists('reImg'):
            print("檔案存在。")
            shutil.rmtree('reImg')
            os.makedirs('reImg')           
        else:
            print("檔案不存在。")
            os.makedirs('reImg')


        for i in range(num_img):
            basename = os.path.basename(img_list[i])
            print(basename)

            path_name = 'images/{}'.format(basename)
            exif = get_exif(path_name)


            try:
                imgTime = exif[imgTimeId]     
                print("have time") 
            except:
                imgTime = dt.datetime.fromtimestamp(os.path.getmtime(path_name)).strftime('%Y:%m:%d %H:%M:%S')
                print("dont have time") 
             


            orientation = exif[orientationId]

            try:
              width = exif[imgWidthId]
              height = exif[imgLengthId]
              print('key 2')          
            except:
              width = exif[pixelDix]
              height = exif[pixelDiy]
              print('key 1')

            print("{}, {}".format(width, height))


            new_w = int(width / 10)
            new_h = int(height / 10)


            img = Image.open(path_name)
            width, height = img.size
            rsize_img = img.resize((new_w, new_h))

            if(orientation == 6):
                ori_img = rsize_img.transpose(Image.ROTATE_270)
                ori_img.save('reImg/re_{}'.format(basename), 'JPEG')
                new_h , new_w = new_w, new_h
                print('90')
            elif(orientation == 8):
                ori_img = rsize_img.transpose(Image.ROTATE_90)
                ori_img.save('reImg/re_{}'.format(basename), 'JPEG')
                new_h , new_w = new_w, new_h
                print('270')
            elif(orientation == 2):
                ori_img = rsize_img.transpose(Image.FLIP_LEFT_RIGHT)
                ori_img.save('reImg/re_{}'.format(basename), 'JPEG')
                print('180')
            elif(orientation == 4):
                ori_img = rsize_img.transpose(Image.FLIP_TOP_BOTTOM)
                ori_img.save('reImg/re_{}'.format(basename), 'JPEG')
                print('180')
            elif(orientation == 5):
                ori_img = rsize_img.transpose(Image.FLIP_LEFT_RIGHT)
                ori_img_f = rsize_img.transpose(Image.ROTATE_90)
                ori_img_f.save('reImg/re_{}'.format(basename), 'JPEG')
                print('180')
            elif(orientation == 7):
                ori_img = rsize_img.transpose(Image.FLIP_LEFT_RIGHT)
                ori_img_f = rsize_img.transpose(Image.ROTATE_270)
                ori_img_f.save('reImg/re_{}'.format(basename), 'JPEG')
                print('180')
            elif(orientation == 3):
                ori_img = rsize_img.transpose(Image.ROTATE_180)
                ori_img.save('reImg/re_{}'.format(basename), 'JPEG')
                print('180')
            
            else:
                rsize_img.save('reImg/re_{}'.format(basename), 'JPEG')
                print('else')
            
            
            try:
                gpsInfo = exif[gpsTagId]
                lat_str = gpsInfo[2]
                lat = format_lat_lon(lat_str)
                lon_str = gpsInfo[4]
                lon = format_lat_lon(lon_str)   
                print("{}, {}".format(lat, lon)) 
                data = '{},{},{},{}\n'.format(basename, imgTime, lon, lat)
                kml_out.write(place_mark.format(basename,basename,basename,new_w,new_h,lon,lat))
                for k in sorted(exif.keys()):
                   print('{}: {}'.format(k, exif[k]))
            except:
                print("enter")
                self.txtCtrl.WriteText('%s has no GPS info\n' % basename)
                data = '{},{}\n'.format(basename, imgTime)
                
            self.txtCtrl.WriteText(data)
            
            fout.write(data)
            
        fout.close()
        kml_out.write(kml_trailer)
        kml_out.close()

#---------------------------------------------------------------------------
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def format_lat_lon(data):
    dd = float(data[0])
    mm = float(data[1]) / 60
    ss = float(data[2]) / 3600
    
    result = dd + mm + ss
    return result

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
#---------------------------------------------------------------------------

# Every wxWidgets application must have a class derived from wx.App
class MyApp(wx.App):

    # wxWindows calls this method to initialize the application
    def OnInit(self):

        # Create an instance of our customized Frame class
        frame = MyFrame(None, -1, "Create Worldfile")
        frame.Show(True)

        # Tell wxWindows that this is our main window
        self.SetTopWindow(frame)

        # Return a success flag
        return True
        
#---------------------------------------------------------------------------
    
if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
