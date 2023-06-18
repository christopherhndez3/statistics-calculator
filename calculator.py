import statistics

def calcular_estadisticas(numeros):
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    try:
        moda = statistics.mode(numeros)
    except statistics.StatisticsError:
        moda = "No hay un valor único de moda"
    desviacion_estandar = statistics.stdev(numeros)
    
    return media, mediana, moda, desviacion_estandar

numeros_str = input("Ingresa una lista de números separados por comas: ")

numeros = [int(num) for num in numeros_str.split(",")]

media, mediana, moda, desviacion_estandar = calcular_estadisticas(numeros)



print("Media aritmética:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desviación estándar:", desviacion_estandar)
