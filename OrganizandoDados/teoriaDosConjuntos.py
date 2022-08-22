conjunto_processador = set ({'CPU', 'Processador', 'Core', 'CPU'})
conjunto_processador2 = set (conjunto_processador)
print(conjunto_processador2)

#começando a usar operador de união ("|", ".union")

#Os dados não se repetem (CPU)

userThor = {'mysql', 'CPU', 'RAM', 'SSD1', 'Google'}
userThanos = {'LoL', 'RAM', 'CPU', 'HD', 'Google'}
userCA = {'mysql', 'LOL', 'RAM', 'CPU', 'Firefox'}
userTS = {'mysql', 'CPU', 'RAM', 'SSD1', 'Google'}
inventario1 = userThor | userCA
print(inventario1)

#unimos os dois conjuntos de dados de strings, fazendo com que eles sejam
#apresentados juntos.

inventario2 = userThor | userCA | userThanos | userTS
print(inventario2)

#unindo todos os conjuntos de informações e os apresentando juntos
#por estar em formato de string, o item 'LOL & LoL' são exibidos juntos

inventario3 = userThor.union(userCA)
print(inventario3)

#essa é uma outra forma de fazer uma união entre duas listas de dados.

inventario4 = userThor.union(userCA, userTS, userThanos)
print(inventario4)

#usando operador de intersecção (&)

inventario1 = userThor & userCA
print(inventario1)

#usando de outra forma a intersecção

inventario3 = userThor.intersection(userThanos)
print(inventario3)

#fazendo a intersecção entre todos os conjuntos de dados

inventario4 = userThor.intersection(userThanos, userCA, userTS)
print(inventario4)

#usando o operador de difeença
#as duas maneiras que podemos fazer a diferença é assim

inventario5 = userThor - userThanos
print(inventario5)

inventario5 = userThor - userTS - userCA - userThanos
print(inventario5)

#usando operador de pertinencia


#validando se "CPU", esta contida dentro de "userThanos"
'CPU' in userTS
'Firefox' in userThanos

#validando se "LoL" NÃO esta contido no conjunto "userCA"
'LoL' not in userCA
'LOL' not in userCA


#aqui vamos fazer a validação de subconjuntos
#se por exemplo, o conjunto Hulk tem "CPU,RAM", o comando que valida ele com "userThor" que possui os dois, retornaria True
#se fizessemos essa validação com um conjunto que não tivesse "RAM, CPU", receberiamos False como resposta

userThor.issubset(userThanos)

userThor.issubset(userTS)

#outra forma de fazer

userThor <= userThanos

userThor <= userTS


#testando comparação/igualdade

#validando se os dois conjuntos são iguais
userTS == (userThor)

#validando se os dois conjuntos são diferentes
userTS != (userThor)

#-------------------------------------- de novo

userTS == (userCA)

userTS != (userCA)

#validando usando simetria/diferença simetrica
#aqui validamos qual dado um dos conjuntos tem e o outro não tem, e vice versa.

userTS ^ userCA
