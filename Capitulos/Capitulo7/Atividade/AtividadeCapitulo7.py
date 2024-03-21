anos_fumando = float(input("Há quantos anos que Vossa Mercê fuma? "))

if anos_fumando > 0:
    macos_por_dia = float(input("Quantos maços de cigarro Vossa Mercê fuma por dia? "))

    if macos_por_dia > 0:
        preco_maco_cigarro = float(input("Qual o valor do maço de cigarro que Vossa Mercê compra? "))

        if preco_maco_cigarro > 0:
            #             ( anos X 365 = dias )
            total_gasto = anos_fumando * 365 * macos_por_dia * preco_maco_cigarro

            if total_gasto < 20000:
                print(f"Com o valor R$ {total_gasto:.2f}, Vossa Mercê poderia ter dado entrada em um carro.")

            elif total_gasto < 50000:
                print(f"Com o valor R$ {total_gasto:.2f}, Vossa Mercê poderia ter comprado um carro popular usado")

            else:
                print(f"Com o valor R$ {total_gasto:.2f}, Vossa Mercê poderia ter comprado um carro zero.")

        elif preco_maco_cigarro == 0:
            print("Os cigarros que Vossa Mercê fuma são gratuitos, então não gastou nada com cigarros.")

        else:
            print("Vossa Mercê digitou um valor inválido.")

    elif macos_por_dia == 0:
        print("Vossa mercê não fuma, então não gastou nada com cigarros.")

    else:
        print("Vossa Mercê digitou um valor inválido.")

elif anos_fumando == 0:
    print("Vossa Mercê não fuma, então não gastou nada com cigarros.")

else:
    print("Vossa Mercê digitou um valor inválido.")
