carEconomy = 12

def getDistance(time, averageSpeed):
    return time * averageSpeed

def getUsedLiters(distance):
    return distance / carEconomy

travelTime = int(input("Digite o tempo de viagem: "))
averageSpeed = int(input("Digite a velocidade média: "))
distance = getDistance(travelTime, averageSpeed)

print(f"Tempo de viagem: {travelTime}")
print(f"Velocidade média: {averageSpeed}")
print(f"Distãncia percorrida: {distance}")
print(f"Litros gastos: {getUsedLiters(distance)}")


