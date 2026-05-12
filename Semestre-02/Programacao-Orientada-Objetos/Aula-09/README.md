# Práticas de TDD e Tratamento de Exceções 🚀

Este projeto foi desenvolvido como parte dos estudos de **Programação Orientada a Objetos** (Semestre 02 - ADS). O objetivo principal é aplicar conceitos de Test-Driven Development (TDD) e o tratamento robusto de exceções em Python utilizando o framework `pytest`.

## 📚 Conceitos Aplicados

### 1. TDD (Test Driven Development)
Seguimos o ciclo de desenvolvimento orientado a testes:
- **Red**: Criamos um teste que falha propositalmente (fase de erro).
- **Green**: Escrevemos o código mínimo necessário para o teste passar.
- **Refactor**: Melhoramos o código mantendo a integridade dos testes.

### 2. Padrão xUnit (AAA / GWT)
Os testes foram estruturados seguindo os padrões:
- **Arrange / Given**: Preparação do cenário e dados.
- **Act / When**: Execução da funcionalidade ou método.
- **Assert / Then**: Verificação se o resultado obtido é o esperado.

### 3. Tratamento de Exceções
Implementamos o gerenciamento de erros para garantir a resiliência do software:
- **Lançamento (`raise`)**: A lógica de negócio (`jogo.py`) interrompe a execução caso regras semânticas sejam violadas (ex: idade negativa).
- **Captura (`try/except`)**: O ponto de entrada da aplicação (`app.py`) captura a exceção e fornece um feedback amigável ao usuário, evitando o encerramento inesperado do programa.

## 🛠️ Tecnologias Utilizadas
- **Python 3.14+**
- **Pytest**: Framework para automação de testes unitários.
- **Venv**: Ambiente virtual para isolamento de dependências.

## ⚙️ Como Rodar o Projeto

1. **Ative o ambiente virtual:**
   ```bash
   .\.venv\Scripts\activate

2. Execute os testes:

Bash
pytest -v

3. Execute a aplicação:

Bash
python app.py

## 📂 Estrutura de Pastas
- `codigo/`: Contém a lógica de negócio e funções principais.
- `tests/`: Contém os scripts de testes automatizados.
- `app.py`: Interface de interação com o usuário final.