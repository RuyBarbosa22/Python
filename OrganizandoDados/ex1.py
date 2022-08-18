import psutil

pctDisco = psutil.disk_usage('C:\\')[3]
htzAtualCpu =   psutil.cpu_freq()[0]
lgcCpu = psutil.cpu_count()
pctUsoNucleo = psutil.cpu_percent(interval=1, percpu=True)
pctUsoCpu =  psutil.cpu_percent(interval = None , percpu = False )




print(pctDisco) #Porcentagem de uso Disco
print(htzAtualCpu)  #Velocidade atual CPU
print(lgcCpu) #Número de núcleos da CPU
print(pctUsoNucleo) #Porcentagem de uso de cada núcleo da CPU
print(pctUsoCpu) #Porcentagem de uso atual da CPU
