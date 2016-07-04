from django.shortcuts import render_to_response,RequestContext,HttpResponseRedirect
import os  # for finding the working directory
import subprocess
from osgeo import gdal,osr
from PIL import Image
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np
import tkinter

def index(request):
	return render_to_response("index.html",{})


def landset7(request):
	return render_to_response("landset7.html",{})


def landset8(request):
	return render_to_response("landset8.html",{})

def ndvi_7(request):
	output=""
	loc=""
	if request.method=="POST":
		ndvi71=request.FILES.get("ndvi71")
		ndvi72=request.FILES.get("ndvi72")
		ndvi_7e(ndvi71,ndvi72)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS7ndvi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS7ndvi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndvi_7.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

def ndwi_7(request):
	output=""
	loc=""
	if request.method=="POST":
		ndwi71=request.FILES.get("ndwi71")
		ndwi72=request.FILES.get("ndwi72")
		ndwi_7e(ndwi71,ndwi72)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS7ndwi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS7ndwi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndwi_7.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

def ndbi_7(request):
	output=""
	loc=""
	if request.method=="POST":
		ndbi71=request.FILES.get("ndbi71")
		ndbi72=request.FILES.get("ndbi72")
		ndbi_7e(ndbi71,ndbi72)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS7ndbi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS7ndbi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndbi_7.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

def ndvi_8(request):
	output=""
	loc=""
	if request.method=="POST":
		ndvi81=request.FILES.get("ndvi81")
		ndvi82=request.FILES.get("ndvi82")
		ndvi_8e(ndvi81,ndvi82)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS8ndvi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS8ndvi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndvi_8.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

def ndwi_8(request):
	output=""
	loc=""
	if request.method=="POST":
		ndwi81=request.FILES.get("ndwi81")
		ndwi82=request.FILES.get("ndwi82")
		ndwi_8e(ndwi81,ndwi82)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS8ndwi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS8ndwi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndwi_8.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

def ndbi_8(request):
	output=""
	loc=""
	if request.method=="POST":
		ndbi81=request.FILES.get("ndbi81")
		ndbi82=request.FILES.get("ndbi82")
		ndbi_8e(ndbi81,ndbi82)
		output="done"
		loc="image saved at C:/Users/Abhishek/Desktop/ENV/GUI/static/LS8ndbi.tif "
		path_to_notepad = 'C:\\Program Files (x86)\\Safari\\Safari.exe'
		path_to_file = 'C:\\Users\\Abhishek\\Desktop\\ENV\\GUI\\static\\LS8ndbi.tif'
		subprocess.call([path_to_notepad, path_to_file])
	return render_to_response("ndbi_8.html",{"output":output,"loc":loc},context_instance=RequestContext(request))

#functions

def ndvi_7e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()
	print (os.path.abspath(file1.name))

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4=dataSource.GetRasterBand(1)
	band4Arr=band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5=dataSource2.GetRasterBand(1)
	band5Arr=band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS7ndvi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()
	
def ndwi_7e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4=dataSource.GetRasterBand(1)
	band4Arr=band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5=dataSource2.GetRasterBand(1)
	band5Arr=band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS7ndwi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()


def ndbi_7e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4 = dataSource.GetRasterBand(1)
	band4Arr = band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5 = dataSource2.GetRasterBand(1)
	band5Arr = band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS7ndbi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()

def ndvi_8e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4 = dataSource.GetRasterBand(1)
	band4Arr = band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5 = dataSource2.GetRasterBand(1)
	band5Arr = band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS8ndvi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()

def ndwi_8e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4 = dataSource.GetRasterBand(1)
	band4Arr = band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5 = dataSource2.GetRasterBand(1)
	band5Arr = band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS8ndwi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()

def ndbi_8e(file1,file2):
	print ("the GDAL version")
	print(gdal.__version__)
	gdal.AllRegister()

	## Check working directory
	print ("Working directory:",  os.getcwd())

	## Opening Erdas Imagine Images (*.tif)
	driver = gdal.GetDriverByName('GTiff')

	filename = os.path.abspath(file1.name)
	filename2 = os.path.abspath(file2.name)

	dataSource = gdal.Open(filename, GA_ReadOnly)
	dataSource2 = gdal.Open(filename2,  GA_ReadOnly)

	## Transform bands into arrays
	band4 = dataSource.GetRasterBand(1)
	band4Arr = band4.ReadAsArray(0,0,dataSource.RasterXSize, dataSource.RasterYSize)

	band5 = dataSource2.GetRasterBand(1)
	band5Arr = band5.ReadAsArray(0,0,dataSource2.RasterXSize, dataSource2.RasterYSize)

	## Change data type
	band4Arr=band4Arr.astype(np.float32)
	band5Arr=band5Arr.astype(np.float32)

	## Create mask to select non-zero value
	mask = np.greater(band4Arr+band5Arr,  0) 
	ndwi = np.choose(mask,(-99, (band4Arr-band5Arr)/(band4Arr+band5Arr)))
	check = np.logical_or ( band4Arr > 0, band5Arr > 0 )
	ndwi = np.where ( check,  (band4Arr-band5Arr ) / ( band4Arr+band5Arr ) * 100, -999 )
	# For some reason still returns a divide by zero warning!
	print ("NDWI min and max values", ndwi[ndwi>-99].min(), ndwi.max())

	## Output an image
	outDataSet=driver.Create('static/LS8ndbi.tif', dataSource.RasterXSize, dataSource.RasterYSize, 1, GDT_Float32)
	outBand = outDataSet.GetRasterBand(1)
	outBand.WriteArray(ndwi,0,0)
	outBand.SetNoDataValue(-99)

	## Set projection to input source projection
	outDataSet.SetProjection(dataSource.GetProjection())

	## Save and clean memory
	outBand.FlushCache()
	outDataSet.FlushCache()

