datos = input().split(', ')
sumatoria = 0

for i in datos:
    sumatoria+=float(i)

print(sumatoria/len(datos))