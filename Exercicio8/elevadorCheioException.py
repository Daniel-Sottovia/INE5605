class ElevadorCheioException(Exception):
    def __init__(self):
        super().__init__("O elevador esta cheio!")


if __name__ == '__main__':
    print(ElevadorCheioException())
