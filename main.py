import sys
from PyQt5.QtWidgets import QApplication
from view import View
from model import Model
from controller import Controller

app = QApplication(sys.argv)

model = Model()
view = View()
controller = Controller()

model.set_view(view)
view.set_model(model)
view.set_controller(controller)
controller.set_view(view)
controller.set_model(model)

sys.exit(app.exec_())
