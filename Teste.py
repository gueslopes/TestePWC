import re
from tokenize import String
from pip import List


def checaCaso(endereco) -> List[str]:

    endereco = endereco.replace(",", "")

    valores_split = dict(
        casoComplexo="(^\w+?\s\d+)",
        casoNumero="(\d+.)",
        casoComum="(\d+.+)"
    )

    if regexes("^\w+?\s\d+\s\w+?\s\d+", endereco):
        return trataDados(endereco, valores_split['casoComplexo'])

    elif regexes("^\d", endereco):
        return formataDados(trataDados(endereco, valores_split['casoNumero']))

    else:
        return trataDados(endereco, valores_split['casoComum'])


def trataDados(endereco, split) -> List[str]:

    return list(filter(None, re.split(
        split, endereco, maxsplit=1, flags=re.IGNORECASE)))


def formataDados(formata_lista) -> List[str]:

    formata_lista[0] = formata_lista[0].replace(" ", "")
    formata_lista.reverse()

    return formata_lista


def regexes(regex, endereco) -> bool:

    return re.match(regex, endereco, flags=re.IGNORECASE)


def main():
    # Entrada colocada manualmente
    entrada: String = input("Digite o endereco: ")

    print(checaCaso(entrada))


main()
