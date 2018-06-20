import os, os.path, sys
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_explorerWindow import Ui_ExplorerWindow
import resources

class MapExplorer(QMainWindow, Ui_ExplorerWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.connect(self.actionQuit, SIGNAL("triggered()"), qApp.quit)
        self.connect(self.actionShowBasemapLayer, SIGNAL("triggered()"), self.showBasemapLayer)
        self.connect(self.actionShowLandmarkLayer, SIGNAL("triggered()"), self.showLandmarkLayer)
        self.connect(self.actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(self.actionPan, SIGNAL("triggered()"), self.setPanMode)
        self.connect(self.actionExplore, SIGNAL("triggered()"), self.setExploreMode)
        
        self.mapCanvas = QgsMapCanvas()
        self.mapCanvas.useImageToRender(False)
        self.mapCanvas.setCanvasColor(Qt.white)
        self.mapCanvas.show()
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mapCanvas)
        self.centralWidget.setLayout(layout)
        
        self.actionShowBasemapLayer.setChecked(True)
        self.actionShowLandmarkLayer.setChecked(True)
    
    def showBasemapLayer(self):
        self.showVisibleMapLayers()
    def showLandmarkLayer(self):
        self.showVisibleMapLayers()
    def zoomIn(self):
        pass
    def zoomOut(self):
        pass
    def setPanMode(self):
        pass
    def setExploreMode(self):
        pass
    def loadMap(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        
        filename = os.path.join(cur_dir, "data", "NE1_LR_LC_SR_W_DR", "NE1_LR_LC_SR_W_DR.tif")
        self.basemap_layer = QgsRasterLayer(filename, "basemap")
        #Returns False
        print self.basemap_layer.isValid()
        QgsMapLayerRegistry.instance().addMapLayer(self.basemap_layer)
        
        filename = os.path.join(cur_dir, "data","ne_10m_populated_places","ne_10m_populated_places.shp")
        self.landmark_layer = QgsVectorLayer(filename, "landmarks", "ogr")
        #Returns False
        print self.landmark_layer.isValid()
        QgsMapLayerRegistry.instance().addMapLayer(self.landmark_layer)
        
        mlr = QgsMapLayerRegistry.instance().mapLayers()
        count = 0
        for layer in mlr:
            print layer
            count += 1
        print count, "layers"
        
        self.showVisibleMapLayers()
        self.mapCanvas.setExtent(QgsRectangle(-127.7, 24.4, -79.3, 49.1))
        print "End"
    def showVisibleMapLayers(self):
        layers = []
        if self.actionShowLandmarkLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.landmark_layer))
        if self.actionShowBasemapLayer.isChecked():
            layers.append(QgsMapCanvasLayer(self.basemap_layer))
        self.mapCanvas.setLayerSet(layers)
        
def main():
    
    # QGIS_PREFIX = C:\OSGeo4W64\apps\qgis
    QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
    qgs = QgsApplication(sys.argv, True)
    qgs.initQgis()
    app = QApplication(sys.argv)
    
    window = MapExplorer()
    window.show()
    window.raise_()
    window.loadMap()
    
    app.exec_()
    app.deleteLater()
    QgsApplication.exitQgis()

if __name__ == "__main__":
    main()