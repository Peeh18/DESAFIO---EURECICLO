# testes.py
import pytest
from garrafas_solver import encontrar_melhor_combinacao

def test_combinacao_exata():
    galao = 5
    garrafas = [1, 3, 4.5, 1.5]
    resultado, sobra = encontrar_melhor_combinacao(galao, garrafas)
    assert sum(resultado) - galao == pytest.approx(sobra)
    assert sobra >= 0

def test_combinacao_com_sobra():
    galao = 5
    garrafas = [1, 3]
    resultado, sobra = encontrar_melhor_combinacao(galao, garrafas)
    assert sobra >= 0
    assert sum(resultado) - galao == pytest.approx(sobra)

def test_menor_numero_de_garrafas():
    galao = 4.9
    garrafas = [4.5, 0.4, 0.3, 0.1]
    resultado, sobra = encontrar_melhor_combinacao(galao, garrafas)
    assert resultado == [4.5, 0.4]
    assert sobra == pytest.approx(0)