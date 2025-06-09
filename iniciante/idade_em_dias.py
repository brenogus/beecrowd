dias_totais = int(input())

anos = dias_totais //  365
meses = dias_totais % 365
meses_totais = meses // 30
dias = meses % 30

print(f'{anos} ano(s)')
print(f'{meses_totais} mes(es)')
print(f'{dias} dia(s)')