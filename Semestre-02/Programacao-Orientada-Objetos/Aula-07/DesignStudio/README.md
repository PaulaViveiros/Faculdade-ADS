# 🎨 Design Studio - Praticando POO e Modularização

Este projeto foi desenvolvido para consolidar conceitos fundamentais de Programação Orientada a Objetos (POO) em Python, focando em organização e escalabilidade.

## 🧠 Conceitos Aplicados

### 1. Modularização
Em vez de um arquivo único, o projeto foi dividido em módulos (`designer.py` e `ferramenta.py`). Isso facilita a manutenção e permite que cada classe viva em seu próprio "espaço".

### 2. Associação de Objetos
Demonstramos como um objeto (Designer) pode interagir com outro objeto (Ferramenta) através de métodos, sem a necessidade de herança. É a representação real de "alguém usa algo".

### 3. SRP (Single Responsibility Principle)
Cada classe tem uma única responsabilidade. A `Ferramenta` cuida de suas funções técnicas, enquanto o `Designer` cuida da lógica de trabalho.

## 🛠️ Estrutura do Projeto
- `ferramenta.py`: Classe base para ferramentas de design.
- `designer.py`: Classe que gerencia as ações do profissional.
- `main.py`: Ponto de entrada que orquestra a interação entre os módulos.