# -*- coding: utf-8 -*-

# brew install pyqt6

import os
import random
import sys
import io
import shutil

import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import *

from matplotlib.backends.backend_qt import FigureCanvasQT

from .sup import Global, is_int, get_data_from_img_name, get_img_path_by_id


def exe_widget_in_QDialog(parent, widget: "QWidget"):
    msg = QDialog(parent)
    msg.setModal(True)

    grid = QGridLayout()

    exitButton = QPushButton("Close", msg)
    exitButton.clicked.connect(lambda: msg.close())

    grid.addWidget(widget, 0, 0, 1, 1)
    grid.addWidget(exitButton, 1, 0, 1, 1)

    msg.setLayout(grid)
    msg.exec()


class MainWidget(QWidget):

    def __init__(self):
        self.i_of_cur_i = 0
        self.cur_i = Global.images_indexes[self.i_of_cur_i]
        self.needed_keys = [
                        QtCore.Qt.Key.Key_Up, QtCore.Qt.Key.Key_Down, QtCore.Qt.Key.Key_Left, QtCore.Qt.Key.Key_Right,
                        QtCore.Qt.Key.Key_0, QtCore.Qt.Key.Key_1, QtCore.Qt.Key.Key_2, QtCore.Qt.Key.Key_3,
                        QtCore.Qt.Key.Key_4
                            ]
        super().__init__()

        self.__grid = QGridLayout(self)
        self.pic_label_1 = QLabel("")
        self.pic_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pic_label_2 = QLabel("")
        self.pic_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pic_label_3 = QLabel("")
        self.pic_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pic_label_4 = QLabel("")
        self.pic_label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pic = QLabel("", self)
        self.pic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pic_vote = QLabel("", self)
        self.update_image()

        self.goto_widget = QWidget()
        self.__goto_grid = QGridLayout(self.goto_widget)
        self.goto_widget.setMinimumSize(400, 200)
        self.goto_text = QLineEdit("Type image id to consider", self.goto_widget)
        self.goto_button = QPushButton("goto", self.goto_widget)
        self.goto_button.clicked.connect(lambda: self._goto_button_handler())
        self.__goto_grid.addWidget(self.goto_text, 0, 0, 1, 1)
        self.__goto_grid.addWidget(self.goto_button, 0, 1, 1, 1)
        self.goto_widget.setLayout(self.__goto_grid)
        self.goto_popup = QPushButton("goto", self)
        self.goto_popup.clicked.connect(lambda: exe_widget_in_QDialog(self, self.goto_widget))
        self.goto_popup.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        self.__grid.addWidget(self.pic_label_1, 0, 0, 1, 1)
        self.__grid.addWidget(self.pic_label_2, 0, 1, 1, 1)
        self.__grid.addWidget(self.pic_label_3, 0, 2, 1, 1)
        self.__grid.addWidget(self.pic_label_4, 0, 3, 1, 1)
        self.__grid.addWidget(self.pic, 1, 0, 1, 2)
        self.__grid.addWidget(self.pic_vote, 1, 2, 1, 2)
        self.__grid.addWidget(self.goto_popup, 2, 3, 1, 1)

        self.setLayout(self.__grid)

    def cur_move(self, moved: int):
        self.i_of_cur_i += moved
        if self.i_of_cur_i < 0:
            self.i_of_cur_i = 0
        if self.i_of_cur_i >= Global.images_indexes_len:
            self.i_of_cur_i = Global.images_indexes_len-1
        self.cur_i = Global.images_indexes[self.i_of_cur_i]

    def update_image(self):
        image_path = Global.images[self.cur_i]
        pixmap = QtGui.QPixmap(image_path)
        self.pic.setPixmap(pixmap)
        self.pic.update()

        image_data = get_data_from_img_name(image_path)
        real, pred, p_of_0, p_of_1, p_of_2, p_of_3, p_of_4 = image_data
        ps = [p_of_0, p_of_1, p_of_2, p_of_3, p_of_4]

        fig = plt.figure(figsize=(7, 4))
        plt.bar([0, 1, 2, 3, 4], ps, # color='maroon',
                    width=0.4)
        plt.xlabel("Class")
        plt.ylabel("Opinion on probability")
        plt.title(f"Real={real}, pred={pred}, probabilities={ps}. ")

        bio = io.BytesIO()
        plt.savefig(bio, dpi=75, format="png", transparent=True)
        # pixmap = QtGui.QPixmap(bio)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(bio.getbuffer().tobytes(), format="png")
        self.pic_vote.setPixmap(pixmap)
        self.pic_vote.update()
        plt.close()

        process_procent = f"{self.i_of_cur_i}/{Global.images_indexes_len} \n{round(self.i_of_cur_i/Global.images_indexes_len*100, 2)} %"
        self.pic_label_1.setText(f"{process_procent}")
        self.pic_label_2.setText(f"ID: \n{self.cur_i}")
        self.pic_label_3.setText(f"Real: \n{real}")
        self.pic_label_4.setText(f"Predict: \n{pred}")
        self.pic_label_1.update(), self.pic_label_2.update(), self.pic_label_3.update(), self.pic_label_4.update()

    def key_pressed(self, event):
        # super().keyPressEvent(event)
        if event.key() in self.needed_keys:
            if event.key() == QtCore.Qt.Key.Key_Left:
                cur_before = self.cur_i
                self.cur_move(-1)
                cur_after = self.cur_i
                if cur_before != cur_after:
                    img_path = get_img_path_by_id(self.cur_i, Global.output_dir)
                    if img_path is not None:
                        os.unlink(img_path)
            if event.key() in [QtCore.Qt.Key.Key_Up, QtCore.Qt.Key.Key_Down]:
                this_img_path = Global.images[self.cur_i]
                this_img_meta = Global.image_meta[f"{self.cur_i}"]
                new_class = None
                if event.key() == QtCore.Qt.Key.Key_Down:
                    new_class = this_img_meta["real"]
                if event.key() == QtCore.Qt.Key.Key_Up:
                    new_class = this_img_meta["pred"]
                file_out_path = os.path.join(Global.output_dir, f"{new_class}/{self.cur_i}.png")
                shutil.copyfile(this_img_path, file_out_path)
                self.cur_move(1)
            if event.key() in [QtCore.Qt.Key.Key_0, QtCore.Qt.Key.Key_1, QtCore.Qt.Key.Key_2,
                               QtCore.Qt.Key.Key_3, QtCore.Qt.Key.Key_4]:
                this_img_path = Global.images[self.cur_i]
                new_class = None
                if event.key() == QtCore.Qt.Key.Key_0:
                    new_class = 0
                if event.key() == QtCore.Qt.Key.Key_1:
                    new_class = 1
                if event.key() == QtCore.Qt.Key.Key_2:
                    new_class = 2
                if event.key() == QtCore.Qt.Key.Key_3:
                    new_class = 3
                if event.key() == QtCore.Qt.Key.Key_4:
                    new_class = 4
                file_out_path = os.path.join(Global.output_dir, f"{new_class}/{self.cur_i}.png")
                shutil.copyfile(this_img_path, file_out_path)
                self.cur_move(1)
            if event.key() in [QtCore.Qt.Key.Key_Right]:
                self.cur_move(1)

            self.update_image()

    def _goto_button_handler(self):
        text = self.goto_text.text()
        if not is_int(text):
            self.goto_text.setText(f"{text} is not number")
            self.goto_text.update()
            return
        img_id = int(text)
        if img_id not in Global.images_indexes:
            self.goto_text.setText(f"{text}   No such image to consider with id={img_id}")
            self.goto_text.update()
            return
        self.cur_move(-Global.images_indexes_len*2)
        while self.cur_i != img_id:
            self.cur_move(1)
        self.update_image()


class MainWidgetMain(QMainWindow):

    def __init__(self, parent=None):
        super(MainWidgetMain, self).__init__(parent)
        self.setWindowTitle("My Window")
        icon_path = os.path.join(Global.root, "imgs/ico.png")
        self.setWindowIcon(QtGui.QIcon(icon_path))

        self.mw = MainWidget()
        self.setCentralWidget(self.mw)

        self.setGeometry(250, 250, 280, 500)
        self.show()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.mw.key_pressed(event)


def entry_point():
    app = QApplication([])
    app.setStyleSheet("QLabel{font-size: 18pt;}")
    # app.setStyle("Fusion") # https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets
    mwm = MainWidgetMain()
    sys.exit(app.exec())


def entry_point2():
    app = QApplication([])
    icon_path = os.path.join(Global.root, "imgs/ico.png")
    app.setWindowIcon(QtGui.QIcon(icon_path))
    window = MainWidget()
    # window.setWindowTitle("konciliation")
    window.setGeometry(250, 250, 280, 500)
    window.show()
    sys.exit(app.exec())
