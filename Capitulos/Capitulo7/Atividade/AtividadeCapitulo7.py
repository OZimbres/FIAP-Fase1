anos_fumando = float(input("Há quantos anos que vossa mercê fuma? "))
preco_maco_cigarro = float(input("Qual o valor do maço de cigarro que vossa mercê compra? "))
macos_por_dia = float(input("Quantos maços de cigarro vossa mercê fuma por dia? "))

total_gasto = anos_fumando * 365 * macos_por_dia * preco_maco_cigarro

if total_gasto < 20000:
    print(f"Com o valor R$ {total_gasto:.2f}, você poderia ter dado entrada em um carro.")
elif total_gasto < 50000:
    print(f"Com o valor R$ {total_gasto:.2f}, você poderia ter comprado um carro popular usado")
else:
    print(f"Com o valor R$ {total_gasto:.2f}, você poderia ter comprado um carro zero.")
