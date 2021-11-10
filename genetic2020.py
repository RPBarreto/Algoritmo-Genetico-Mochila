

from random import randint, random
from operator import add, itemgetter
from functools import reduce

def individual(length, min, max, ):
    'Create a member of the population.'
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual, target, objetos):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for

    Como o target neste problema é o peso limitador da mochila, ele não será usado como medida de fitness 
    e sim como parametro de exclusão de individuos que ultrapassarem este valor, a exclusão é dada ao atribuir um valor 0 de fitness

    O fitness será calculado pela maior soma de Valor dos itens
    """
    valor = 0
    peso = 0
    for i in range(len(objetos)):
            valor += individual[i]*objetos[i]["valor"]  #Percorre a lista e multiplica o estado do objeto (0 ou 1) pelo seu valor e peso
            peso += individual[i]*objetos[i]["peso"] #os valores são adicionados as variaveis de peso e valor, objetos com estado zero somam zero e com estado 1 somam seu respectivos valores de peso e valor

    if peso <= target:
        return valor
    else:
        return 0


def media_fitness(pop, target,objetos):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, target,objetos) for x in pop))
    return summed / (len(pop) * 1.0)


def evolve(pop, target, objetos, retain=0.2, random_select=0.05, mutate=0.01):
    'Tabula cada individuo e o seu fitness'
    graded = [ (fitness(x, target, objetos), x) for x in pop]
    'Ordena pelo fitness os individuos - maior->menor'
    graded = [ x[1] for x in sorted(graded, reverse=True)]
    'calcula qtos serao elite'
    retain_length = int(len(graded)*retain)
    'elites ja viram pais'
    parents = graded[:retain_length]
    # randomly add other POUCOS individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    'descobre quantos filhos terao que ser gerados alem da elite e aleatorios'
    desired_length = len(pop) - parents_length
    children = []
    'comeca a gerar filhos que faltam'
    while len(children) < desired_length:
        'escolhe pai e mae no conjunto de pais'
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            'gera filho metade de cada'
            child = male[:half] + female[half:]
            'adiciona novo filho a lista de filhos'
            children.append(child)
    'adiciona a lista de pais (elites) os filhos gerados'
    parents.extend(children)
    return parents

def evolveRoleta(pop, target, objetos, number_parents, mutate=0.01):
    'Tabula cada individuo e o seu fitness'
    graded = [ [fitness(x, target, objetos), x] for x in pop]
    'soma dos fitness'
    summed = reduce(add, (fitness(x, target, objetos) for x in pop))
    #'Ordena pelo fitness os individuos - maior->menor, mantendo os fitness dos individuos'
    #graded = sorted(graded, key=itemgetter(0) ,reverse=True)
    
    parents =[]
    anterior =0
    for x in graded:
        relative_prob = 0
        relative_prob = (x[0]/summed) + anterior
        anterior = relative_prob
         #calcula o valor relativo de probabilidade do individuo e soma com a somatória da torta, dando o valor a qual é necessario para que seja escolhido
        x[0]=relative_prob

   # print(pie)
    while len(parents) < number_parents: #enquanto o numero de pais nao for preenchido, repete
        r = random() #aleatorio entre 0 e 1
        for x in graded: #para cada pedaço da torta pegar a posição e probabilidade
            if r <= x[0]: #caso o numero aleatorio seja menor ou igual a probabilidade relativa, o individuo é adicionado aos pais pela sua posição
                parents.append(x[1])
                break
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    'descobre quantos filhos terao que ser gerados'
    desired_length = len(pop)
    children = []
    'comeca a gerar filhos que faltam'
    while len(children) < desired_length:
        'escolhe pai e mae no conjunto de pais'
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            'gera filho metade de cada'
            child = male[:half] + female[half:]
            'adiciona novo filho a lista de filhos'
            children.append(child)
    return children
