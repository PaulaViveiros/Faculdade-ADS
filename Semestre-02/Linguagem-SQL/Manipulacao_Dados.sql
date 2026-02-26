-- ======================================================
-- ESTUDOS DE SQL - MANIPULAÇÃO DE DADOS (DML)
-- Objetivo: Povoar o banco da Cafeteria e ajustar receitas
-- ======================================================

-- 1. INSERINDO MEDIDAS QUE FALTAVAM
-- O IDENTITY cuida dos IDs automaticamente
INSERT INTO Medida (Nome, Descricao) VALUES ('Unidade', 'un'), ('Gramas', 'g');

-- 2. INSERINDO AS BEBIDAS
INSERT INTO Bebida (Nome, ModoPreparo, TempoPreparo, Quantidade, idMedida, Temperatura) VALUES 
('Suco de Morango', 'Bater morangos com água', 5, 300.00, 1, 'Gelado'),
('Vitamina de Banana', 'Bater banana com leite', 7, 400.00, 1, 'Gelado'),
('Chocolate Quente', 'Misturar leite e cacau', 10, 200.00, 1, 'Quente'),
('Expresso', 'Café moído na hora', 3, 50.00, 1, 'Quente');

-- 3. CRIANDO AS RECEITAS (Tabela de Ligação)
-- Vinculando ingredientes às bebidas com as quantidades certas
INSERT INTO BebidaIngrediente (idBebida, idIngrediente, idMedida, Quantidade) 
VALUES 
(2, 6, 6, 150.00), -- Suco de Morango: 150g de Morango (ID 6 = g)
(2, 4, 6, 15.00);   -- Suco de Morango: 15g de Açúcar

-- 4. AJUSTANDO DADOS (UPDATE)
-- Exemplo de correção de unidade de medida e quantidade
UPDATE BebidaIngrediente 
SET idMedida = 6, Quantidade = 15.00 
WHERE idBebida = 2 AND idIngrediente = 4;

-- 5. RELATÓRIO COMPLETO (O "SELECT GRANDÃO")
-- Comando para visualizar nomes em vez de apenas IDs
SELECT 
    B.Nome AS [Bebida],
    I.Nome AS [Ingrediente],
    BI.Quantidade AS [Qtd],
    M.Descricao AS [Unidade]
FROM BebidaIngrediente BI
INNER JOIN Bebida B ON BI.idBebida = B.idBebida
INNER JOIN Ingrediente I ON BI.idIngrediente = I.idIngrediente
INNER JOIN Medida M ON BI.idMedida = M.idMedida;