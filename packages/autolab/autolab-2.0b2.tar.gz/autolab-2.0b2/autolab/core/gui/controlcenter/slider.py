# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:23:51 2023

@author: jonathan
"""
from typing import Any

import numpy as np
from qtpy import QtCore, QtWidgets, QtGui

from ..icons import icons
from ..GUI_utilities import get_font_size, setLineEditBackground
from ... import config


class Slider(QtWidgets.QMainWindow):

    def __init__(self, item: QtWidgets.QTreeWidgetItem):
        """ https://stackoverflow.com/questions/61717896/pyqt5-qslider-is-off-by-one-depending-on-which-direction-the-slider-is-moved """
        QtWidgets.QMainWindow.__init__(self)
        self.item = item
        self.resize(self.minimumSizeHint())
        self.setWindowTitle(self.item.variable.address())
        self.setWindowIcon(QtGui.QIcon(icons['slider']))

        # Load configuration
        control_center_config = config.get_control_center_config()
        self.precision = int(control_center_config['precision'])

        self._font_size = get_font_size() + 1

        # Slider
        self.slider_instantaneous = True
        self.true_min = self.item.variable.type(0)
        self.true_max = self.item.variable.type(10)
        self.true_step = self.item.variable.type(1)

        centralWidget = QtWidgets.QWidget()
        layoutWindow = QtWidgets.QVBoxLayout()
        layoutTopValue = QtWidgets.QHBoxLayout()
        layoutSlider = QtWidgets.QHBoxLayout()
        layoutBottomValues = QtWidgets.QHBoxLayout()

        centralWidget.setLayout(layoutWindow)
        layoutWindow.addLayout(layoutTopValue)
        layoutWindow.addLayout(layoutSlider)
        layoutWindow.addLayout(layoutBottomValues)

        self.instantCheckBox = QtWidgets.QCheckBox()
        self.instantCheckBox.setToolTip("True: Changes instantaneously the value.\nFalse: Changes the value when click released.")
        self.instantCheckBox.setCheckState(QtCore.Qt.Checked)
        self.instantCheckBox.stateChanged.connect(self.instantChanged)

        layoutTopValue.addWidget(QtWidgets.QLabel("Instant"))
        layoutTopValue.addWidget(self.instantCheckBox)

        self.valueWidget = QtWidgets.QLineEdit()
        self.valueWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.valueWidget.setReadOnly(True)
        self.valueWidget.setText(f'{self.true_min}')
        setLineEditBackground(self.valueWidget, 'edited', self._font_size)

        layoutTopValue.addStretch()
        layoutTopValue.addWidget(QtWidgets.QLabel("Value"))
        layoutTopValue.addWidget(self.valueWidget)
        layoutTopValue.addStretch()
        layoutTopValue.addSpacing(40)

        self.sliderWidget = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sliderWidget.setValue(0)
        self.sliderWidget.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderWidget.valueChanged.connect(self.valueChanged)
        self.sliderWidget.sliderReleased.connect(self.sliderReleased)
        self.sliderWidget.setStyle(ProxyStyle())

        button_minus = QtWidgets.QToolButton()
        button_minus.setArrowType(QtCore.Qt.LeftArrow)
        button_minus.clicked.connect(self.minusClicked)

        button_plus = QtWidgets.QToolButton()
        button_plus.setArrowType(QtCore.Qt.RightArrow)
        button_plus.clicked.connect(self.plusClicked)

        layoutSlider.addWidget(button_minus)
        layoutSlider.addWidget(self.sliderWidget)
        layoutSlider.addWidget(button_plus)

        self.minWidget = QtWidgets.QLineEdit()
        self.minWidget.setAlignment(QtCore.Qt.AlignLeft)
        self.minWidget.returnPressed.connect(self.minWidgetValueChanged)
        self.minWidget.textEdited.connect(lambda: setLineEditBackground(
            self.minWidget, 'edited', self._font_size))

        layoutBottomValues.addWidget(QtWidgets.QLabel("Min"))
        layoutBottomValues.addWidget(self.minWidget)
        layoutBottomValues.addSpacing(10)
        layoutBottomValues.addStretch()

        self.stepWidget = QtWidgets.QLineEdit()
        self.stepWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.stepWidget.returnPressed.connect(self.stepWidgetValueChanged)
        self.stepWidget.textEdited.connect(lambda: setLineEditBackground(
            self.stepWidget, 'edited', self._font_size))

        layoutBottomValues.addWidget(QtWidgets.QLabel("Step"))
        layoutBottomValues.addWidget(self.stepWidget)
        layoutBottomValues.addStretch()
        layoutBottomValues.addSpacing(10)

        self.maxWidget = QtWidgets.QLineEdit()
        self.maxWidget.setAlignment(QtCore.Qt.AlignRight)
        self.maxWidget.returnPressed.connect(self.maxWidgetValueChanged)
        self.maxWidget.textEdited.connect(lambda: setLineEditBackground(
            self.maxWidget, 'edited', self._font_size))

        layoutBottomValues.addWidget(QtWidgets.QLabel("Max"))
        layoutBottomValues.addWidget(self.maxWidget)

        self.setCentralWidget(centralWidget)

        self.updateStep()

        self.resize(self.minimumSizeHint())
        self.show()

    def updateStep(self):

        slider_points = 1 + int(
            np.floor((self.true_max - self.true_min) / self.true_step))
        self.true_max = self.item.variable.type(
            self.true_step*(slider_points - 1) + self.true_min)

        self.minWidget.setText(f'{self.true_min}')
        setLineEditBackground(self.minWidget, 'synced', self._font_size)
        self.maxWidget.setText(f'{self.true_max}')
        setLineEditBackground(self.maxWidget, 'synced', self._font_size)
        self.stepWidget.setText(f'{self.true_step}')
        setLineEditBackground(self.stepWidget, 'synced', self._font_size)

        temp = self.slider_instantaneous
        self.slider_instantaneous = False
        self.sliderWidget.setMinimum(0)
        self.sliderWidget.setSingleStep(1)
        self.sliderWidget.setTickInterval(1)
        self.sliderWidget.setMaximum(slider_points - 1)
        self.slider_instantaneous = temp

    def updateTrueValue(self, old_true_value: Any):

        new_cursor_step = round(
            (old_true_value - self.true_min) / self.true_step)
        slider_points = 1 + int(
            np.floor((self.true_max - self.true_min) / self.true_step))
        if new_cursor_step > (slider_points - 1):
            new_cursor_step = slider_points - 1
        elif new_cursor_step < 0:
            new_cursor_step = 0

        temp = self.slider_instantaneous
        self.slider_instantaneous = False
        self.sliderWidget.setSliderPosition(new_cursor_step)
        self.slider_instantaneous = temp

        true_value = self.item.variable.type(
            new_cursor_step*self.true_step + self.true_min)
        self.valueWidget.setText(f'{true_value:.{self.precision}g}')
        setLineEditBackground(self.valueWidget, 'edited', self._font_size)

    def stepWidgetValueChanged(self):

        old_true_value = self.item.variable.type(self.valueWidget.text())
        try:
            true_step = self.item.variable.type(self.stepWidget.text())
            assert true_step != 0, "Can't have step=0"
            self.true_step = true_step
        except Exception as e:
            self.item.gui.setStatus(f"Variable {self.item.variable.name}: {e}",
                                    10000, False)
            return None
        self.updateStep()
        self.updateTrueValue(old_true_value)

    def minWidgetValueChanged(self):

        old_true_value = self.item.variable.type(self.valueWidget.text())
        try:
            self.true_min = self.item.variable.type(self.minWidget.text())
        except Exception as e:
            self.item.gui.setStatus(f"Variable {self.item.variable.name}: {e}",
                                    10000, False)
            return None
        self.updateStep()
        self.updateTrueValue(old_true_value)

    def maxWidgetValueChanged(self):

        old_true_value = self.item.variable.type(self.valueWidget.text())
        try:
            self.true_max = self.item.variable.type(self.maxWidget.text())
        except Exception as e:
            self.item.gui.setStatus(f"Variable {self.item.variable.name}: {e}",
                                    10000, False)
            return None
        self.updateStep()
        self.updateTrueValue(old_true_value)

    def sliderReleased(self):
        """ Do something when the cursor is released """
        value = self.sliderWidget.value()
        true_value = self.item.variable.type(
            value*self.true_step + self.true_min)
        self.valueWidget.setText(f'{true_value:.{self.precision}g}')
        setLineEditBackground(self.valueWidget, 'synced', self._font_size)
        self.item.gui.threadManager.start(
            self.item, 'write', value=true_value)
        self.updateStep()

    def valueChanged(self, value: Any):
        """ Do something with the slider value when the cursor is moved """
        true_value = self.item.variable.type(
            value*self.true_step + self.true_min)
        self.valueWidget.setText(f'{true_value:.{self.precision}g}')
        if self.slider_instantaneous:
            setLineEditBackground(self.valueWidget, 'synced', self._font_size)
            self.item.gui.threadManager.start(
                self.item, 'write', value=true_value)
        else:
            setLineEditBackground(self.valueWidget,'edited', self._font_size)
        # self.updateStep()  # Don't use it here, infinite loop leading to crash if set min > max

    def instantChanged(self, value):
        self.slider_instantaneous = self.instantCheckBox.isChecked()

    def minusClicked(self):
        self.sliderWidget.setSliderPosition(self.sliderWidget.value()-1)
        if not self.slider_instantaneous: self.sliderReleased()

    def plusClicked(self):
        self.sliderWidget.setSliderPosition(self.sliderWidget.value()+1)
        if not self.slider_instantaneous: self.sliderReleased()

    def closeEvent(self, event):
        """ This function does some steps before the window is really killed """
        self.item.clearSlider()



class ProxyStyle(QtWidgets.QProxyStyle):
    """ https://stackoverflow.com/questions/67299834/pyqt-slider-not-come-to-a-specific-location-where-i-click-but-move-to-a-certain """
    def styleHint(self, hint, opt=None, widget=None, returnData=None):
        res = super().styleHint(hint, opt, widget, returnData)
        if hint == self.SH_Slider_AbsoluteSetButtons:
            res |= QtCore.Qt.LeftButton
        return res
