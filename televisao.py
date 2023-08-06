import os
class Tv:
    def __init__(self, marca, tamanho,  estado = 'Desligado', canal = 2 , volume = 0 ):
        self.marca = marca
        self.tamanho = tamanho
        self.estado = estado
        self.canal = canal
        self.volume = volume

    def mostrarEstado(self):
        print('\nSTATUS DA TELEVISÃO')
        print('_____________________')
        if (self.estado == 'Ligada'):
            print(f'\nTv: {self.estado}')
            print(f'Canal: {self.canal}')
            print(f'Volume: {self.volume}')
        else:
            print("\nAparelho Desligado!!!")
        print('_____________________')


    def mudarCanal(self):
        achei = False
        if (self.estado == 'Ligada'):
            canalProcurado = int(input('Informe o canal: '))
            for p in range(0, len(canal1)):
                if (canalProcurado == canal1[p]):
                    self.canal = canal1[p]
                    achei = True
            if (not achei):
                print("\nCanal não esta gravado....")
        tv1.mostrarEstado()
        os.system('pause')


    def ligar(self, botao):
        if (botao == 'Ligar'):
            self.estado = 'Ligada'
        else:
            self.estado = 'Desligada'
        tv1.mostrarEstado()
        os.system('pause')

    def aumentarVolume(self, botao):
        if (self.estado == 'Ligada'):
            if(botao == '+'):
                if(self.volume < 3):
                    print('\nAumentando Volume!!!!')
                    self.volume += 1
                    print(f'Volume = {self.volume}')
                if (self.volume == 3):
                    print('\nVolume máximo alcançado!!!!')
            else:
                if (self.volume > 0):
                    print('\nDiminuindo Volume!!!!')
                    self.volume -= 1
                    print(f'Volume = {self.volume}')
                else:
                    print('\nVolume não pode mais baixar!!!')
                    print(f'Volume = {self.volume}')
        tv1.mostrarEstado()
        os.system('pause')

    def gravarCanal(self, canal1):
        achei = False
        if (self.estado == 'Ligada'):
            novoCanal = int(input("Informe o novo canal: "))
            for p in range(0, len(canal1)):
                if (novoCanal == canal1[p]):
                    achei = True
            if (not achei):
                canal1.append(novoCanal)
                print(f'\nCanal {novoCanal} gravado com sucesso!!!!')
            else:
                print("\nCanal já foi gravado....")

        else:
            tv1.mostrarEstado()
        os.system('pause')
        return canal1

tv1 = Tv('philco', 15)
canal1 = [2, 4, 6, 9, 11, 13]
