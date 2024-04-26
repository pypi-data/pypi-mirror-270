# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mw4/gui/widgets/message.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MessageDialog.sizePolicy().hasHeightForWidth())
        MessageDialog.setSizePolicy(sizePolicy)
        MessageDialog.setMinimumSize(QtCore.QSize(800, 285))
        MessageDialog.setMaximumSize(QtCore.QSize(800, 1200))
        MessageDialog.setSizeIncrement(QtCore.QSize(10, 10))
        MessageDialog.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MessageDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageDialog)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear = QtWidgets.QPushButton(MessageDialog)
        self.clear.setMinimumSize(QtCore.QSize(100, 25))
        self.clear.setMaximumSize(QtCore.QSize(100, 25))
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(MessageDialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.messageTable = QtWidgets.QTableWidget(MessageDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.messageTable.setFont(font)
        self.messageTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.messageTable.setLineWidth(0)
        self.messageTable.setAutoScrollMargin(0)
        self.messageTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.messageTable.setTabKeyNavigation(False)
        self.messageTable.setProperty("showDropIndicator", False)
        self.messageTable.setDragDropOverwriteMode(False)
        self.messageTable.setAlternatingRowColors(False)
        self.messageTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.messageTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.messageTable.setShowGrid(False)
        self.messageTable.setGridStyle(QtCore.Qt.DotLine)
        self.messageTable.setWordWrap(True)
        self.messageTable.setCornerButtonEnabled(False)
        self.messageTable.setColumnCount(0)
        self.messageTable.setObjectName("messageTable")
        self.messageTable.setRowCount(0)
        self.messageTable.horizontalHeader().setCascadingSectionResizes(True)
        self.messageTable.horizontalHeader().setDefaultSectionSize(80)
        self.messageTable.horizontalHeader().setHighlightSections(True)
        self.messageTable.horizontalHeader().setMinimumSectionSize(5)
        self.messageTable.horizontalHeader().setSortIndicatorShown(False)
        self.messageTable.horizontalHeader().setStretchLastSection(True)
        self.messageTable.verticalHeader().setVisible(False)
        self.messageTable.verticalHeader().setCascadingSectionResizes(True)
        self.messageTable.verticalHeader().setDefaultSectionSize(10)
        self.messageTable.verticalHeader().setHighlightSections(True)
        self.messageTable.verticalHeader().setMinimumSectionSize(1)
        self.messageTable.verticalHeader().setSortIndicatorShown(False)
        self.messageTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.messageTable)

        self.retranslateUi(MessageDialog)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

    def retranslateUi(self, MessageDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageDialog.setWindowTitle(_translate("MessageDialog", "Messages"))
        self.clear.setText(_translate("MessageDialog", "Clear window"))
        self.messageTable.setToolTip(_translate("MessageDialog", "<html><head/><body><p>Messages</p></body></html>"))
        self.messageTable.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageDialog = QtWidgets.QWidget()
    ui = Ui_MessageDialog()
    ui.setupUi(MessageDialog)
    MessageDialog.show()
    sys.exit(app.exec_())
