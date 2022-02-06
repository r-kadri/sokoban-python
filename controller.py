class Controller:
    def __init__(self):
        self.__model = None
        self.__view = None
        self.__finished = False

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    def move_player(self, direction):
        plateau = self.model.get_level()
        x = 0
        y = 0
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau[i][j] == "J":
                    x = i
                    y = j
                    break
        x_cible = x
        y_cible = y
        x_move_box = x
        y_move_box = y

        if direction == 0:
            x_cible += -1
            x_move_box += -2

        elif direction == 1:
            y_cible += 1
            y_move_box += 2

        elif direction == 2:
            x_cible += 1
            x_move_box += 2

        elif direction == 3:
            y_cible += -1
            y_move_box += -2

        if direction in [0, 1, 2, 3]:
            if self.passage_possible(x, y, x_cible, y_cible):
                if plateau[x_cible][y_cible] == "C":
                    if self.passage_possible(x_cible, y_cible, x_move_box, y_move_box):
                        self.move_box(x_cible, y_cible, x_move_box, y_move_box)
                        plateau[x][y] = "O"
                        plateau[x_cible][y_cible] = "J"
                else:
                    plateau[x][y] = "O"
                    plateau[x_cible][y_cible] = "J"

        self.model.set_matrix(plateau)

    def move_box(self, xCaisse, yCaisse, xCible, yCible):
        level = self.model.get_level()
        if self.passage_possible(xCaisse, yCaisse, xCible, yCible):
            level[xCible][yCible] = "C"
            level[xCaisse][yCaisse] = "O"
        self.model.set_matrix(self)

    def passage_possible(self, ligneCase1, colonneCase1, ligneCase2, colonneCase2):
        matrixJeu, matrixPoint = self.model.get_matrix()
        if matrixJeu[ligneCase1][colonneCase1] == "J":
            if matrixJeu[ligneCase2][colonneCase2] == "O" or matrixJeu[ligneCase2][colonneCase2] == "C":
                return True

        elif matrixJeu[ligneCase1][colonneCase1] == "C":
            if matrixJeu[ligneCase2][colonneCase2] == "O":
                return True
        return False

    def is_finished(self):
        level, points = self.model.get_matrix()
        for i in range(len(points)):
            for j in range(len(points[i])):
                if points[i][j] == 1 and level[i][j] != "C":
                    return False
        return True
