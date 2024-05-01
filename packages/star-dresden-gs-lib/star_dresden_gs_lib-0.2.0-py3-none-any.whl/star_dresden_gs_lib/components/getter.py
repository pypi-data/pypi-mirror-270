from typing import Callable

from PyQt6 import QtWidgets


class GetterWidget(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, button: QtWidgets.QPushButton = None,
                 text: QtWidgets.QLabel = None, execute_func: Callable = None, *args, **kwargs):
        """

        :param name: the name of the Widget
        :param endpoint: a Callable function for either the Endpoint
        :param button_pos: (optional)
        :param text_pos: (optional)
        :param execute_func: (optional) a custom function for the button press
        :param args: (optional)
        :param kwargs: (optional)
        """
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.name = name
        self._endpoint = endpoint

        self.button = button if button != None else QtWidgets.QPushButton('None')
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text if text != None else QtWidgets.QLabel('None')
        self.text.setText(name)

        self.last_data = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.text, 0, 1)

    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __execute(self):
        value = self._endpoint()
        self.last_data = value


class GetterWithParamWidget(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, input_field: QtWidgets.QLineEdit = None,
                 button: QtWidgets.QPushButton = None,
                 text: QtWidgets.QLabel = None, execute_func: Callable = None, *args, **kwargs):
        """

        :param name: the name of the Widget
        :param endpoint: a Callable function for either the Endpoint
        :param button_pos: (optional)
        :param text_pos: (optional)
        :param execute_func: (optional) a custom function for the button press
        :param args: (optional)
        :param kwargs: (optional)
        """
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.name = name
        self._endpoint = endpoint

        self.button = button if button != None else QtWidgets.QPushButton('None')
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text if text != None else QtWidgets.QLabel('None')
        self.text.setText(name)

        self.input_field = input_field if input_field != None else QtWidgets.QLineEdit("input")

        self.last_data = {}
        self.last_sent = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.input_field, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.text, 0, 2)

    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __execute(self):
        self.last_sent = self.input_field.text()
        value = self._endpoint()
        self.last_data = value

    def set_button_pos(self, x, y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)

    def set_text_pos(self, x, y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)

    def set_input_pos(self, x, y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)
