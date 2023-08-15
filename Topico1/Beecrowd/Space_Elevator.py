
def numero_do_andar(nivel):
    andar_atual = 0
    numero_andar = 0
    #enquanto  andar atual for menor que o nivel o qual deseja
    while andar_atual < nivel:
        # transforma numero de andares em str para poder verificar os caracteres
        numero_andar_str = str(numero_andar)
        # se nao esta na condicao ( ou seja nao possuir 4 ou 13) aumenta o andar, caso possuia pula o andar atual para nao somar no numero de andares 
        if '4' not in numero_andar_str and '13' not in numero_andar_str:
            andar_atual += 1
        
        numero_andar += 1

    return numero_andar 


while True:
    nivel_desejado = int(input('Digite o andar'))

    if nivel_desejado > 0:
        break

numero_do_andar_correspondente = numero_do_andar(nivel_desejado)
print(f"O nível {nivel_desejado} corresponde ao número do andar {numero_do_andar_correspondente}.")

