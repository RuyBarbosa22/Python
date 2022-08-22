import psutil

pctDisco = psutil.disk_usage('C:\\')[3]
livreDisco = round((psutil.disk_usage('C:\\')[2]/1000000000),2) #convertendo para de Kbs pra GBs e arredondando
totalDisco = round((psutil.disk_usage('C:\\')[0] /1000000000),2)
usadoDisco = round((psutil.disk_usage('C:\\')[1] /1000000000),2)
htzAtualCpu =   (psutil.cpu_freq()[0])/1000
nucleoFisico =  psutil.cpu_count(logical=False)
nucleoLogico = psutil.cpu_count(logical=True)
usoNucleosMedia = psutil.cpu_percent(interval=1)
pctUsoNucleo = psutil.cpu_percent(interval=1, percpu=True)
pctUsoCpu =  psutil.cpu_percent(interval = None , percpu = False )
pctUsoRam = psutil.virtual_memory().percent
dispRam = round(psutil.virtual_memory().total/1000000000,1) #arredondando e fazendo conta 





print(f"Velocidade processador: {htzAtualCpu} Ghz")  #Velocidade atual CPU
print(f"{nucleoLogico} núcleos lógicos") #Número de núcleos da CPU
print(f"{nucleoFisico} núcleos físicos") #Quantidade de núcleos físicos
print(f"Uso núcleo: {pctUsoNucleo}% de uso atual de cada núcleo") #Porcentagem de uso de cada núcleo da CPU
print(f"Média: {usoNucleosMedia}% de uso dos núcleos")
print(f"CPU: {pctUsoCpu}% de uso do processador") #Porcentagem de uso atual da CPU   
print(f"Disco: {pctDisco}% de uso") #Porcentagem de uso Disco
print(f"Disco: {livreDisco}GB de espaço livre") #Gb de espaço livre
print(f"Disco: {totalDisco}GB de espaço total") #Gb de espaço total
print(f"Disco: {usadoDisco}GB de espaço usado") #Gb de espaço usado
print(f"RAM: {dispRam}Gb de RAM disponível") #Gb de ram disponivel
print(f"RAM: {pctUsoRam}% de memória ram em uso") #% de ram usado
