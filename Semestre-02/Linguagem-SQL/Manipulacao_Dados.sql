-- ======================================================
-- ESTUDOS DE SQL - BANCO CAFFEINE_CODE
-- Objetivo: Script COMPLETO (Cadastro, Ajustes e Consultas)
-- ======================================================

USE Caffeine_Code;
GO

-- 1. CADASTRO INICIAL (DML - Cap 5)
-- Inserindo Medidas (O IDENTITY cuida dos IDs)
INSERT INTO Medida (Nome, Descricao) VALUES ('Mililitro', 'ml'), ('Quilo', 'kg'), ('Gramas', 'g');

-- Inserindo Bebidas (Apenas as colunas que REALMENTE existem no seu banco)
INSERT INTO Bebida (Nome, ModoPreparo, Preco) VALUES 
('Café Mocha', 'Misturar café, leite e cacau', 12.00),
('Suco de Morango', 'Bater morangos com água', 10.00),
('Chocolate Quente', 'Misturar leite e cacau', 9.00);
GO

-- 2. AJUSTES DE ESTRUTURA E DADOS (Cap 6, 7 e 8)
-- Adicionando a coluna de tempo que o exercício pediu
IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('Bebida') AND name = 'TempoPreparo')
BEGIN
    ALTER TABLE Bebida ADD TempoPreparo INT;
END
GO

-- Atualizando os dados para os exercícios de fixação
UPDATE Ingrediente SET Nome = 'Cacau em pó 50%' WHERE idIngrediente = 1;
UPDATE Venda SET Data = '20150115' WHERE MONTH(Data) = 2;

-- Definindo os tempos de preparo
UPDATE Bebida SET TempoPreparo = 5 WHERE Nome = 'Café Mocha';
UPDATE Bebida SET TempoPreparo = 12 WHERE Nome = 'Suco de Morango';
UPDATE Bebida SET TempoPreparo = 8 WHERE Nome = 'Chocolate Quente';
GO

-- 3. CONSULTAS DE RELATÓRIO (DQL - Cap 8)
-- Quantidade de bebidas rápidas (entre 5 e 10 min)
SELECT COUNT(*) AS TotalBebidasRapidas
FROM Bebida
WHERE TempoPreparo BETWEEN 5 AND 10;

-- Cardápio ordenado de A a Z
SELECT Nome, Preco, TempoPreparo 
FROM Bebida 
ORDER BY Nome ASC;
GO