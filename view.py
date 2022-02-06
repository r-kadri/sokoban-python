from model import Model
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chemins = {"X": "source/image/mur.png", "O": "source/image/sol.png", "C": "source/image/caisseM.png",
                        "J": "source/image/crash.png", "R": "source/image/caisseV.png", 1: "source/image/pomme.png"}
        self.setFixedSize(512, 512)
        self.setWindowTitle("Sokoban PyQt5")
        self.model = Model()
        self.controller = None
        self.__window = Pattern()
        self.__window.set_model(self.model)
        self.setCentralWidget(self.__window)
        self.show()

    def set_model(self, model):
        self.model = model

    def set_controller(self, controller):
        self.controller = controller

    def update_view(self):
        self.update()

    def keyPressEvent(self, event):
        if not self.controller.is_finished():
            if event.key() == Qt.Key_Up:
                self.controller.move_player(0)

            elif event.key() == Qt.Key_Down:
                self.controller.move_player(2)

            elif event.key() == Qt.Key_Right:
                self.controller.move_player(1)

            elif event.key() == Qt.Key_Left:
                self.controller.move_player(3)

            self.__window = Pattern()
            self.__window.set_model(self.model)
            self.setCentralWidget(self.__window)

    def get_case(self, i, j):
        matrix, points = self.model.get_matrix()
        k = matrix[j][i]
        if k == "J":
            k = "O"
        return self.chemins.get(k)

    def caisse_verte(self, lig, col):
        matrixJeu, matrixPoints = self.model.get_matrix()
        return matrixJeu[lig][col] == "C" and matrixPoints[lig][col] == 1

    def paintEvent(self, event):
        matrix, points = self.model.get_matrix()
        painter = QPainter(self)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[j][i] != "X" and matrix[j][i] != "O":
                    if not self.caisse_verte(j, i):
                        k = self.get_case(i, j)
                        img = QPixmap(k)
                        painter.drawPixmap(64 * i, 64 * j, img)

                    if matrix[j][i] == "J":
                        k = self.chemins.get("J")
                        img = QPixmap(k)
                        painter.drawPixmap(64 * i + 14, 64 * j + 2, img)

                    if points[j][i] == 1 and not self.caisse_verte(j, i):
                        img = QPixmap(self.chemins.get(1))
                        painter.drawPixmap(64 * i + 16, 64 * j + 16, img)

                    if self.caisse_verte(j, i):
                        img = QPixmap(self.chemins.get("R"))
                        painter.drawPixmap(64 * i, 64 * j, img)


class Pattern(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(512, 512)
        self.move(0, 0)
        self.model = None
        self.chemins = {"X": "source/image/mur.png", "O": "source/image/sol.png", "C": "source/image/caisseM.png",
                        "J": "source/image/crash.png", "R": "source/image/caisseV.png", 1: "source/image/pomme.png"}

    def set_model(self, model):
        self.model = model

    def update_dessin(self):
        self.update()

    def get_case(self, i, j):
        matrix, points = self.model.get_matrix()
        k = matrix[j][i]
        if k == "J":
            k = "O"
        return self.chemins.get(k)

    def caisse_verte(self, lig, col):
        matrixJeu, matrixPoints = self.model.get_matrix()
        return matrixJeu[lig][col] == "C" and matrixPoints[lig][col] == 1

    def paintEvent(self, event):
        matrix, points = self.model.get_matrix()
        painter = QPainter(self)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                img = QPixmap(self.chemins.get("O"))
                painter.drawPixmap(64 * i, 64 * j, img)
                if not self.caisse_verte(j, i):
                    k = self.get_case(i, j)
                    img = QPixmap(k)
                    painter.drawPixmap(64 * i, 64 * j, img)

                if points[j][i] == 1 and not self.caisse_verte(j, i):
                    img = QPixmap(self.chemins.get(1))
                    painter.drawPixmap(64 * i + 16, 64 * j + 16, img)

                if matrix[j][i] == "J":
                    k = self.chemins.get("J")
                    img = QPixmap(k)
                    painter.drawPixmap(64 * i + 14, 64 * j + 2, img)

                if self.caisse_verte(j, i):
                    img = QPixmap(self.chemins.get("R"))
                    painter.drawPixmap(64 * i, 64 * j, img)
