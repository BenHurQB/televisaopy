

from televisao import tv1
from televisao import canal1
import os

def menu():
    print("\n\nCONTROLE REMOTO")
    print('_____________________')
    print('\n1 - Ligar / Desligar ')
    print('2 - Volume')
    print('3 - Mudar Canal')
    print('4 - Gravar Canal')
    print('0 - Sair')
    print('_____________________')
    opc = int(input('Sua opção:  '))
    return opc


#escolha = ''
#botao = ''

tv1.mostrarEstado()
opc = menu()
while (opc != 0):

    if (opc == 1):
        print("\nMenu Liga / desliga")
        print('_____________________')
        print('1 - Ligar')
        print('2 - Desligar')
        escolha = int(input('Sua opção: '))
        if (escolha == 1):
            tv1.ligar('Ligar')
        else:
            tv1.ligar('Desligar')
    elif (opc == 2):
        escolha = input('Tecle [ + / - ]  para aumentar / diminuir: ')
        tv1.aumentarVolume(escolha)
    elif (opc == 3):
        tv1.mudarCanal()
    elif (opc == 4):
        tv1.gravarCanal(canal1)
    else:
        print("Opção Invalida!!!!!!")

    opc = menu()

print("Fim do Programa....")
