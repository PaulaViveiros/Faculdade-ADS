# 🏦 Sistema Bancário em Python - Praticando POO

Este repositório contém uma implementação prática de um sistema de contas bancárias, desenvolvido para consolidar os conceitos fundamentais da **Programação Orientada a Objetos (POO)** em Python, como parte dos meus estudos em **Análise e Desenvolvimento de Sistemas (ADS)**.

## 🚀 Conceitos de POO Aplicados

Neste projeto, foquei na aplicação dos quatro pilares da POO:

### 🧬 1. Herança
Utilizei a herança para criar uma hierarquia entre a `ContaBancaria` (Classe Mãe) e a `ContaInvestimento` (Classe Filha), permitindo a reutilização de atributos como `titular` e comportamentos como `depositar`.

### 🎭 2. Polimorfismo de Sobrescrita
Implementei o polimorfismo ao redefinir o método `sacar()` na classe `ContaInvestimento`. Embora o nome do método seja o mesmo da classe mãe, ele possui um comportamento específico: a aplicação de uma taxa de serviço sobre o valor do saque.



### 🔒 3. Encapsulamento
O saldo da conta foi definido como um atributo privado (`__saldo`), garantindo que o valor não seja alterado diretamente por agentes externos. O acesso e a modificação do saldo ocorrem exclusivamente através dos métodos `sacar()` e `depositar()`.

### 📞 4. Uso da função `super()`
Utilizei a função `super()` para invocar o construtor (`__init__`) da classe mãe e para delegar a execução final do saque, permitindo que a classe filha adicione sua lógica de taxas sem precisar acessar diretamente o saldo privado.

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.10+
* **Editor:** Visual Studio Code (VS Code)
* **Versionamento:** Git & GitHub

## 📖 Como visualizar os testes

O código utiliza o bloco `if __name__ == '__main__':` para executar simulações de:
1. Saque em conta comum (sem taxas).
2. Saque em conta investimento (com aplicação automática de taxas).
3. Verificação de saldo insuficiente (lógica de proteção).