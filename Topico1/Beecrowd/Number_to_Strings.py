

numeros = [
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "catorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove"
]

decimais = [
    "", "", "vinte", "trinta", "quarenta", "cinquenta",
    "sessenta", "setenta", "oitenta", "noventa"
]

centenas = [
    "", "cento", "duzentos", "trezentos", "quatrocentos",
    "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"
]


def numero_para_string(numero):
    

    if numero < 20:
        # verifica se é menor que 20 (numeros com nomes unicos) e dps vai ate o vetor correspondente pois a adicao no vetor numero esta em ordem de 0 a 19
        return numeros[numero]
    elif numero < 100:
        # verifica se é menor que 100 (antes da casa da centena) e dps faz uma divisao interia logo arrecada o primeiro valor da centena, apos isso pega o resto da divisao por 10 logo pega a primeira casa, caso seja 0 nao imprime o mesmo
        return decimais[numero // 10] + (" e " + numeros[numero % 10] if numero % 10 != 0 else "")
    elif numero < 1000:
        # verifica se é divizivel por 100 e resta 0 , caso nao, ou seja possui decimais ele faz uma chamada recursiva e imprime as decimais com o resto por 100, sendo assim recebendo o numero decimal
        if numero % 100 == 0:
            return centenas[numero // 100]
        else:
            return centenas[numero // 100] + " e " + numero_para_string(numero % 100)
    elif numero < 1000000:
            #verifica se reta zero na divisao assim sendo numero exato, caso n faz uma recursividade achando a centena e dps a dezena
            if numero % 1000 == 0:
                return numero_para_string(numero // 1000) + " mil"
            else:
                return numero_para_string(numero // 1000) + " mil e " + numero_para_string(numero % 1000)


while True:
    try:
        n = int(input("Digite um numero: "))
        print(numero_para_string(n))
    except EOFError:
        break