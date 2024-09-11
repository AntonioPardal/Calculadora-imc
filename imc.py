peso = float(input("digite seu peso em Kg: "))

altura = float(input("digite sua altura em Mts: "))

imc = peso / (altura * altura)

print("seu imc é igual a: ", imc)

if imc < 16:
	print("Seu estado é de Magreza grave\nProcure um médico ou nutricionista.")
elif imc < 17:
	print("Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.")
elif imc < 18.5:
	print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
	print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")
