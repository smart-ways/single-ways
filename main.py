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

    def _plot_city(self, G):
        pos = nx.circular_layout(G)
        node_labels = {}
        for u in G.nodes():
            node_labels[u] = u
        nx.draw(G, pos)
        nx.draw_networkx_labels(G, pos, labels = node_labels)
        plt.show()

    def read_city_data(self):
        file_city_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        # Plot city
        self.city = nx.read_edgelist(str(file_city_data), create_using=nx.DiGraph())
        self._plot_city(self.city)
        self.lblProcessing.setText("Done. OK")

    def read_traffic_data(self):
        file_traffic_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        # Add traffic data
        self.lblProcessing.setText("Done. OK")

    def process(self):
        self.lblProcessing.setText("Processing...")
        # Add traffic data
        self.lblProcessing.setText("Done. OK")

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
