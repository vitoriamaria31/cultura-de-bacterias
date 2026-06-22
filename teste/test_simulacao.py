from modelos.bacteria import Bacteria
from modelos.bacteria_resistente import BacteriaResistente
from simulacao import Simulacao


def test_crescimento_bacteria():
    bacteria = Bacteria("E. coli", 100, 0.25)

    bacteria.crescer()

    assert bacteria.get_populacao() > 100


def test_bacteria_resistente():
    simulacao = Simulacao()

    simulacao.usar_bacteria_resistente()

    assert isinstance(simulacao.bacteria, BacteriaResistente)


def test_antibiotico_reduz_populacao():
    simulacao = Simulacao()

    populacao_inicial = simulacao.bacteria.get_populacao()

    simulacao.aplicar_antibiotico()

    assert simulacao.bacteria.get_populacao() < populacao_inicial