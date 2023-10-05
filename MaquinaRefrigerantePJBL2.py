# Módulo que exibe a quantidade de dinheiro para cada cédula/moeda e a quantidade de bebidas
def exibir_quantias(qtd025, qtd050, qtd1, qtd2, qtd5, qtd10, qtd20, qtdbebidas):
    print("Há", qtd025, "moeda(s) de 25 centavos")
    print("Há", qtd050, "moeda(s) de 50 centavos")
    print("Há", qtd1, "moeda(s) de 1 real")
    print("Há", qtd2, "cédula(s) de 2 reais")
    print("Há", qtd5, "cédula(s) de 5 reais")
    print("Há", qtd10, "cédula(s) de 10 reais")
    print("Há", qtd20, "cédula(s) de 20 reais")
    print("Há", qtdbebidas, "bebida(s) na máquina")


# Módulo que exibe o menu de ADMIN
def exibir_menu():
    print("Deseja realizar qual operação:")
    print("1-ADICIONAR/REMOVER DINHEIRO 2-ADICIONAR/REMOVER BEBIDAS 3-HISTÓRICO DE PAGAMENTOS PIX")
    print("4-VOLTAR AO MENU 5-DESLIGAR A MÁQUINA")


# Função para impedir retirada de valores que extrapolem o limite inferior lógico de 0.
# Entrada : valor requisitado
# Saída: valor que possa ser utilizado (não seja inferior à 0)
def retirar_impossivel(valor):
    while valor < 0:
        print("Valor inferior à 0, impossível retirar nesse momento.")
        valor = int(input("Insira o valor novamente: "))
    return valor


# Função semelhante à retirar_impossivel, porém esta também usa como parâmetro a variável de adicionar/remover ao total.
# Entrada : dinheiro e variável que armazena o quanto deseja adicionar/remover
# Saída: dinheiro total (impossível ser inferior à 0)
def operar_dinheiro(dinheiro, adicionar_remover):
    while dinheiro + adicionar_remover < 0:
        print("Isso é impossível de se realizar, tente outra vez...")
        adicionar_remover = int(input("Quanto deseja adicionar/remover? "))
    total = dinheiro + adicionar_remover
    return total


# Dados Iniciais da máquina

opcao_admin = 0
preco_pix = []
numeros_pix = []
preco_bebida = 4
troco_025_int = 0
troco_050_int = 0
troco_1_int = 0
troco_2_int = 0
troco_5_int = 0
troco_10_int = 0
troco_20_int = 0
dinheiro_cliente = 0

# Entrada do dinheiro de inicialização

print("Insira as cédulas, moedas e bebidas iniciais da máquina...")
contador_moedas_25centavos = retirar_impossivel(int(input("Quantas moedas de 25 centavos deseja colocar? ")))
contador_moedas_50centavos = retirar_impossivel(int(input("Quantas moedas de 50 centavos deseja colocar? ")))
contador_moedas_1real = retirar_impossivel(int(input("Quantas moedas de 1 real deseja colocar? ")))
contador_cedulas_2reais = retirar_impossivel(int(input("Quantas cédulas de 2 reais deseja colocar? ")))
contador_cedulas_5reais = retirar_impossivel(int(input("Quantas cédulas de 5 reais deseja colocar? ")))
contador_cedulas_10reais = retirar_impossivel(int(input("Quantas cédulas de 10 reais deseja colocar? ")))
contador_cedulas_20reais = retirar_impossivel(int(input("Quantas cédulas de 20 reais deseja colocar? ")))
contador_bebidas = retirar_impossivel(int(input("Quantas bebidas deseja colocar? ")))
exibir_quantias(contador_moedas_25centavos, contador_moedas_50centavos, contador_moedas_1real, contador_cedulas_2reais, contador_cedulas_5reais, contador_cedulas_10reais, contador_cedulas_20reais, contador_bebidas)

# Menu principal da máquina de refrigerantes

print("Inicializando menu de usuário...")
while opcao_admin != 5:
    perfil = int(input("Desejar acessar a máquina como 1-ADMIN 2-CLIENTE "))
    if perfil == 1:

        # Mostra os valores presentes na máquina para cédulas/moedas e quantidade de bebidas.

        exibir_quantias(contador_moedas_25centavos, contador_moedas_50centavos, contador_moedas_1real, contador_cedulas_2reais, contador_cedulas_5reais, contador_cedulas_10reais, contador_cedulas_20reais, contador_bebidas)
        print("Totalizando R$", "%.2f" % ((contador_moedas_25centavos * 0.25) + (contador_moedas_50centavos * 0.5) + contador_moedas_1real + (contador_cedulas_2reais * 2) + (contador_cedulas_5reais * 5) + (contador_cedulas_10reais * 10) + (contador_cedulas_20reais * 20)))
        exibir_menu()
        opcao_admin = int(input("Insira uma opção: "))
        while opcao_admin != 4:
            if opcao_admin != 1 and opcao_admin != 2 and opcao_admin != 3 and opcao_admin != 5:

                # Proteção contra inputs inteiros inválidos.

                print("Você inseriu uma opção inexistente...")
                print("Voltando ao menu...")
                opcao_admin = 4

            elif opcao_admin == 1:

                # Permite a adição/remoção de dinheiro pelo ADMIN

                adicionar_remover_25centavos = int(input("Quantas moedas de 25 centavos deseja Adicionar/Remover? "))
                contador_moedas_25centavos = operar_dinheiro(contador_moedas_25centavos, adicionar_remover_25centavos)
                adicionar_remover_25centavos = 0
                adicionar_remover_50centavos = int(input("Quantas moedas de 50 centavos deseja Adicionar/Remover? "))
                contador_moedas_50centavos = operar_dinheiro(contador_moedas_50centavos, adicionar_remover_50centavos)
                adicionar_remover_50centavos = 0
                adicionar_remover_1real = int(input("Quantas moedas de 1 real deseja Adicionar/Remover? "))
                contador_moedas_1real = operar_dinheiro(contador_moedas_1real, adicionar_remover_1real)
                adicionar_remover_1real = 0
                adicionar_remover_2reais = int(input("Quantas cédulas de 2 reais deseja Adicionar/Remover? "))
                contador_cedulas_2reais = operar_dinheiro(contador_cedulas_2reais, adicionar_remover_2reais)
                adicionar_remover_2reais = 0
                adicionar_remover_5reais = int(input("Quantas cédulas de 5 reais deseja Adicionar/Remover? "))
                contador_cedulas_5reais = operar_dinheiro(contador_cedulas_5reais, adicionar_remover_5reais)
                adicionar_remover_5reais = 0
                adicionar_remover_10reais = int(input("Quantas cédulas de 10 reais deseja Adicionar/Remover? "))
                contador_cedulas_10reais = operar_dinheiro(contador_cedulas_10reais, adicionar_remover_10reais)
                adicionar_remover_10reais = 0
                adicionar_remover_20reais = int(input("Quantas cédulas de 20 reais deseja Adicionar/Remover? "))
                contador_cedulas_20reais = operar_dinheiro(contador_cedulas_20reais, adicionar_remover_20reais)
                adicionar_remover_20reais = 0
                exibir_quantias(contador_moedas_25centavos, contador_moedas_50centavos, contador_moedas_1real, contador_cedulas_2reais, contador_cedulas_5reais, contador_cedulas_10reais, contador_cedulas_20reais, contador_bebidas)
                print("Valor atualizado R$", "%.2f" % ((contador_moedas_25centavos * 0.25) + (contador_moedas_50centavos * 0.5) + contador_moedas_1real + (contador_cedulas_2reais * 2) + (contador_cedulas_5reais * 5) + (contador_cedulas_10reais * 10) + (contador_cedulas_20reais * 20)))
                exibir_menu()
                opcao_admin = int(input("Insira uma opção: "))
            elif opcao_admin == 3:

                # Checagem de histórico PIX - Números Telefônicos e Valores

                print("Histórico de pagamentos PIX:")
                if numeros_pix == []:
                    print("Não há pagamentos PIX registrados")
                else:
                    for cont_mostrar_pagamentos_pix in range(len(numeros_pix)):
                        print(numeros_pix[cont_mostrar_pagamentos_pix], "- R$ " "%.2f" % preco_pix[cont_mostrar_pagamentos_pix])
                exibir_menu()
                opcao_admin = int(input("Insira uma opção: "))

            elif opcao_admin == 2:

                # Mostra o total de bebidas e permite adição/remoção das mesmas.

                print("Total de bebidas na máquina:", contador_bebidas)
                adicionar_remover_bebidas = int(input("Quantas bebidas deseja Adicionar/Remover? "))
                if contador_bebidas + adicionar_remover_bebidas < 0:
                    while contador_bebidas + adicionar_remover_bebidas < 0:
                        print("Isso é impossível de se realizar, tente outra vez...")
                        adicionar_remover_bebidas = int(input("Quantas bebidas deseja Adicionar/Remover? "))
                contador_bebidas = contador_bebidas + adicionar_remover_bebidas
                print("Total atualizado de bebidas na máquina:", contador_bebidas)
                adicionar_remover_bebidas = 0
                exibir_menu()
                opcao_admin = int(input("Insira uma opção: "))
            elif opcao_admin == 5:

                # Encerra as atividades da máquina
                break

    elif perfil == 2:

        # Acesso ao menu Cliente / Informa a quantidade de bebidas e o preço unitário

        print("Menu do Cliente...")
        print("Há", contador_bebidas, "bebida(s) na máquina e cada uma custa R$", "%.2f" % preco_bebida)
        if (contador_moedas_25centavos * 0.25) + (contador_moedas_50centavos * 0.5) + contador_moedas_1real + (contador_cedulas_2reais * 2) + (contador_cedulas_5reais * 5) + (contador_cedulas_10reais * 10) + (contador_cedulas_20reais * 20) == 0:
            print("Não há dinheiro na máquina, o pagamento deve ser feito apenas em PIX até que o ADMIN adicione cédulas/moedas")
        if contador_bebidas > 0:
            opcao_cliente = int(input("Deseja comprar? 1-SIM 2-NÃO "))
            if opcao_cliente == 1:

                # Pergunta ao cliente a quantidade de bebidas desejada e informa o preço total.

                quantidade_bebidas = retirar_impossivel(int(input("Quantas bebidas deseja comprar? ")))
                while quantidade_bebidas == 0:
                    print ("Digite uma quantia diferente de 0!")
                    quantidade_bebidas = retirar_impossivel(int(input("Quantas bebidas deseja comprar? ")))
                while quantidade_bebidas > contador_bebidas:
                    print("Não há bebidas suficientes, compre a quantia disponivel e peça ao admin para adicionar mais")
                    quantidade_bebidas = retirar_impossivel(int(input("Quantas bebidas deseja comprar? ")))
                custo_bebidas = preco_bebida * quantidade_bebidas
                print("Preço total de R$", "%.2f" % custo_bebidas)

                # Forma de Pagamento PIX/DINHEIRO

                if (contador_moedas_25centavos * 0.25) + (contador_moedas_50centavos * 0.5) + contador_moedas_1real + (contador_cedulas_2reais * 2) + (contador_cedulas_5reais * 5) + (contador_cedulas_10reais * 10) + (contador_cedulas_20reais * 20) == 0:
                    print("Pagamento via PIX...")
                    opcao_pagamento = 2
                else:
                    print("Forma de pagamento:")
                    opcao_pagamento = int(input("Qual será a forma de pagamento: 1-DINHEIRO 2-PIX "))
                while opcao_pagamento != 1 and opcao_pagamento != 2:
                    print("Digite uma forma de pagamento válida!")
                    opcao_pagamento = int(input("Qual será a forma de pagamento: 1-DINHEIRO 2-PIX "))
                if opcao_pagamento == 1:

                    # Controle de cédulas/moedas na relação cliente - máquina

                    while dinheiro_cliente < custo_bebidas:
                        cliente_moedas_25centavos = retirar_impossivel(int(input("Quantas moedas de 25 centavos deseja colocar? ")))
                        dinheiro_cliente = (cliente_moedas_25centavos * 0.25) + dinheiro_cliente
                        contador_moedas_25centavos = contador_moedas_25centavos + cliente_moedas_25centavos
                        cliente_moedas_50centavos = retirar_impossivel(int(input("Quantas moedas de 50 centavos deseja colocar? ")))
                        dinheiro_cliente = (cliente_moedas_50centavos * 0.5) + dinheiro_cliente
                        contador_moedas_50centavos = contador_moedas_50centavos + cliente_moedas_50centavos
                        cliente_moedas_1real = retirar_impossivel(int(input("Quantas moedas de 1 real deseja colocar? ")))
                        dinheiro_cliente = cliente_moedas_1real + dinheiro_cliente
                        contador_moedas_1real = contador_moedas_1real + cliente_moedas_1real
                        cliente_cedulas_2reais = retirar_impossivel(int(input("Quantas cédulas de 2 reais deseja colocar? ")))
                        dinheiro_cliente = (cliente_cedulas_2reais * 2) + dinheiro_cliente
                        contador_cedulas_2reais = contador_cedulas_2reais + cliente_cedulas_2reais
                        cliente_cedulas_5reais = retirar_impossivel(int(input("Quantas cédulas de 5 reais deseja colocar? ")))
                        dinheiro_cliente = (cliente_cedulas_5reais * 5) + dinheiro_cliente
                        contador_cedulas_5reais = contador_cedulas_5reais + cliente_cedulas_5reais
                        cliente_cedulas_10reais = retirar_impossivel(int(input("Quantas cédulas de 10 reais deseja colocar? ")))
                        dinheiro_cliente = (cliente_cedulas_10reais * 10) + dinheiro_cliente
                        contador_cedulas_10reais = contador_cedulas_10reais + cliente_cedulas_10reais
                        cliente_cedulas_20reais = retirar_impossivel(int(input("Quantas cédulas de 20 reais deseja colocar? ")))
                        dinheiro_cliente = (cliente_cedulas_20reais * 20) + dinheiro_cliente
                        contador_cedulas_20reais = contador_cedulas_20reais + cliente_cedulas_20reais
                        print("Você inseriu R$", "%.2f" % dinheiro_cliente)
                        if dinheiro_cliente < custo_bebidas:
                            print("Valor insuficiente, insira mais cédulas/moedas")
                        else:

                            # Cálculo do troco e seleção de cédulas/moedas de forma eficiente.

                            troco = dinheiro_cliente - custo_bebidas
                            if troco > 0:
                                print("Troco de R$", "%.2f" % troco)
                                if troco >= 20:
                                    if int(troco/20) < contador_cedulas_20reais:
                                        troco_20_int = int(troco/20)
                                        troco = troco - (troco_20_int*20)
                                        contador_cedulas_20reais = contador_cedulas_20reais - troco_20_int
                                    else:
                                        troco_20_int = contador_cedulas_20reais
                                        troco = troco - (contador_cedulas_20reais*20)
                                        contador_cedulas_20reais = 0
                                if troco >= 10:
                                    if int(troco/10) < contador_cedulas_10reais:
                                        troco_10_int = int(troco/10)
                                        troco = troco - (troco_10_int*10)
                                        contador_cedulas_10reais = contador_cedulas_10reais - troco_10_int
                                    else:
                                        troco_10_int = contador_cedulas_10reais
                                        troco = troco - (contador_cedulas_10reais*10)
                                        contador_cedulas_10reais = 0
                                if troco >= 5:
                                    if int(troco/5) < contador_cedulas_5reais:
                                        troco_5_int = int(troco/5)
                                        troco = troco - (troco_5_int*5)
                                        contador_cedulas_5reais = contador_cedulas_5reais - troco_5_int
                                    else:
                                        troco_5_int = contador_cedulas_5reais
                                        troco = troco - (contador_cedulas_5reais*5)
                                        contador_cedulas_5reais = 0
                                if troco >= 2:
                                    if int(troco/2) < contador_cedulas_2reais:
                                        troco_2_int = int(troco/2)
                                        troco = troco - (troco_2_int*2)
                                        contador_cedulas_2reais = contador_cedulas_2reais - troco_2_int
                                    else:
                                        troco_2_int = contador_cedulas_2reais
                                        troco = troco - (contador_cedulas_2reais*2)
                                        contador_cedulas_2reais = 0
                                if troco >= 1:
                                    if int(troco) < contador_moedas_1real:
                                        troco_1_int = int(troco)
                                        troco = troco - troco_1_int
                                        contador_moedas_1real = contador_moedas_1real - troco_1_int
                                    else:
                                        troco_1_int = contador_moedas_1real
                                        troco = troco - (contador_moedas_1real*1)
                                        contador_moedas_1real = 0
                                if troco >= 0.5:
                                    if int(troco / 0.5) < contador_moedas_50centavos:
                                        troco_050_int = int(troco / 0.5)
                                        troco = troco - (troco_050_int * 0.5)
                                        contador_moedas_50centavos = contador_moedas_50centavos - troco_050_int
                                    else:
                                        troco_050_int = contador_moedas_50centavos
                                        troco = troco - (contador_moedas_50centavos * 0.5)
                                        contador_moedas_50centavos = 0
                                if troco >= 0.25:
                                    if int(troco / 0.25) < contador_moedas_25centavos:
                                        troco_025_int = int(troco / 0.25)
                                        troco = troco - (troco_025_int * 0.25)
                                        contador_moedas_25centavos = contador_moedas_25centavos - troco_025_int
                                    else:
                                        troco_025_int = contador_moedas_25centavos
                                        troco = troco - (contador_moedas_25centavos * 0.25)
                                        contador_moedas_25centavos = 0
                                if troco == 0:

                                    # Caso a variável troco seja 0, a máquina foi capaz de devolver o troco ao cliente.

                                    print("Bebida(s) no dispenser")
                                    print("Seu troco está no depósito")
                                    print("Há", troco_025_int, "moeda(s) de 25 centavos no depósito")
                                    print("Há", troco_050_int, "moeda(s) de 50 centavos no depósito")
                                    print("Há", troco_1_int, "moeda(s) de 1 real no depósito")
                                    print("Há", troco_2_int, "cédula(s) de 2 reais no depósito")
                                    print("Há", troco_5_int, "cédula(s) de 5 reais no depósito")
                                    print("Há", troco_10_int, "cédula(s) de 10 reais no depósito")
                                    print("Há", troco_20_int, "cédula(s) de 20 reais no depósito")

                                    # Zerando o troco de cada cédula/moeda para transações futuras

                                    troco_025_int = 0
                                    troco_050_int = 0
                                    troco_1_int = 0
                                    troco_2_int = 0
                                    troco_5_int = 0
                                    troco_10_int = 0
                                    troco_20_int = 0
                                    contador_bebidas = contador_bebidas - quantidade_bebidas

                                else:

                                    # Máquina não conseguiu gerar troco, devolvendo dinheiro ao cliente e restaurando os
                                    # contadores do sistema

                                    print("Não há troco disponível para você, chame o admin para adicionar mais dinheiro à máquina")
                                    contador_moedas_25centavos = contador_moedas_25centavos + troco_025_int - cliente_moedas_25centavos
                                    contador_moedas_50centavos = contador_moedas_50centavos + troco_050_int - cliente_moedas_50centavos
                                    contador_moedas_1real = contador_moedas_1real + troco_1_int - cliente_moedas_1real
                                    contador_cedulas_2reais = contador_cedulas_2reais + troco_2_int - cliente_cedulas_2reais
                                    contador_cedulas_5reais = contador_cedulas_5reais + troco_5_int - cliente_cedulas_5reais
                                    contador_cedulas_10reais = contador_cedulas_10reais + troco_10_int - cliente_cedulas_10reais
                                    contador_cedulas_20reais = contador_cedulas_20reais + troco_20_int - cliente_cedulas_20reais
                                    print("Devolvendo o que você colocou..")
                                    if cliente_moedas_25centavos > 0:
                                        print("Há", cliente_moedas_25centavos, "moeda(s) de 25 centavos no depósito")
                                    if cliente_moedas_50centavos > 0:
                                        print("Há", cliente_moedas_50centavos, "moeda(s) de 50 centavos no depósito")
                                    if cliente_moedas_1real > 0:
                                        print("Há", cliente_moedas_1real, "moeda(s) de 1 real no depósito")
                                    if cliente_cedulas_2reais > 0:
                                        print("Há", cliente_cedulas_2reais, "cédula(s) de 2 reais no depósito")
                                    if cliente_cedulas_5reais > 0:
                                        print("Há", cliente_cedulas_5reais, "cédula(s) de 5 reais no depósito")
                                    if cliente_cedulas_10reais > 0:
                                        print("Há", cliente_cedulas_10reais, "cédula(s) de 10 reais no depósito")
                                    if cliente_cedulas_20reais > 0:
                                        print("Há", cliente_cedulas_20reais, "cédula(s) de 20 reais no depósito")
                                    troco_025_int = 0
                                    troco_050_int = 0
                                    troco_1_int = 0
                                    troco_2_int = 0
                                    troco_5_int = 0
                                    troco_10_int = 0
                                    troco_20_int = 0
                            else:

                                # Caso o valor inserido seja igual ao preço cobrado

                                print("Bebida no dispenser")
                                print("Não há troco")
                                contador_bebidas = contador_bebidas - quantidade_bebidas
                    dinheiro_cliente = 0
                elif opcao_pagamento == 2:

                    # Armazenamento do número do telefone do cliente e do valor total cobrado.

                    numeros_pix.append(int(input("Digite o número de telefone para pagamento via PIX: ")))
                    preco_pix.append(custo_bebidas)
                    print("Aguardando aprovação...")
                    print("Pagamento aprovado!")
                    print("Bebida(s) no dispenser")
                    contador_bebidas = contador_bebidas - quantidade_bebidas
            elif opcao_cliente == 2:
                print("Voltando ao menu...")
            else:
                print("Opção inválida, voltando ao menu...")
        else:
            print("Não há bebidas, peça ao admin para adicioná-las")
    else:
        print("Valor inválido, tente novamente...")
print("Muito obrigado por utilizar este serviço, desligando a máquina...")
