# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fitting/qt/view.ui'
#
# Created: Fri Jan 11 13:59:50 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui,QtWidgets

class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(1024, 742)
        font = QtGui.QFont()
        font.setPointSize(11)
        View.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(View)
        #self.horizontalLayout = QtGui.QHBoxLayout(View)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.controlPanel_widget = QtGui.QWidget(View)
        self.controlPanel_widget = QtWidgets.QWidget(View)
        self.controlPanel_widget.setMinimumSize(QtCore.QSize(270, 0))
        self.controlPanel_widget.setObjectName("controlPanel_widget")
        #self.verticalLayout = QtGui.QVBoxLayout(self.controlPanel_widget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.controlPanel_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.leftLung_groupBox = QtGui.QGroupBox(self.controlPanel_widget)
        self.leftLung_groupBox = QtWidgets.QGroupBox(self.controlPanel_widget)
        self.leftLung_groupBox.setObjectName("leftLung_groupBox")
        #self.gridLayout_4 = QtGui.QGridLayout(self.leftLung_groupBox)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.leftLung_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        #self.datacloudIpdata_lineEdit = QtGui.QLineEdit(self.leftLung_groupBox)
        self.datacloudIpdata_lineEdit = QtWidgets.QLineEdit(self.leftLung_groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.datacloudIpdata_lineEdit.setFont(font)
        self.datacloudIpdata_lineEdit.setObjectName("datacloudIpdata_lineEdit")
        self.gridLayout_4.addWidget(self.datacloudIpdata_lineEdit, 0, 0, 1, 1)
        #self.surfaceIpnode_pushButton = QtGui.QPushButton(self.leftLung_groupBox)
        self.surfaceIpnode_pushButton = QtWidgets.QPushButton(self.leftLung_groupBox)
        self.surfaceIpnode_pushButton.setObjectName("surfaceIpnode_pushButton")
        self.gridLayout_4.addWidget(self.surfaceIpnode_pushButton, 1, 1, 1, 1)
        #self.datacloudIpdata_pushButton = QtGui.QPushButton(self.leftLung_groupBox)
        self.datacloudIpdata_pushButton = QtWidgets.QPushButton(self.leftLung_groupBox)
        self.datacloudIpdata_pushButton.setObjectName("datacloudIpdata_pushButton")
        self.gridLayout_4.addWidget(self.datacloudIpdata_pushButton, 0, 1, 1, 1)
       # self.surfaceIpnode_lineEdit = QtGui.QLineEdit(self.leftLung_groupBox)
        self.surfaceIpnode_lineEdit = QtWidgets.QLineEdit(self.leftLung_groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.surfaceIpnode_lineEdit.setFont(font)
        self.surfaceIpnode_lineEdit.setObjectName("surfaceIpnode_lineEdit")
        self.gridLayout_4.addWidget(self.surfaceIpnode_lineEdit, 1, 0, 1, 1)
        #self.surfaceIpelem_pushButton = QtGui.QPushButton(self.leftLung_groupBox)
        self.surfaceIpelem_pushButton = QtWidgets.QPushButton(self.leftLung_groupBox)
        self.surfaceIpelem_pushButton.setObjectName("surfaceIpelem_pushButton")
        self.gridLayout_4.addWidget(self.surfaceIpelem_pushButton, 2, 1, 1, 1)
        #self.surfaceIpelem_lineEdit = QtGui.QLineEdit(self.leftLung_groupBox)
        self.surfaceIpelem_lineEdit = QtWidgets.QLineEdit(self.leftLung_groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.surfaceIpelem_lineEdit.setFont(font)
        self.surfaceIpelem_lineEdit.setObjectName("surfaceIpelem_lineEdit")
        self.gridLayout_4.addWidget(self.surfaceIpelem_lineEdit, 2, 0, 1, 1)
        #self.showDatacloud_checkBox = QtGui.QCheckBox(self.leftLung_groupBox)
        self.showDatacloud_checkBox = QtWidgets.QCheckBox(self.leftLung_groupBox)
        self.showDatacloud_checkBox.setChecked(True)
        self.showDatacloud_checkBox.setObjectName("showDatacloud_checkBox")
        self.gridLayout_4.addWidget(self.showDatacloud_checkBox, 4, 0, 1, 2)
        #self.showMesh_checkBox = QtGui.QCheckBox(self.leftLung_groupBox)
        self.showMesh_checkBox = QtWidgets.QCheckBox(self.leftLung_groupBox)
        self.showMesh_checkBox.setChecked(True)
        self.showMesh_checkBox.setObjectName("showMesh_checkBox")
        self.gridLayout_4.addWidget(self.showMesh_checkBox, 5, 0, 1, 2)
        self.showNode_checkBox = Qtwidgets.QCheckbox(self.leftLung_groupBox)
        self.showNode_checkBox.setChecked(True)
        self.showNode_checkBox.setObjectName("showNode_checkBox")
        self.gridLayout_4.addWidget(self.showNode_checkBox, 6, 0, 1, 2)
        #self.load_pushButton = QtGui.QPushButton(self.leftLung_groupBox)
        self.load_pushButton = QtWidgets.QPushButton(self.leftLung_groupBox)
        self.load_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.load_pushButton.setObjectName("load_pushButton")
        self.gridLayout_4.addWidget(self.load_pushButton, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.leftLung_groupBox)
        #self.groupBox_2 = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.controlPanel_widget)
        self.groupBox_2.setObjectName("groupBox_2")
        #self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #self.iterations_spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.iterations_spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.iterations_spinBox.setMinimum(1)
        self.iterations_spinBox.setMaximum(20)
        self.iterations_spinBox.setProperty("value", 8)
        self.iterations_spinBox.setObjectName("iterations_spinBox")
        self.gridLayout_3.addWidget(self.iterations_spinBox, 2, 1, 1, 1)
        #self.fit_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.fit_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.fit_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.fit_pushButton.setObjectName("fit_pushButton")
        self.gridLayout_3.addWidget(self.fit_pushButton, 4, 0, 1, 2)
        #self.label = QtGui.QLabel(self.groupBox_2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        #self.landmarks_groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.landmarks_groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.landmarks_groupBox.setObjectName("landmarks_groupBox")
        #self.gridLayout = QtGui.QGridLayout(self.landmarks_groupBox)
        self.gridLayout = QtWidgets.QGridLayout(self.landmarks_groupBox)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        #self.ventralNode_pushButton = QtGui.QPushButton(self.landmarks_groupBox)
        self.ventralNode_pushButton = QtWidgets.QPushButton(self.landmarks_groupBox)
        self.ventralNode_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ventralNode_pushButton.setFont(font)
        self.ventralNode_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ventralNode_pushButton.setAutoFillBackground(False)
        self.ventralNode_pushButton.setStyleSheet("color:olive;")
        self.ventralNode_pushButton.setCheckable(True)
        self.ventralNode_pushButton.setObjectName("ventralNode_pushButton")
        self.gridLayout.addWidget(self.ventralNode_pushButton, 1, 0, 1, 1)
        #self.apexNode_pushButton = QtGui.QPushButton(self.landmarks_groupBox)
        self.apexNode_pushButton = QtWidgets.QPushButton(self.landmarks_groupBox)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apexNode_pushButton.sizePolicy().hasHeightForWidth())
        self.apexNode_pushButton.setSizePolicy(sizePolicy)
        self.apexNode_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.apexNode_pushButton.setFont(font)
        self.apexNode_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.apexNode_pushButton.setAutoFillBackground(False)
        self.apexNode_pushButton.setStyleSheet("color:green;")
        self.apexNode_pushButton.setCheckable(True)
        self.apexNode_pushButton.setObjectName("apexNode_pushButton")
        self.gridLayout.addWidget(self.apexNode_pushButton, 0, 0, 1, 1)
        #self.basalNode_pushButton = QtGui.QPushButton(self.landmarks_groupBox)
        self.basalNode_pushButton = QtWidgets.QPushButton(self.landmarks_groupBox)
        self.basalNode_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.basalNode_pushButton.setFont(font)
        self.basalNode_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.basalNode_pushButton.setAutoFillBackground(False)
        self.basalNode_pushButton.setStyleSheet("color:maroon;")
        self.basalNode_pushButton.setCheckable(True)
        self.basalNode_pushButton.setObjectName("basalNode_pushButton")
        self.gridLayout.addWidget(self.basalNode_pushButton, 0, 1, 1, 1)
       #self.lateralNode_pushButton = QtGui.QPushButton(self.landmarks_groupBox)
        self.lateralNode_pushButton = QtWidgets.QPushButton(self.landmarks_groupBox)
        self.lateralNode_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lateralNode_pushButton.setFont(font)
        self.lateralNode_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lateralNode_pushButton.setAutoFillBackground(False)
        self.lateralNode_pushButton.setStyleSheet("color:navy;")
        self.lateralNode_pushButton.setCheckable(True)
        self.lateralNode_pushButton.setObjectName("lateralNode_pushButton")
        self.gridLayout.addWidget(self.lateralNode_pushButton, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.landmarks_groupBox, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        #spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        #self.groupBox = QtGui.QGroupBox(self.controlPanel_widget)
        self.groupBox = QtWidgets.QGroupBox(self.controlPanel_widget)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        #self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #self.outputExnode_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.outputExnode_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputExnode_lineEdit.setFont(font)
        self.outputExnode_lineEdit.setObjectName("outputExnode_lineEdit")
        self.gridLayout_2.addWidget(self.outputExnode_lineEdit, 0, 0, 1, 1)
        #self.outputExelem_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.outputExelem_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.outputExelem_lineEdit.setFont(font)
        self.outputExelem_lineEdit.setObjectName("outputExelem_lineEdit")
        self.gridLayout_2.addWidget(self.outputExelem_lineEdit, 1, 0, 1, 1)
        #self.outputExnode_pushButton = QtGui.QPushButton(self.groupBox)
        self.outputExnode_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.outputExnode_pushButton.setObjectName("outputExnode_pushButton")
        self.gridLayout_2.addWidget(self.outputExnode_pushButton, 0, 1, 1, 1)
        #self.outputExelem_pushButton = QtGui.QPushButton(self.groupBox)
        self.outputExelem_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.outputExelem_pushButton.setObjectName("outputExelem_pushButton")
        self.gridLayout_2.addWidget(self.outputExelem_pushButton, 1, 1, 1, 1)
        #self.save_pushButton = QtGui.QPushButton(self.groupBox)
        self.save_pushButton = QtWidgets.QPushButton(self.groupBox)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_pushButton.sizePolicy().hasHeightForWidth())
        self.save_pushButton.setSizePolicy(sizePolicy)
        self.save_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.save_pushButton.setObjectName("save_pushButton")
        self.gridLayout_2.addWidget(self.save_pushButton, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        #self.info_pushButton = QtGui.QPushButton(self.controlPanel_widget)
        self.info_pushButton = QtWidgets.QPushButton(self.controlPanel_widget)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pushButton.sizePolicy().hasHeightForWidth())
        self.info_pushButton.setSizePolicy(sizePolicy)
        self.info_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.info_pushButton.setFlat(True)
        self.info_pushButton.setObjectName("info_pushButton")
        self.verticalLayout.addWidget(self.info_pushButton)
        self.horizontalLayout.addWidget(self.controlPanel_widget)
        self.sceneviewer_widget = SceneviewerWidget(View)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        #View.setWindowTitle(QtGui.QApplication.translate("View", "Lung fitting", None, QtGui.QApplication.UnicodeUTF8))
        View.setWindowTitle(QtWidgets.QApplication.translate("View", "Lung fitting", None))
        #self.leftLung_groupBox.setTitle(QtGui.QApplication.translate("View", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLung_groupBox.setTitle(QtWidgets.QApplication.translate("View", "Inputs", None))
        #self.surfaceIpnode_pushButton.setText(QtGui.QApplication.translate("View", ".ipnode", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceIpnode_pushButton.setText(QtWidgets.QApplication.translate("View", ".ipnode", None))
        #self.datacloudIpdata_pushButton.setText(QtGui.QApplication.translate("View", ".ipdata", None, QtGui.QApplication.UnicodeUTF8))
        self.datacloudIpdata_pushButton.setText(QtWidgets.QApplication.translate("View", ".ipdata", None))
        #self.surfaceIpelem_pushButton.setText(QtGui.QApplication.translate("View", ".ipelem", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceIpelem_pushButton.setText(QtWidgets.QApplication.translate("View", ".ipelem", None))
        
        """
        self.showDatacloud_checkBox.setText(QtGui.QApplication.translate("View", "Show data cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.showMesh_checkBox.setText(QtGui.QApplication.translate("View", "Show surface mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.load_pushButton.setText(QtGui.QApplication.translate("View", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("View", "Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.fit_pushButton.setText(QtGui.QApplication.translate("View", "Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("View", "Iterations:", None, QtGui.QApplication.UnicodeUTF8))
        self.landmarks_groupBox.setTitle(QtGui.QApplication.translate("View", "Choosing landmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.ventralNode_pushButton.setAccessibleName(QtGui.QApplication.translate("View", "ventral", None, QtGui.QApplication.UnicodeUTF8))
        self.ventralNode_pushButton.setText(QtGui.QApplication.translate("View", "Ventral", None, QtGui.QApplication.UnicodeUTF8))
        self.apexNode_pushButton.setAccessibleName(QtGui.QApplication.translate("View", "apex", None, QtGui.QApplication.UnicodeUTF8))
        self.apexNode_pushButton.setText(QtGui.QApplication.translate("View", "Apex", None, QtGui.QApplication.UnicodeUTF8))
        self.basalNode_pushButton.setAccessibleName(QtGui.QApplication.translate("View", "basal", None, QtGui.QApplication.UnicodeUTF8))
        self.basalNode_pushButton.setText(QtGui.QApplication.translate("View", "Basal", None, QtGui.QApplication.UnicodeUTF8))
        self.lateralNode_pushButton.setAccessibleName(QtGui.QApplication.translate("View", "lateral", None, QtGui.QApplication.UnicodeUTF8))
        self.lateralNode_pushButton.setText(QtGui.QApplication.translate("View", "Lateral", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("View", "Saving", None, QtGui.QApplication.UnicodeUTF8))
        self.outputExnode_pushButton.setText(QtGui.QApplication.translate("View", ".exnode", None, QtGui.QApplication.UnicodeUTF8))
        self.outputExelem_pushButton.setText(QtGui.QApplication.translate("View", ".exelem", None, QtGui.QApplication.UnicodeUTF8))
        self.save_pushButton.setText(QtGui.QApplication.translate("View", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.info_pushButton.setText(QtGui.QApplication.translate("View", "Info", None, QtGui.QApplication.UnicodeUTF8))
        """


        self.showDatacloud_checkBox.setText(QtWidgets.QApplication.translate("View", "Show data cloud", None))
        self.showMesh_checkBox.setText(QtWidgets.QApplication.translate("View", "Show surface mesh", None))
        self.showNode_checkBox.setText(QtWidgets.QApplication.translate("View", "Show sphere node", None))
        self.load_pushButton.setText(QtWidgets.QApplication.translate("View", "Load", None))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("View", "Fitting", None))
        self.fit_pushButton.setText(QtWidgets.QApplication.translate("View", "Fit", None))
        self.label.setText(QtWidgets.QApplication.translate("View", "Iterations:", None))
        self.landmarks_groupBox.setTitle(QtWidgets.QApplication.translate("View", "Choosing landmarks", None))
        self.ventralNode_pushButton.setAccessibleName(QtWidgets.QApplication.translate("View", "ventral", None))
        self.ventralNode_pushButton.setText(QtWidgets.QApplication.translate("View", "Ventral", None))
        self.apexNode_pushButton.setAccessibleName(QtWidgets.QApplication.translate("View", "apex", None))
        self.apexNode_pushButton.setText(QtWidgets.QApplication.translate("View", "Apex", None))
        self.basalNode_pushButton.setAccessibleName(QtWidgets.QApplication.translate("View", "basal", None))
        self.basalNode_pushButton.setText(QtWidgets.QApplication.translate("View", "Basal", None))
        self.lateralNode_pushButton.setAccessibleName(QtWidgets.QApplication.translate("View", "lateral", None))
        self.lateralNode_pushButton.setText(QtWidgets.QApplication.translate("View", "Lateral", None))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("View", "Saving", None))
        self.outputExnode_pushButton.setText(QtWidgets.QApplication.translate("View", ".exnode", None))
        self.outputExelem_pushButton.setText(QtWidgets.QApplication.translate("View", ".exelem", None))
        self.save_pushButton.setText(QtWidgets.QApplication.translate("View", "Save", None))
        self.info_pushButton.setText(QtWidgets.QApplication.translate("View", "Info", None))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

if __name__ == "__main__":
    import sys
    #app = QtGui.QApplication(sys.argv)
    #View = QtGui.QWidget()
    app = QtWidgets.QApplication(sys.argv)
    View = QtWidgets.QWidget()
    ui = Ui_View()
    ui.setupUi(View)
    View.show()
    sys.exit(app.exec_())

