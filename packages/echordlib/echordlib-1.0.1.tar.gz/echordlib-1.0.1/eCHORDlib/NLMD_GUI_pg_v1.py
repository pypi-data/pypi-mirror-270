# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 11:11:27 2023

@author: clanglois1
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:26:20 2023

@author: clanglois1
"""
import os
import sys

from inspect import getsourcefile
from os.path import abspath

import numpy as np


import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
import tifffile as tf

from LibrairiesCyril import general_functions as gf


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # enable highdpi scaling

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # use highdpi icons

path2thisFile = abspath(getsourcefile(lambda:0))
uiclass, baseclass = pg.Qt.loadUiType(os.path.dirname(path2thisFile) + "/NLMD_v1.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.expStack = parent.image
        self.expStack = np.flip(self.expStack, 1)
        self.expStack = np.rot90(self.expStack, k=1, axes=(2, 1))

        self.denoised_Stack = np.copy(parent.denoisedImage)
        self.denoised_Stack = np.flip(self.denoised_Stack, 1)
        self.denoised_Stack = np.rot90(self.denoised_Stack, k=1, axes=(2, 1))
        
        self.expSeries.ui.histogram.hide()
        self.expSeries.ui.roiBtn.hide()
        self.expSeries.ui.menuBtn.hide()
        self.expSeries.setImage(self.denoised_Stack)  
        self.expSeries.autoRange()

        self.x = 0
        self.y = 0
        
        self.patch_size = 5
        self.patch_distance = 6
        self.param_h = self.slider_h.value() / 10_0.0
        
        self.label_distance.setText("Patch Distance : " + str(self.patch_distance))
        self.label_size.setText("Patch Size : " + str(self.patch_size))
        self.label_h.setText("Parameter h : " + str(self.param_h))
        
        
        if self.denoised.isChecked():
            self.denoised.toggle()
            
        self.denoised.setCheckable(False)

        self.crosshair_v1= pg.InfiniteLine(angle=90, movable=False)
        self.crosshair_h1 = pg.InfiniteLine(angle=0, movable=False)

        self.expSeries.addItem(self.crosshair_v1, ignoreBounds=True)
        self.expSeries.addItem(self.crosshair_h1, ignoreBounds=True) 
        
        self.plotIt = self.profiles.getPlotItem()
        self.plotIt.addLine(x = self.expSeries.currentIndex)
        
        self.proxy1 = pg.SignalProxy(self.expSeries.scene.sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        self.proxy4 = pg.SignalProxy(self.expSeries.ui.graphicsView.scene().sigMouseClicked, rateLimit=60, slot=self.mouseClick)
        
        # self.slider_threshold.sliderReleased.connect(self.radius_changed)
        
        self.slider_size.valueChanged.connect(self.size_changed)
        self.slider_distance.valueChanged.connect(self.distance_changed)
        self.slider_h.valueChanged.connect(self.h_changed)
        
        self.expSeries.timeLine.sigPositionChanged.connect(self.drawCHORDprofiles)
        self.preview.clicked.connect(self.denoiseStack)
        self.denoised.stateChanged.connect(self.drawCHORDprofiles)


    def displayExpStack(self, Series):
        # self.expSeries.clear()
        self.expSeries.ui.histogram.hide()
        self.expSeries.ui.roiBtn.hide()
        self.expSeries.ui.menuBtn.hide()
        
        view = self.expSeries.getView()
        state = view.getState()        
        self.expSeries.setImage(Series) 
        view.setState(state)

    
    def size_changed(self):
        value = self.slider_size.value()
        print("size changed : ", value, "  patch distance : ", self.patch_distance, "   parameter h : ", self.param_h)
        self.patch_size = value
        self.label_size.setText("Patch Size : " + str(value))
        self.denoiseSlice()
    
    def distance_changed(self):
        value = self.slider_distance.value()
        print("distance changed : ", value, "  patch size : ", self.patch_size, "   parameter h : ", self.param_h)
        self.threshold = value
        
        self.label_distance.setText("Patch Distance : " + str(value))
        
        self.denoiseSlice()
        
    def h_changed(self):
        value = self.slider_h.value()
        self.param_h = value / 10_0.0        
        print("parameter h changed : ", self.param_h, "  patch size : ", self.patch_size, "  patch distance : ", self.patch_distance)
        
        self.label_h.setText("Parameter h : " + str(self.param_h))

        self.denoiseSlice()

    def denoiseSlice(self):
        print("denoiseSlice entered")
        
        a = gf.NonLocalMeanDenoising(self.expStack[0, :, :], self.param_h, True, self.patch_size, self.patch_distance)
        
        self.denoised_Stack[0, :, :] = a

        self.displayExpStack(self.denoised_Stack)
        
        self.Modified_pixels_proportion, self.mean_modified_pixels_intensity, self.mean_proportion_intensity = gf.Pixels_transformation(self.expStack[0, :, :], self.denoised_Stack[0, :, :])
        print("Taux de pxls modifié (%) : ", '%.1f'%(self.Modified_pixels_proportion), "  taux de transformation (%) : ", '%.2f'%(self.mean_proportion_intensity))

        self.denoised.setEnabled(False)
        print("denoise slice OK")

    def denoiseStack(self):
        print("denoiseStack entered")
        self.denoised.setEnabled(False)
        self.preview.setEnabled(False)
        
        for i in range(0,len(self.expStack[:, 0, 0])): # Applique pour chaque slice les paramètres du remove outlier
            a = gf.NonLocalMeanDenoising(self.expStack[i, :, :], self.param_h, True, self.patch_size, self.patch_distance)
            self.denoised_Stack[i, :, :] = a

            if (i+1)%10 == 0:
                print(f"slice {i+1} denoised")
                
        self.denoised.setCheckable(True)
        self.denoised.setEnabled(True)  
        self.denoised.setChecked(True)
        self.preview.setEnabled(True)
        
        self.parent.denoisedImage = np.copy(self.denoised_Stack)
        self.parent.denoisedImage = np.rot90(self.parent.denoisedImage, k=3, axes=(2, 1))
        self.parent.denoisedImage = np.flip(self.parent.denoisedImage, 1)

        print("Denoising achieved")
        self.drawCHORDprofiles()        
        
    
    def drawCHORDprofiles(self):
        
        try:
            self.profiles.clear()
            self.plotIt.addLine(x = self.expSeries.currentIndex)
            # self.plotIt.addLine(x = 120)
            if self.denoised.isChecked():
                self.profiles.plot(self.denoised_Stack[:, self.x, self.y], pen=(255, 255, 23))
            self.profiles.plot(self.expStack[:, self.x, self.y], pen=(255, 125, 200))
        except:
            pass
    def mouseMoved(self, e):

        pos = e[0]

        # print("mouseMoved", pos)
        if not self.mouseLock.isChecked():
            if self.expSeries.view.sceneBoundingRect().contains(pos):
    
                item = self.expSeries.view
                mousePoint = item.mapSceneToView(pos) 
                     
                self.crosshair_v1.setPos(mousePoint.x())
                self.crosshair_h1.setPos(mousePoint.y())

            self.x = int(mousePoint.x())
            self.y = int(mousePoint.y())
            
            # print(self.x, self.y)
            if self.x >= 0 and self.y >= 0 and self.x < len(self.expStack[0, :, 0]) and self.y < len(self.expStack[0, 0, :]):
                self.drawCHORDprofiles()

    
    def mouseClick(self, e):

        pos = e[0]
        
        self.mouseLock.toggle()
        
        fromPosX = pos.scenePos()[0]
        fromPosY = pos.scenePos()[1]
        
        posQpoint = QtCore.QPointF()
        posQpoint.setX(fromPosX)
        posQpoint.setY(fromPosY)

        if self.expSeries.view.sceneBoundingRect().contains(posQpoint):
                
            item = self.expSeries.view
            mousePoint = item.mapSceneToView(posQpoint) 

            self.crosshair_v1.setPos(mousePoint.x())
            self.crosshair_h1.setPos(mousePoint.y())
                 
            self.x = int(mousePoint.x())
            self.y = int(mousePoint.y())
            
        # print(self.x, self.y)
        if self.x >= 0 and self.y >= 0 and self.x < len(self.expStack[0, :, 0])and self.y < len(self.expStack[0, 0, :]):
            self.drawCHORDprofiles()
       
class launcher(object):
    def __init__(self, image, denoisedImage):
        
        self.image = image
        self.denoisedImage = denoisedImage
        
        self.denoiseGUI()
        
    def denoiseGUI(self):
        app = QApplication(sys.argv)
        w = MainWindow(self)
        w.show()
        app.setQuitOnLastWindowClosed(True)
        app.exec_()

if __name__ == '__main__':
    
    StackLoc, StackDir = gf.getFilePathDialog("Stack d'image' (*.tiff)")
    
    Raw_Stack = tf.TiffFile(StackLoc[0]).asarray()
    b = launcher(Raw_Stack, np.copy(Raw_Stack))


