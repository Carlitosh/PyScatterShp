 #!/usr/bin/env python
# -*- coding: utf-8

from osgeo import ogr
import numpy as np

def atrib(mps):
	dataSource = ogr.Open(mps)
	daLayer = dataSource.GetLayer(0)
	layerDefinition = daLayer.GetLayerDefn()
	count_item = np.arange(0,len(daLayer))
	Atributos = []
	a = np.arange(0,len(daLayer))
	for i in range(layerDefinition.GetFieldCount()):
		at = layerDefinition.GetFieldDefn(i).GetName()
		Atributos.append(at)
	atrib = []
	for i in Atributos:
		atrib.append(i)
	return atrib	

def read_shp(mps,x,y):
	shapefile = ogr.Open(mps)
	layer = shapefile.GetLayer()
	a = np.arange(0,len(layer))
	X=[]
	Y = []
	try:
		for i in a:
			feature = layer.GetFeature(i)
			x1 = feature.GetField(x)
			y1 = feature.GetField(y)
			X.append(x1)
			Y.append(y1)
			
		x2 = np.asarray([float(i) for i in X])
		y2 = np.asarray([float(i) for i in Y])
			
		
		return x2,y2
		
	except:
		print "Error a nivel de obtencion de atributos"	

		
