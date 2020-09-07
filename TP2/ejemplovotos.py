votos = []
n = int(input("Votos del candidato? (-1 para terminar): "))
while n != -1:
    votos = votos + [n]  #votos.append(n) sería similar
    n = int(input("Votos del candidato? (-1 para terminar) "))
print()

# Calcular porcentajes e imprimir listado final
total = sum(votos)
for i in range(len(votos)):
    porcentaje = votos[i] * 100 / total
    print(" Candidato %d: %d votos (%.2f%%)"%(i, votos[i], porcentaje), end=" ")
    # Imprimir el gráfico de barras
    for j in range(int(porcentaje/10)):
        print("", end="")
        print()