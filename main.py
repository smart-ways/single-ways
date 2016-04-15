import sys
import matplotlib.pyplot as plt
import networkx as nx
from PyQt4 import QtGui

import gui

class MainApp(QtGui.QMainWindow, gui.Ui_SmartWays):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.city = nx.DiGraph()
        self.setupUi(self)
        self.btnReadCityData.clicked.connect(self.read_city_data)
        self.btnReadTrafficData.clicked.connect(self.read_traffic_data)
        self.btnProcess.clicked.connect(self.process)
        self.btnViewCity.clicked.connect(self.view_city)

    def read_city_data(self):
        file_city_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        self.city = nx.read_edgelist(str(file_city_data), create_using=nx.DiGraph())
        self.lblProcessing.setText("Done. OK")
        self.btnViewCity.setEnabled(True)

    def read_traffic_data(self):
        file_traffic_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        # Add traffic data
        self.lblProcessing.setText("Done. OK")

    def process(self):
        self.lblProcessing.setText("Processing...")
        # Add traffic data
        self.lblProcessing.setText("Done. OK")

    def view_city(self):
        pos = nx.circular_layout(self.city)
        node_labels = {}
        for u in self.city.nodes():
            node_labels[u] = u
        nx.draw(self.city, pos)
        nx.draw_networkx_labels(self.city, pos, labels=node_labels)
        self.btnViewCity.setEnabled(True)
        plt.show()


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
