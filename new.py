from qgis.core import *
from qgis.gui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import os
# Environment variable QGISHOME must be set to the 1.x install directory
# before running this application
qgis_prefix = os.getenv("QGIS_PREFIX")

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(800, 400)

        # Set the title for the app
        self.setWindowTitle("Map Canvas - By Ameet Chaudhari")

    def main(argv):
        # create Qt application
        app = QApplication(argv)

        # Initialize qgis libraries
        QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
        QgsApplication.initQgis()

        # create main window
        wnd = MainWindow()
        # Move the app window to upper left
        wnd.move(100,100)
        wnd.show()

        # run!
        retval = app.exec_()
        # exit
        QgsApplication.exitQgis()
        sys.exit(retval)

        if __name__ == "__main__":
            main(sys.argv)