import random
import time

def jogar(jogo=1):
    novo = '-----NOVO JOGO-----'
    print novo
    jogando = True
    espaco = '.\n' * 50
    nivel = 1
    codigo = ''
    while jogando:
        if jogo ==1:
            codigo = ''
        else:
            codigo += ' '
        for i in range(nivel):
            minuscula = chr(random.randint(ord('a'), ord('z')))
            maiuscula = chr(random.randint(ord('A'), ord('Z')))
            numero = str(random.randint(0, 9))
            tipo = [minuscula, maiuscula, numero]
            digito = tipo[random.randint(0, 2)]
            codigo += digito
        texto = 'nível ' + str(nivel) + '\n\n' + codigo
        print texto
        t1 = time.time()
        while time.time() < t1 + nivel * 2:
            pass
        print espaco
        resposta = raw_input('resposta  -->\t')
        if resposta == codigo:
            print '\nCerto!'
            nivel += 1
        else:
            mensagem = '\nErrado :(\na resposta certa era "'
            mensagem += codigo + '"\nconseguiste chegar ao nível '
            mensagem += str(nivel) + '\n\n\n'
            print mensagem
            actualizar(nivel)
            codigo = ''
            pausa = raw_input(novo)
            nivel = 1

        
def actualizar(valor):
    ficheiro = 'Memoria.txt'
    ler = open(ficheiro, 'r')
    recorde = int(ler.read())
    ler.close()
    if valor > recorde:
        print '\nParabéns, bateste o recorde anterior!\n'
        novo =  open(ficheiro, 'w')
        novo.write(str(valor))
        novo.close()
    print 'recorde: ', recorde

jogar()
