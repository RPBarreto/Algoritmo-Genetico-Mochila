
# Objetivo: achar um vetor de inteiros (entre i_min e i_max) com i_length posicoes cuja a soma de todos os termos seja o mais proximo possivel de target

#O algoritmo rodara epochs vezes -> numero de populacoes geradas. Sera impresso a media de fitness de cada uma das epochs populacoes

#RODAR COM PYTHON 2!!! (senao colocar () em print e tirar x de xrange


  
from genetic2020 import *

objetos = [{
    "item": "Notebook",
    "peso": 10,
    "valor": 30,
},{
    "item": "Smartphone",
    "peso": 2,
    "valor": 15,
},{
    "item": "Copo",
    "peso": 4,
    "valor": 1,
},{
    "item": "Oculos",
    "peso": 1,
    "valor": 4,
},{
    "item": "Carregador Notebook",
    "peso": 1,
    "valor": 3,
},{
    "item": "GPU",
    "peso": 5,
    "valor": 12,
},{
    "item": "Perfume",
    "peso": 2,
    "valor": 8,
},{
    "item": "Diamante",
    "peso": 1,
    "valor": 40,
},{
    "item": "Monitor",
    "peso": 25,
    "valor": 30,
},{
    "item": "Garrafa",
    "peso": 2,
    "valor": 3,
},{
    "item": "Cachorro",
    "peso": 30,
    "valor": 50,
},{
    "item": "Impressora",
    "peso": 25,
    "valor": 8,
}]

target = 30 #Peso Mochila
i_length = len(objetos) #Tamanho do vetor de objetos
#i_length = 2
i_min = 0 #Valor minimo é zero, igual ao objeto não estar presente
i_max = 1 #Valor máximo é um, igual ao objeto estar presente
p_count = 200 #tamanho população
epochs = 100 #numero de gerações
number_parents=40 #numero de pais a serem selecionados
p = population(p_count, i_length, i_min, i_max) #criação da populacao de acordo com os parametros
fitness_history = [media_fitness(p, target,objetos),]
for i in range(epochs):
    p = evolveRoleta(p, target, objetos, number_parents)
    fitness_history.append(media_fitness(p, target, objetos))
print("Medias")
for datum in fitness_history:
   print (datum)