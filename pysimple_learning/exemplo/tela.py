import PySimpleGUI as sg

class Exemplo:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('My Window')],
                  [sg.In()],
                  [sg.In()],
                  [sg.Button('Go'), sg.Button('Exit'), sg.Cancel(), sg.OK()]
                 ]

        layout = [[sg.Sizer(0, 300), sg.Column([[sg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]

        self.__window = sg.Window('Deus', layout, margins=(0,0))

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

if __name__ == '__main__':
    daniel = Exemplo()
    daniel.open()