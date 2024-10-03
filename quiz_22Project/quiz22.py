# variables
nombre = input("ingrese su nombre: ")
dias = int(input("ingrese los dias de trabajo: "))
salario = int(input("ingrese su salario: "))

prima = (salario*dias)/360
cesantias = (salario*dias)/360
interesesCesantias = (cesantias*0.12)/dias
vacaciones = (salario*dias)/720 # datos de prueba
liquidacion = (prima+cesantias+interesesCesantias+vacaciones)

print(f"señor {nombre} para los {dias} dias laborados y salario {salario}, su liquidacion se compone asi: "
      f"prima: {prima:.2f}, "
      f"cesantia: {cesantias:.2f},"
      f"intereses cesantias: {interesesCesantias:.2f} "
      f"vacaciones: {vacaciones:.2f} "
      f"liquidacion: {liquidacion:.2f}")