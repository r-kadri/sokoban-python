class Model:
    def __init__(self):
        self.view = None
        self.controller = None
        self.level, self.points = self.generate_level()

    def generate_level(self):
        return [
                   ["O", "O", "O", "X", "X", "X", "X", "O"],
                   ["O", "O", "O", "X", "O", "O", "X", "0"],
                   ["X", "X", "X", "X", "O", "C", "X", "X"],
                   ["X", "O", "J", "C", "O", "O", "O", "X"],
                   ["X", "O", "X", "X", "O", "O", "O", "X"],
                   ["X", "O", "O", "O", "X", "X", "O", "X"],
                   ["X", "O", "O", "O", "C", "O", "O", "X"],
                   ["X", "X", "X", "X", "X", "X", "X", "X"]
               ], [
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]
               ]

    def get_level(self):
        return self.level.copy()

    def get_matrix(self):
        return self.level.copy(), self.points.copy()

    def set_matrix(self, matrix):
        self.level = matrix
        self.view.update()

    def set_view(self, view):
        self.view = view
        self.view.update()
