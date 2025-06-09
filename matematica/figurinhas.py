quantidade_casos = int(input())
mdc = None
mdc_resultados = []

for i in range(quantidade_casos):
    q_ricardo, q_vicente = map(int,input().strip().split())
    while q_vicente != 0:
       q_ricardo, q_vicente = q_vicente, q_ricardo % q_vicente
    mdc_resultados.append(q_ricardo)

for i in range(len(mdc_resultados)):
    print(mdc_resultados[i])

       
        


