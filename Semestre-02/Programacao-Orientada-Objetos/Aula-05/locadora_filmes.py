class Filme:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.status = 'disponível'

    def alugar(self):
        self.status = 'alugado'
        print(f"✅ O filme '{self.titulo}' foi alugado!")

    def devolver(self):
        self.status = 'disponível'
        print(f"🔄 O filme '{self.titulo}' foi devolvido e está disponível.")

    # NOVO MÉTODO: Apresentação do Filme
    def exibir_info(self):
        print("-" * 30)
        print(f"🎬 TÍTULO: {self.titulo}")
        print(f"🎭 GÊNERO: {self.genero}")
        print(f"📌 STATUS: {self.status}")
        print("-" * 30)

# --- TESTANDO TUDO ---
meu_filme = Filme('Ps I Love You', 'Romance')
meu_filme.exibir_info() # Mostra disponível

meu_filme.alugar()
meu_filme.exibir_info() # Mostra alugado