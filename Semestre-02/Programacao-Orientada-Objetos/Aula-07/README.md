# 📡 Sistema de Notificações - Herança Múltipla e MRO

Este projeto explora o conceito de **Herança Múltipla** em Python, utilizando um sistema de alertas urgentes que precisam disparar notificações por diferentes canais simultaneamente.

## 🏗️ Duas Formas de Implementação

Neste exercício, analisei duas abordagens para resolver o problema de disparar múltiplos métodos em classes independentes:

### 1. Chamada Direta (`Classe.metodo(self)`)
Nesta versão, chamo explicitamente cada classe pai pelo nome dentro da classe filha.
- **Quando usar:** Quando as classes herdadas são ferramentas independentes e você quer garantir que todas executem sua tarefa.
- **Vantagem:** Controle total da ordem de execução e clareza visual.
- **Desvantagem:** Cria um acoplamento forte (se o nome da classe mãe mudar, você precisa mudar o código da filha).
- **Veredito:** É a forma mais eficiente para este sistema, pois garante o envio tanto por E-mail quanto por SMS sem quebras.

### 2. Uso do `super()` e o GPS do Python (MRO)
Nesta versão, deixo o Python decidir a ordem através do **Method Resolution Order (MRO)**.
- **Quando usar:** Em sistemas complexos e integrados (frameworks), para evitar o "Problema do Diamante".
- **Vantagem:** Segue o padrão oficial da linguagem e evita redundâncias em hierarquias complexas.
- **Desvantagem:** Exige que **todas** as classes da cadeia usem `super()`, caso contrário, a execução para na primeira classe encontrada.

> [!IMPORTANT]
> **Aprendizado Técnico sobre o Erro:**
> Durante os testes com `super()`, identifiquei um `AttributeError`. Isso ocorreu porque a última classe da cadeia MRO tentou propagar o método para a classe base `object`, que não possui o método `enviar`. Isso demonstra que o uso de `super()` exige uma hierarquia onde todas as classes colaboram ou possuem uma base comum.
>
> **Conclusão:** Percebi que usar `super()` em classes totalmente independentes (como Email e SMS) pode criar uma dependência desnecessária. A **Chamada Direta** mostrou-se mais robusta aqui por garantir a execução de todas as ferramentas sem depender da "corrente" do MRO.

## 🧪 O que aprendi
Aprendi que o `super()` não é apenas um "atalho para a mãe", mas um comando para o Python seguir para o próximo item da lista de prioridades. Para verificar essa ordem exata e entender o caminho que o interpretador faz, utilizei o comando:
```python
print(Classe.mro())