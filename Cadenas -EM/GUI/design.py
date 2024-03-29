# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 523)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    font: 12pt \"Lato\";\n"
"     border-radius: 10px;\n"
"     background-color:      #ffffff;\n"
"    width:                 24px;\n"
"    height:                 24px;\n"
"    border: 2px solid  #000000;\n"
"    }\n"
"\n"
" QPushButton:hover {\n"
"        background-color:#ffffff;\n"
"        color: #0f0e17;\n"
"    }\n"
"\n"
"QRadioButton{\n"
"font: 12pt \"Lato\";\n"
"color: black;\n"
"}\n"
"QLabel{\n"
"font: 12pt \"Lato\";\n"
"color: black;\n"
"}\n"
"\n"
"QTabWidget::pane {             \n"
"            border-width: 2px;         \n"
"            border-style: solid;       \n"
"            border-color: #000000;         \n"
"            border-radius: 2px;                 \n"
"        }\n"
"\n"
"\n"
"QTabBar::tab{\n"
"background-color:#ffffff;\n"
"border:2px solid #000000;\n"
"color: black;\n"
"width:70px;                                    \n"
"border-radius:2px;\n"
"border-top-left-radius: 1px;                   \n"
" border-top-right-radius:1px;\n"
"padding:5px 8px;\n"
"font: 10pt \"Lato\";\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected{\n"
"border:2px solid purple;\n"
"color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lato\";\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"font: 10pt \"Lato\";\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"\n"
"    font: 12pt \"Lato\";\n"
"    padding-right: 2px; \n"
"    border-width: 5;\n"
"    background-color: rgb(255, 255, 255);\n"
"    background-color: white;\n"
"    border-style: outset;\n"
"    border-color: white;    \n"
"    border-radius:  8px;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.tabWidget_r2 = QtWidgets.QTabWidget(self.frame)
        self.tabWidget_r2.setObjectName("tabWidget_r2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_17.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.in_horm = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_horm.setMinimum(1.0)
        self.in_horm.setMaximum(400.0)
        self.in_horm.setObjectName("in_horm")
        self.horizontalLayout_2.addWidget(self.in_horm)
        self.verticalLayout_17.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.in_C = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_C.setDecimals(0)
        self.in_C.setMinimum(1.0)
        self.in_C.setMaximum(90.0)
        self.in_C.setProperty("value", 20.0)
        self.in_C.setObjectName("in_C")
        self.horizontalLayout_4.addWidget(self.in_C)
        self.verticalLayout_17.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.in_n_motor = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_n_motor.setMinimum(1.0)
        self.in_n_motor.setMaximum(3000.0)
        self.in_n_motor.setObjectName("in_n_motor")
        self.horizontalLayout_3.addWidget(self.in_n_motor)
        self.verticalLayout_17.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.in_n_d = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_n_d.setMinimum(1.0)
        self.in_n_d.setObjectName("in_n_d")
        self.horizontalLayout_15.addWidget(self.in_n_d)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.in_ndientes_impulsora = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_ndientes_impulsora.setDecimals(0)
        self.in_ndientes_impulsora.setMinimum(11.0)
        self.in_ndientes_impulsora.setMaximum(999.0)
        self.in_ndientes_impulsora.setObjectName("in_ndientes_impulsora")
        self.horizontalLayout_5.addWidget(self.in_ndientes_impulsora)
        self.verticalLayout_17.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.in_rv = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.in_rv.setMinimum(0.01)
        self.in_rv.setMaximum(100.0)
        self.in_rv.setProperty("value", 1.0)
        self.in_rv.setObjectName("in_rv")
        self.horizontalLayout_6.addWidget(self.in_rv)
        self.verticalLayout_17.addLayout(self.horizontalLayout_6)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_17.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_17.addWidget(self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_17.addWidget(self.label_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rb_caracteristica = QtWidgets.QRadioButton(self.frame_2)
        self.rb_caracteristica.setChecked(True)
        self.rb_caracteristica.setObjectName("rb_caracteristica")
        self.horizontalLayout_7.addWidget(self.rb_caracteristica)
        self.rb_torcion_alto = QtWidgets.QRadioButton(self.frame_2)
        self.rb_torcion_alto.setObjectName("rb_torcion_alto")
        self.horizontalLayout_7.addWidget(self.rb_torcion_alto)
        self.verticalLayout_17.addLayout(self.horizontalLayout_7)
        self.bt_calcular = QtWidgets.QPushButton(self.frame_2)
        self.bt_calcular.setMinimumSize(QtCore.QSize(0, 35))
        self.bt_calcular.setObjectName("bt_calcular")
        self.verticalLayout_17.addWidget(self.bt_calcular)
        self.horizontalLayout.addWidget(self.frame_2)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_18.addWidget(self.label_12)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_18.addWidget(self.label_2)
        self.bt_save_data = QtWidgets.QPushButton(self.frame_3)
        self.bt_save_data.setMinimumSize(QtCore.QSize(0, 35))
        self.bt_save_data.setObjectName("bt_save_data")
        self.verticalLayout_18.addWidget(self.bt_save_data)
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_18.addWidget(self.line)
        self.horizontalLayout.addWidget(self.frame_3)
        self.tabWidget_r2.addTab(self.tab, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_14 = QtWidgets.QFrame(self.tab_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tableWidget_15 = QtWidgets.QTableWidget(self.frame_14)
        self.tableWidget_15.setObjectName("tableWidget_15")
        self.tableWidget_15.setColumnCount(5)
        self.tableWidget_15.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(4, item)
        self.verticalLayout_16.addWidget(self.tableWidget_15)
        self.verticalLayout_15.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.tab_8)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_15.addWidget(self.frame_15)
        self.verticalLayout_15.setStretch(0, 4)
        self.verticalLayout_15.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_8, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_19_1 = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_19_1.setObjectName("tableWidget_19_1")
        self.tableWidget_19_1.setColumnCount(7)
        self.tableWidget_19_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_1.setHorizontalHeaderItem(6, item)
        self.verticalLayout_6.addWidget(self.tableWidget_19_1)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.tab_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.tab_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidget_19_2 = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_19_2.setObjectName("tableWidget_19_2")
        self.tableWidget_19_2.setColumnCount(7)
        self.tableWidget_19_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19_2.setHorizontalHeaderItem(6, item)
        self.verticalLayout_8.addWidget(self.tableWidget_19_2)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.tab_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7.addWidget(self.frame_7)
        self.verticalLayout_7.setStretch(0, 4)
        self.verticalLayout_7.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_20 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(15)
        self.tableWidget_20.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(14, item)
        self.verticalLayout_4.addWidget(self.tableWidget_20)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3.addWidget(self.widget_2)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.tab_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tableWidget_22 = QtWidgets.QTableWidget(self.frame_8)
        self.tableWidget_22.setShowGrid(True)
        self.tableWidget_22.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget_22.setRowCount(1)
        self.tableWidget_22.setColumnCount(3)
        self.tableWidget_22.setObjectName("tableWidget_22")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(2, item)
        self.tableWidget_22.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_10.addWidget(self.tableWidget_22)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.tab_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_9.addWidget(self.frame_9)
        self.verticalLayout_9.setStretch(0, 4)
        self.verticalLayout_9.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_10 = QtWidgets.QFrame(self.tab_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tableWidget_23 = QtWidgets.QTableWidget(self.frame_10)
        self.tableWidget_23.setObjectName("tableWidget_23")
        self.tableWidget_23.setColumnCount(2)
        self.tableWidget_23.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(1, item)
        self.verticalLayout_12.addWidget(self.tableWidget_23)
        self.verticalLayout_11.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.tab_7)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_11.addWidget(self.frame_11)
        self.verticalLayout_11.setStretch(0, 4)
        self.verticalLayout_11.setStretch(1, 1)
        self.tabWidget_r2.addTab(self.tab_7, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_13 = QtWidgets.QFrame(self.tab_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.tableWidget_result1 = QtWidgets.QTableWidget(self.frame_13)
        self.tableWidget_result1.setObjectName("tableWidget_result1")
        self.tableWidget_result1.setColumnCount(3)
        self.tableWidget_result1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result1.setHorizontalHeaderItem(2, item)
        self.verticalLayout_20.addWidget(self.tableWidget_result1)
        self.verticalLayout_19.addWidget(self.frame_13)
        self.tabWidget_r2.addTab(self.tab_9, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_12 = QtWidgets.QFrame(self.tab_2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tableWidget_result2 = QtWidgets.QTableWidget(self.frame_12)
        self.tableWidget_result2.setObjectName("tableWidget_result2")
        self.tableWidget_result2.setColumnCount(6)
        self.tableWidget_result2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result2.setHorizontalHeaderItem(5, item)
        self.verticalLayout_14.addWidget(self.tableWidget_result2)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.verticalLayout_13.setStretch(0, 4)
        self.tabWidget_r2.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget_r2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_r2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI"))
        self.label_10.setText(_translate("MainWindow", "SELECCIÓN DE CADENAS -ANSI"))
        self.label.setText(_translate("MainWindow", "ENTRADAS"))
        self.label_3.setText(_translate("MainWindow", "Potencia nominal del motor[HP]"))
        self.label_5.setText(_translate("MainWindow", "Distancia entre centros [Pasos]"))
        self.label_4.setText(_translate("MainWindow", "Velocidad del motor [RPM]"))
        self.label_11.setText(_translate("MainWindow", "Factor de diseño"))
        self.label_6.setText(_translate("MainWindow", "# dientes de catarina impulsora"))
        self.label_7.setText(_translate("MainWindow", "Relacion de trasmision"))
        self.label_8.setText(_translate("MainWindow", "Seleccione el tipo de maquina  (Factor de servicio)"))
        self.label_9.setText(_translate("MainWindow", "Fuente de Potencia"))
        self.rb_caracteristica.setText(_translate("MainWindow", "Par de torsión normal"))
        self.rb_torcion_alto.setText(_translate("MainWindow", "Par de torsión alto"))
        self.bt_calcular.setText(_translate("MainWindow", "CALCULAR"))
        self.label_12.setText(_translate("MainWindow", "Verifique la tabla de resultados"))
        self.bt_save_data.setText(_translate("MainWindow", "GUARDAR DATOS"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab), _translate("MainWindow", "Calculos"))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fuente de potencia            \n"
""))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fuente de potencia            \n"
""))
        item = self.tableWidget_15.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fuente de potencia            \n"
""))
        item = self.tableWidget_15.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fuente de potencia            \n"
""))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_8), _translate("MainWindow", "Tabla 17-15"))
        item = self.tableWidget_19_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de cadena ANSI"))
        item = self.tableWidget_19_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Paso (pulg)"))
        item = self.tableWidget_19_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ancho (pulg)"))
        item = self.tableWidget_19_1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rest. mín. a la tensión (lbf)"))
        item = self.tableWidget_19_1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Peso promedio (lbf/pie)"))
        item = self.tableWidget_19_1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Diámetro del rodillo (pulg)"))
        item = self.tableWidget_19_1.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "espct. d\' hileras múlt. (pulg)"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_4), _translate("MainWindow", "Tabla 17-19"))
        item = self.tableWidget_19_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de cadena ANSI"))
        item = self.tableWidget_19_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Paso (mm)"))
        item = self.tableWidget_19_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ancho (mm)"))
        item = self.tableWidget_19_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rest. mín. a la tensión (N)"))
        item = self.tableWidget_19_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Peso promedio (N/m)"))
        item = self.tableWidget_19_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Diámetro del rodillo (mm)"))
        item = self.tableWidget_19_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "espc. de hileras múlt. (mm)"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_5), _translate("MainWindow", "Tabla 17-19"))
        item = self.tableWidget_20.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "V, (RPM)"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_3), _translate("MainWindow", "Tabla 17-20"))
        item = self.tableWidget_22.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de dientes de catarina impulsora"))
        item = self.tableWidget_22.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Potencia preextremo K1"))
        item = self.tableWidget_22.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Potencia posextremo, K1"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_6), _translate("MainWindow", "Tabla 17-22"))
        item = self.tableWidget_23.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número de hileras"))
        item = self.tableWidget_23.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "K2"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_7), _translate("MainWindow", "Tabla 17-23"))
        item = self.tableWidget_result1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Numero de Hileras"))
        item = self.tableWidget_result1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "K2"))
        item = self.tableWidget_result1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Potencia Requerida"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_9), _translate("MainWindow", "Resultados"))
        item = self.tableWidget_result2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "# Hileras"))
        item = self.tableWidget_result2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Potencia de tablas"))
        item = self.tableWidget_result2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de lubricacion"))
        item = self.tableWidget_result2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ANSI"))
        item = self.tableWidget_result2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lp (pasos)"))
        item = self.tableWidget_result2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lc (pasos)"))
        self.tabWidget_r2.setTabText(self.tabWidget_r2.indexOf(self.tab_2), _translate("MainWindow", "Resultados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
