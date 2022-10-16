class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        super().__init__('O elevador esta no último andar!')