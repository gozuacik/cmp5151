import sys
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import random
from matplotlib.figure import Figure
import Search

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Benchmarking Tool for Sorting and Searching Algorithms')

        # First Text Area
        self.txt = QTextEdit(self)
        self.txt.move(100, 60)
        self.txt.resize(200, 30)
        self.txt.setReadOnly(True)
        self.txt.setText("Searching Algorithms")

        # Second Text Area
        self.txt1 = QTextEdit(self)
        self.txt1.move(350, 60)
        self.txt1.resize(200, 30)
        self.txt1.setReadOnly(True)
        self.txt1.setText("Use Cases")

        # Third Text Area
        self.txt2 = QTextEdit(self)
        self.txt2.move(700, 60)
        self.txt2.resize(200, 30)
        self.txt2.setReadOnly(True)
        self.txt2.setText("Sorting Algorithms")

        # Fourth Text Area
        self.txt3 = QTextEdit(self)
        self.txt3.move(950, 60)
        self.txt3.resize(200, 30)
        self.txt3.setReadOnly(True)
        self.txt3.setText("Use Cases")

        # First Combo Box
        self.comboBoxSearch = QComboBox(self)
        self.comboBoxSearch.move(100, 100)
        self.comboBoxSearch.resize(200, 30)

        self.comboBoxSearch.addItem('Linear')
        self.comboBoxSearch.addItem('Binary')
        self.comboBoxSearch.addItem('Jump')
        self.comboBoxSearch.addItem('Interpolation')
        self.comboBoxSearch.addItem('All')

        # Second Combo Box
        self.comboBoxSearch2 = QComboBox(self)
        self.comboBoxSearch2.move(350, 100)
        self.comboBoxSearch2.resize(200, 30)

        self.comboBoxSearch2.addItem('Best')
        self.comboBoxSearch2.addItem('Worst')
        self.comboBoxSearch2.addItem('Average')
        self.comboBoxSearch2.addItem('All')

        # First Button
        self.pushButtonOk = QPushButton('Run', self)
        self.pushButtonOk.move(250, 150)
        self.pushButtonOk.clicked.connect(self.buttonClickHandler)


        # Third Combo Box
        self.comboBoxSearch3 = QComboBox(self)
        self.comboBoxSearch3.move(700, 100)
        self.comboBoxSearch3.resize(200, 30)

        self.comboBoxSearch3.addItem('Bubble')
        self.comboBoxSearch3.addItem('Selection')
        self.comboBoxSearch3.addItem('Merge')
        self.comboBoxSearch3.addItem('Quick')
        self.comboBoxSearch3.addItem('All')

        # Fourth Combo Box
        self.comboBoxSearch4 = QComboBox(self)
        self.comboBoxSearch4.move(950, 100)
        self.comboBoxSearch4.resize(200, 30)

        self.comboBoxSearch4.addItem('Best')
        self.comboBoxSearch4.addItem('Worst')
        self.comboBoxSearch4.addItem('Average')
        self.comboBoxSearch4.addItem('All')

        # Second Button
        self.pushButtonOk2 = QPushButton('Run', self)
        self.pushButtonOk2.move(850, 150)
        self.pushButtonOk2.clicked.connect(self.buttonClickHandler2)


    def showValues(self,x,y):
        print("Search Algorithm: ",x)
        print("Use Case: ", y)

    # Click Handler for First Run Button
    def buttonClickHandler(self):
        #self.showValues(self.comboBoxSearch.currentText(),self.comboBoxSearch1.currentText())
        print("Search Algorithm: ",self.comboBoxSearch.currentText())
        print("Use Case: ", self.comboBoxSearch2.currentText())
        if self.comboBoxSearch.currentText() == 'All':
            Search.runAll(self.comboBoxSearch.currentText(), self.comboBoxSearch2.currentText())
        else:
            Search.runSearch(self.comboBoxSearch.currentText(),self.comboBoxSearch2.currentText())
        #self.secondWindow = SecondWindow(fig1,fig2)
        #self.dialogs.append(secondWindow)
        #self.secondWindow.show()
        #self.initUI()
        #self.plot()
        #QMessageBox.information(self, 'Message', 'checked' if self.checkBox.isChecked() else 'unchecked')

    # Click Handler for Second Run Button
    def buttonClickHandler2(self):
        #self.showValues(self.comboBoxSearch.currentText(),self.comboBoxSearch1.currentText())
        print("Sort Algorithm: ",self.comboBoxSearch3.currentText())
        print("Use Case: ", self.comboBoxSearch4.currentText())
        self.secondWindow = SecondWindow()
        #self.dialogs.append(secondWindow)
        self.secondWindow.show()
        #self.initUI()
        #self.plot()
        #QMessageBox.information(self, 'Message', 'checked' if self.checkBox.isChecked() else 'unchecked')

class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Performance Results'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self,width=5, height=4)
        m.move(0, 0)
        '''
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)
        '''
        self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self,parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax=self.fig1
        #ax.plot(data, 'r-')
        #ax.set_title('PyQt Matplotlib Example')
        self.draw()


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

main()

