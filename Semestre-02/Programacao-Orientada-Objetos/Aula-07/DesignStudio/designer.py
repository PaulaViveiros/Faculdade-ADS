class Designer:
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self, ferramenta_escolhida):
        print(f"👩‍💻 {self.nome} começou a trabalhar.")
        ferramenta_escolhida.usar() # Aqui a mágica da Associação acontece!