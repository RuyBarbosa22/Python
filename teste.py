
import psutil

utilizacaoCpu = psutil.cpu_times(percpu = False ) 
porcentagemCpu = psutil.cpu_percent(interval = 1, percpu=True)
qtdNucleos = psutil.cpu_count(logical=False)
qtdNucleosLogicos = psutil.cpu_count()
frequenciaCpu =  psutil.cpu_freq()
caminhoDisco = psutil.disk_partitions()
espacoDisco = psutil.disk_usage('C:\\')

print(porcentagemCpu)
print(utilizacaoCpu)
print(qtdNucleos)
print(qtdNucleosLogicos)
print(frequenciaCpu)
print(caminhoDisco)
print(espacoDisco)

# podemos apresentar dados especificos utilizando um indice de vetor ([0,1,2,3,4,5])
# e assim formatalos