
# Meu Portfólio de Estudos - Python 🐍

Este repositório registra minha evolução na faculdade de ADS e no curso de Python do Guanabara.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.14
* **Editor:** VS Code
* **Versionamento:** Git & GitHub

---

## Meu Primeiro Projeto Python 🐍✨

Olá! Este é o meu primeiro repositório documentado. Aqui estou registrando minha jornada de aprendizado em Python.

## 🚀 Desafios e Aprendizados:

### 1. Conversor de Emojis
* **Manipulação de Módulos:** Aprendi a instalar bibliotecas externas usando o `pip`.
* **Biblioteca Emoji:** Usei o módulo `emoji` para deixar as saídas do terminal mais divertidas.
* **Ambiente de Desenvolvimento:** Configurei o Git, o VS Code e aprendi a resolver conflitos de variáveis de ambiente no Windows.

---

### 2.🃏 Analisador de Quadrinhos (Strings)
Neste exercício, explorei a fundo como o Python trata textos e espaços.

**O que pratiquei:**
* **Tratamento de Strings:** Usei `.strip()` para limpeza e ignorar espaços inúteis.
* **Transformação de Texto:** Apliquei `.upper()`, `.lower()` e `.title()` para padronizar nomes.
* **Manipulação de Espaços:** Aprendi a contar apenas letras usando `len()` combinado com `.count()` e também a técnica de remoção com `.replace(' ', '')`.
* **Listas:** Usei o `.split()` (variável `separa`)

---

### 3.🧮 Decomposição Matemática de Números
Neste desafio, aprendi a separar as casas decimais (unidade, dezena, centena e milhar) de um número inteiro sem precisar transformá-lo em texto.

**O que pratiquei:**
* **Divisão Inteira (`//`):** Utilizada para "cortar" os números e mover as casas decimais.
* **Módulo (`%`):** Utilizado para isolar o resto da divisão por 10 e obter o algarismo desejado.
* **Resiliência do Código:** Aprendi que a matemática evita erros de índice (`IndexError`) que aconteceriam se tratássemos números pequenos como texto.

---

### 4.🚀 Evolução de Lógica

### 🏙️ Verificador de Cidades (Lógica de Lista)
Melhorei a lógica proposta em aula para verificar se o nome de uma cidade começa com "Santo".
* **Diferencial:** Uso do `.split()` em vez de fatiamento `[:5]`, evitando que "Santos" seja validado incorretamente.

---

### 5.🔍 Busca Dinâmica vs. Busca Fixa (Verificador de Sobrenomes)
Embora ambos tratem de strings, apliquei conceitos distintos:
* **Verificador de Cidade:** Foco em posição fixa (`separa[0]`) para validar o início do texto.
* **Verificador de Sobrenome:** Uso do operador `in` dentro de coleções (listas) para garantir que a palavra seja encontrada em qualquer posição, evitando falsos positivos como "Silvano".

---

### 6.🧠 Condições e Bibliotecas

### 🎲 Jogo da Adivinhação v2.0
Criei um jogo onde o computador "pensa" em um número e o usuário tenta adivinhar. Evoluí o código original para incluir validações de segurança.

**O que aprendi e apliquei:**
* **Geração Aleatória:** Uso da biblioteca `random` (função `randint`) para criar números pseudoaleatórios baseados na semente do sistema.
* **Controle de Fluxo e UX:** Utilizei a biblioteca `time` (função `sleep`) para criar um efeito de processamento, melhorando a experiência do usuário.
* **Estrutura Condicional Encadeada (`if-elif-else`):** * Implementei uma **validação de entrada** com `range(0, 11)` para garantir que o usuário jogue apenas com números válidos.
    * Usei o `elif` para garantir que a lógica de vitória/derrota só seja executada se o número digitado estiver dentro das regras, evitando respostas contraditórias do sistema.

---

### 7.🚗 Radar Eletrônico
Implementei um sistema de radar que utiliza **Condições Simples** para fiscalizar a velocidade.

**Evolução Técnica:**
* **Cálculo de Multa Dinâmica:** A multa é gerada apenas se a velocidade ultrapassar 80km/h, custando R$ 7,00 por cada km excedente, utilizando a fórmula `(velocidade - 80) * 7`.
* **Formatação Monetária:** Apliquei a máscara de formatação `:.2f` para garantir que o valor da multa seja exibido no padrão real (R$) e representar valores monetários corretamente.
* **Lógica de Fluxo:** O código foi estruturado para que a saudação final ("Dirija com segurança") seja exibida independente se houver ou não a infração, mantendo uma boa interação com o usuário.

---

### 8.✈️ Custo da Viagem (Versão Pro)

Neste projeto, desenvolvi um calculador de passagens aéreas/rodoviárias que utiliza diferentes tarifas baseadas na distância percorrida. 

**O que aprendi e apliquei:**

* **Validação de Entrada:** Implementei um filtro inicial para garantir que o programa não processe distâncias inválidas (menores ou iguais a zero).
* **Operador Ternário:** Utilizei a sintaxe simplificada do Python para realizar o cálculo do preço em uma única linha, tornando o código mais "Pythonico" e elegante.
    * Tarifa A: R$ 0,50/km para viagens de até 200km.
    * Tarifa B: R$ 0,45/km para viagens acima de 200km.
* **Formatação de Saída:** Apliquei máscaras de formatação para exibir a distância sem casas decimais (`:.0f`) e o preço no formato monetário padrão (`:.2f`).

---

### 9.📅 Analisador de Ano Bissexto

 Usei a biblioteca **datetime** para capturar o ano atual do sistema e apliquei lógica matemática avançada para identificar anos bissextos. 
 
 * **Lógica:** Usei os operadores 'and' e 'or' para validar as três regras do calendário gregoriano. 
     * ano % 4 == 0: O ano tem que ser divisível por 4.
     * ano % 100 != 0: Mas não pode terminar em "00" (divisível por 100).
     * or ano % 400 == 0: A menos que ele seja divisível por 400 (como o ano 2000).
 * **Superação Técnica:** Configurei as políticas de execução do PowerShell para permitir o uso de ambientes virtuais (.venv) no VS Code.

---

### 10.🔢 Maior e Menor Valor 

Neste código, evoluí a lógica condicional para lidar com o desafio de comparar três cenários simultâneos, utilizando a técnica de atribuição inicial para otimizar o número de verificações.

* **Lógica de Comparação:** Implementei uma estrutura de verificação para definir qual número é o maior e qual é o menor entre três entradas. 
* **Estrutura Condicional:** Pratiquei o uso de múltiplos blocos 'if' independentes para validar cada cenário de comparação.

---

### 11.💰 Aumento de Salário 

Criei um script para calcular reajustes salariais diferenciados.

* **Lógica de Faixa Salarial:** Salários acima de R$ 1.250,00 recebem 10%, enquanto valores iguais ou inferiores recebem 15%. 
* **Formatação Monetária:** Pratiquei a exibição de valores flutuantes com o padrão de duas casas decimais.

* **Feedback ao Usuário:** O programa agora informa explicitamente a porcentagem aplicada (10% ou 15%), melhorando a experiência de uso.

---

### 12. 🃏 Jogo 21 da Sorte (Blackjack)

Este é um projeto pessoal desenvolvido para praticar lógica de programação em Python, unindo conceitos de estruturas de repetição e geração de números aleatórios.

### 🚀 Como funciona o jogo:
O objetivo é chegar o mais próximo possível de **21 pontos**. 
1. O sistema sorteia automaticamente uma "carta" (número entre 1 e 10).
2. O jogador decide se quer arriscar e tirar mais uma carta ou se prefere parar.
3. Se a soma ultrapassar 21, o jogador "estoura" e perde a partida.
4. Se atingir exatamente 21, é vitória garantida!

### 🛠️ Tecnologias e Conceitos Utilizados:
- **Linguagem:** Python
- **Módulo `random`:** Utilizado para gerar os valores das cartas de forma aleatória (`randint`).
- **Laço `while`:** Controle do fluxo do jogo baseado na decisão do usuário e na pontuação.
- **Estruturas Condicionais:** Uso de `if`, `elif` e `else` para determinar o resultado final.
- **Tratamento de Strings:** Uso de `.lower()` para garantir que o programa entenda a resposta do usuário independente de ser maiúscula ou minúscula.

### 📝 Aprendizados:
Neste projeto, pude consolidar o entendimento sobre como controlar repetições indefinidas e como integrar bibliotecas externas para tornar o programa mais dinâmico e interativo.