# Calculadora de média

lista = []
quantidade = int(input("Digite quantos valores pretende inserir:"))
contador = 0
algarismo = 1
somatoria = 0

while contador < quantidade :
    valores = input(f"Digite o {algarismo}° valor: ").replace("," , ".")
    valores_novos = float(valores)  
    lista.append(valores_novos)
    contador +=1
    algarismo +=1

for valor in lista :
    somatoria += valor

media = somatoria / quantidade
print(f"O valor da média é: {media:.3f}")