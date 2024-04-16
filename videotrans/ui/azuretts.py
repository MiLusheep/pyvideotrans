# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deepl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore,  QtWidgets
from videotrans.configure import config

class Ui_azurettsform(object):
    def setupUi(self, azurettsform):
        azurettsform.setObjectName("azurettsform")
        azurettsform.setWindowModality(QtCore.Qt.NonModal)
        azurettsform.resize(400, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(azurettsform.sizePolicy().hasHeightForWidth())
        azurettsform.setSizePolicy(sizePolicy)
        azurettsform.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(azurettsform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(azurettsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.speech_region = QtWidgets.QLineEdit(azurettsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speech_region.sizePolicy().hasHeightForWidth())
        self.speech_region.setSizePolicy(sizePolicy)
        self.speech_region.setMinimumSize(QtCore.QSize(210, 35))
        self.speech_region.setObjectName("speech_region")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speech_region)
        
        self.formLayout_22 = QtWidgets.QFormLayout()
        self.formLayout_22.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_22.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout_22.setObjectName("formLayout_22")
        self.label22 = QtWidgets.QLabel(azurettsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label22.sizePolicy().hasHeightForWidth())
        self.label22.setSizePolicy(sizePolicy)
        self.label22.setMinimumSize(QtCore.QSize(100, 35))
        self.label22.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label22.setObjectName("label22")
        self.formLayout_22.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label22)
        self.speech_key = QtWidgets.QLineEdit(azurettsform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speech_key.sizePolicy().hasHeightForWidth())
        self.speech_key.setSizePolicy(sizePolicy)
        self.speech_key.setMinimumSize(QtCore.QSize(210, 35))
        self.speech_key.setObjectName("speech_key")
        self.formLayout_22.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speech_key)
        
        
        self.verticalLayout.addLayout(self.formLayout_22)
        self.verticalLayout.addLayout(self.formLayout_2)
        
        
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.save = QtWidgets.QPushButton(azurettsform)
        self.save.setMinimumSize(QtCore.QSize(0, 35))
        self.save.setObjectName("save")
        self.verticalLayout_2.addWidget(self.save)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(azurettsform)
        QtCore.QMetaObject.connectSlotsByName(azurettsform)

    def retranslateUi(self, azurettsform):
        azurettsform.setWindowTitle("AzureTTS")
        self.label.setText( "区域URL" if config.defaulelang=='zh' else "SPEECH_REGION")
        self.label22.setText( "授权key" if config.defaulelang=='zh' else "SPEECH_KEY")
        self.save.setText('保存' if config.defaulelang=='zh' else "Save")
