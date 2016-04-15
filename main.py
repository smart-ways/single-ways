import csv
import sys
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from PyQt4 import QtGui

import city
import gui
import processor

class MainApp(QtGui.QMainWindow, gui.Ui_SmartWays):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.city = nx.DiGraph()
        self.setupUi(self)
        self.btnReadCityData.clicked.connect(self.read_city_data)
        self.btnReadTrafficData.clicked.connect(self.read_traffic_data)
        self.btnProcess.clicked.connect(self.process)
        self.btnViewCity.clicked.connect(self.view_city)
        self.btnViewTraffic.clicked.connect(self.view_traffic)

    def _csv_data_reader(self, filename):
        columns = defaultdict(list)
        with open(filename) as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                for (i,v) in enumerate(row):
                    columns[i].append(v)
        return columns

    def read_city_data(self):
        self.file_city_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        self.city = city.City()
        columns = _csv_data_reader(str(self.file_traffic_data))
        for i in len(columns):
            if int(columns[2][i]) == 1:
                self.city.add_route(columns[0][i], columns[1][i],
                                    length=float(columns[3][i]))
            else:
                self.city.add_route(columns[1][i], columns[0][i],
                                    length=float(columns[3][i]))
        self.lblProcessing.setText("Done. OK")
        self.btnViewCity.setEnabled(True)

    def read_traffic_data(self):
        self.file_traffic_data = QtGui.QFileDialog.getOpenFileName(self)
        self.lblProcessing.setText("Processing...")
        self.lblProcessing.setText("Done. OK")

    def process(self):
        self.lblProcessing.setText("Processing...")
        # self.G has edges colored green and destination nodes colored red
        self.G = processor.process(self.city, self.file_traffic_data)
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

    def view_traffic(self):
        # Plot colored graph self.G
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
