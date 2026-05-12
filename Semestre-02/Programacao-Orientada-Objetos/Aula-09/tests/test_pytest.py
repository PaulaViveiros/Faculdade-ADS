import pytest  # Importa a biblioteca base (necessário para o pytest.raises)
from pytest import mark, fixture  # Importa as ferramentas específicas

#from codigo.jogo import brincadeira # Brincadeira - SUT - System Under Test#

from codigo.jogo import verificar_idade

def test_deve_lancar_erro_quando_idade_for_negativa():
    with pytest.raises(ValueError, match="Idade nao pode ser negativa!"):
        verificar_idade(-5)


#@fixture
#def minha_fixture():
#    """Essa é a minha fixture"""

#def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
#entrada = 1 #dado
#esperado = 1 #dado
#resultado = brincadeira(1) #when
#assert resultado == esperado #then"""##

#Versão simplificada - TDD - Kent Beck - One-Step Test
#def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
#    assert brincadeira(1) == 1

#def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
#    assert brincadeira(2) == 2

#def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
#    assert brincadeira(3) == "queijo"

#@mark.goiabada
#def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
#    assert brincadeira(5) == "goiabada"

#@mark.goiabada
#def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
#    assert brincadeira(10) == "goiabada"

#@mark.skip(reason="Porque o teste ainda não foi implementado")
#def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
#   assert brincadeira(20) == "goiabada"

#@mark.parametrizado
#@mark.parametrize(  
#    'entrada',
#    [5,10,20,25,35]
#)
#def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
#    assert brincadeira(entrada) == "goiabada"

#@mark.parametrizado
#@mark.parametrize(
#    'entrada',
#    [3,6,9,12,18]
#)
#def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
#    assert brincadeira(entrada) == "queijo"

#@mark.parametrizado
#@mark.parametrize(  
#    'entrada,esperado',
#    [(1, 1),(2, 2),(3, "queijo"), (4, 4), (5, "goiabada")]
#)
#def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
#    assert brincadeira(entrada) == esperado

#@mark.xfail
#def test_xfail1():
#    assert brincadeira(20) == "goiabada"

#@mark.xfail
#def test_xfail2():
#    assert brincadeira(20) != "goiabada"

#@mark.xfail(sys.plataform == "win32", reason="Teste falha no Windows")
#def test_xfail_windows():
#    assert brincadeira(20) == "goiabada"

#@mark.xfail(sys.plataform == "win32")
#def test_xfail_windows_skip():
#    assert brincadeira(20) == "goiabada"

#@mark.stdout
#def test_brincadeira_deve_escrever_entrei_na_brincadeira(capsys):
#    brincadeira(0)
#    resultado = capsys.readouterr()
#    assert resultado.out == "Entrei na brincadeira!\n"


"""TDD  - Test Driven Development (Desenvolvimento Orientado a Testes)
é uma metodologia de desenvolvimento de software onde os testes são escritos antes do código de produção.
O processo é dividido em três etapas:


O teste é formado em 3 etapas (GWT - AAA):

- Given (Dado): Contexto do teste, ou seja, o cenário onde o teste será executado.
- When (Quando): A ação que será realizada, ou seja, o comportamento que será testado.
- Then (Então): O resultado esperado, ou seja, a resposta que o teste deve retornar

- Arange (Organizar): Preparar o cenário do teste, ou seja, criar os objetos e definir as variáveis necessárias
para a execução do teste.
- Act (Agir): Executar a ação que será testada, ou seja, chamar o método ou função que será testada.
- Assert (Afirmar): Verificar se o resultado obtido é igual ao resultado esperado, ou seja, comparar o resultado
obtido com o resultado esperado e retornar um erro caso eles sejam diferentes.

xfail - Expected Failure - Falha Esperada - é uma marcação utilizada em testes para indicar que um teste é esperado para falhar.
Isso pode ser útil em situações onde um teste está sendo desenvolvido, mas ainda não foi implementado corretamente,
ou quando um teste está sendo executado em um ambiente onde ele não é suportado (Ex: teste que falha no Windows, mas passa no Linux).
Quando um teste marcado como xfail falha, ele é registrado como uma falha esperada, e não como uma falha real.
Se o teste passar, ele é registrado como um teste inesperadamente bem-sucedido.

A fixture é uma função que é executada antes de cada teste para preparar o ambiente de teste. Ela pode ser usada para criar objetos, 
configurar conexões de banco de dados, ou qualquer outra tarefa necessária para garantir que os testes sejam executados em um ambiente 
controlado e consistente. As fixtures são definidas usando o decorador @pytest.fixture e podem ser compartilhadas entre vários testes.
É basicamente uma maneira de "entrar" em um contexto, ou prover uma ferramenta que precisa ser executada antes de um teste.

xUnit Patterns - Gerard Meszaros - são um conjunto de padrões de design para testes unitários, que ajudam a organizar e estruturar os testes 
de forma eficiente e eficaz. Alguns dos padrões mais comuns incluem:
Setup: "Dado" Um método que é executado antes de cada teste para preparar o ambiente de teste.
Exercise: "Quando" O método que é testado, ou seja, o código que está sendo verificado.
verify: "Então" O método que verifica se o resultado do teste é o esperado.
Teardown: "Depois" "Desmonsta tudo, antes que seja tarde". Um método que é executado após cada teste para limpar o ambiente de teste.""""