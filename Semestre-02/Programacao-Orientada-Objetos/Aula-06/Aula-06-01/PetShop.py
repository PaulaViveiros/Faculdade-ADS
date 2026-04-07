class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal faz um som genérico")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"O {self.nome} está latindo: Au Au!")

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def emitir_som(self):
        print(f"O {self.nome} está miando: Miau!")


# --- TESTE NO VS CODE (A LOJA) ---
if __name__ == '__main__':
    # Teste do Cachorro
    rex = Cachorro("Rex", 3, "Poodle")
    rex.emitir_som() 
    print(vars(rex))

    print("-" * 50)

    # Teste do Gato
    mingau = Gato("Mingau", 2, "Branco")
    mingau.emitir_som()
    print(vars(mingau))