# -*- coding: utf-8 -*-
import anydbm

# one of my first programs
def bot():
    memoria = anydbm.open("dicionario.db","c")
    entrada = "Olá"
    while entrada != "adeus":
        if entrada == "enganaste-te":
            print "o que deveria eu responder?"
            resposta = raw_input("Eu :")
            memoria[entrada] = resposta
            print "Bot :Tentarei memorizar."
        elif entrada in memoria:
            print "Bot :", memoria[entrada]
            entrada = raw_input("Eu :")
        else:
            print "o que deveria eu responder?"
            resposta = raw_input("Eu :")
            memoria[entrada] = resposta
            print "Bot :Tentarei memorizar."
    memoria.close()

bot()
    
