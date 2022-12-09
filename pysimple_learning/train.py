import PySimpleGUI as sg

'''
layout = [
            [sg.Text('Incluir novo Cliente')],
            [sg.Text('Nome', size=(15,1)), sg.InputText('')],
            [sg.Submit(), sg.Cancel()]
        ]

window = sg.Window('Cadastro de Clientes').Layout(layout)

button, values = window.Read()
'''

class ExemploView:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit') # Definição do esquema de Cores

        coluna1 = [[sg.Text('Coluna1', background_color='#d3dfda', justification='center', size=(10,1))],
                   [sg.Spin(values=('1','2','3'), initial_value='selecione', key='sp_spin1')],
                   [sg.Spin(values=('1','2','3'), initial_value='selecione', key='sp_spin2')],
                   [sg.Spin(values=('1','2','3'), initial_value='selecione', key='sp_spin3')]]

        layout = [[sg.Text('Todos os componentes em uma tela!', size=(30, 1), font=('Helvetica', 25))],
                  [sg.Text('Este é um texto e espaço para responder:')],
                  [sg.InputText('Texto de resposta', key='it_nome')],
                  [sg.Checkbox('Checkbox opção 1!', key='ck_opcao1'), sg.Checkbox('Checkbox opção 2!', default=True, key='ck_opcao2')],
                  [sg.Radio('Radio opção 1!', 'RD1', default=True, key='rd_opcao1'), sg.Radio('Radio opção 2!','RD1', key='rd_opcao2')],
                  [sg.Multiline(default_text='Texto padrão para o caso do usuário não digitar nada', size=(35, 3)),
                   sg.Multiline(default_text='Outra coluna com multiplas linhas', size=(35, 3))],
                  [sg.InputCombo(('Combobox 1', 'Combobox 2',), size=(20,3), key='cb_opcoes'),
                   sg.Slider(range=(1, 100), orientation='h', size=(34,20), default_value=85, key='sl_slider1')],
                  [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3), key='lb_itens'),
                   sg.Slider(range=(1, 100), orientation='v', size=(5 ,20), default_value=25, key='sl_slider2'),
                   sg.Slider(range=(1, 100), orientation='v', size=(5 ,20), default_value=25, key='sl_slider3'),
                   sg.Slider(range=(1, 100), orientation='v', size=(5 ,20), default_value=25, key='sl_slider4'),
                   sg.Column(coluna1, background_color='#d3dfda')], # Adicionando a coluna definida anteriormente
                  [sg.Text('_' * 80)], # Linha divisória
                  [sg.Text('Selecione uma pasta', size=(35, 1))],
                  [sg.Text('Pasta selecionada', size=(15, 1), auto_size_text=False, justification='right'),
                   sg.InputText('Pasta Default'), sg.FolderBrowse(key='fb_pasta_selecionada')],
                  [sg.Button('Gravar'), sg.Cancel('Cancelar')]
                  ]

        self.__window = sg.Window('Título da tela', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)


if __name__ == '__main__':
    daniel = ExemploView()
    daniel.open()