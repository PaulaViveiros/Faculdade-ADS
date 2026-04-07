# 🐾 Exercício de Herança: O Pet Shop da Paula

Este projeto foi o meu ponto de partida para entender como a **Programação Orientada a Objetos (POO)** organiza o mundo real em código. Aqui, explorei a hierarquia animal para praticar os pilares básicos da herança.

## 💡 O que eu pratiquei:

### 🧬 Herança Simples
Criei uma classe base chamada `Animal` que contém as características comuns (nome e idade). As classes `Cachorro` e `Gato` herdam essas informações, evitando a repetição de código.

### 🎭 Polimorfismo de Sobrescrita
Implementei o método `emitir_som()` de formas diferentes:
- Na classe **Cachorro**, o som é um "Au Au!".
- Na classe **Gato**, o som é um "Miau!".
Isso demonstra como objetos diferentes podem responder ao mesmo comando de formas específicas.

### 📞 Uso do `super()`
Utilizei o `super().__init__` para garantir que as classes filhas utilizem a lógica de "nascimento" da classe mãe, mantendo o código limpo e moderno.

## 🖥️ Como rodar o teste
O arquivo `petshop.py` contém um bloco de teste que cria instâncias do **Rex** (Cachorro) e do **Mingau** (Gato), exibindo os seus sons e os seus atributos via `vars()`.