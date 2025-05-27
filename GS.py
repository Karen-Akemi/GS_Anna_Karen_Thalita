print("Bem-vindo(a) ao sistema de monitoramento diante os desastres naturais.")

desastres = []

qtd_desastres = int(input("Informe a quantidade de desastres a serem registrados: "))

for i in range(qtd_desastres):
    print(f"\nCadastro do desastre {i + 1}")

    tipo = input("Tipo de desastre (ex: incêndio, enchente, etc.): ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")

    while True:
        total = int(input("Quantidade total de pessoas afetadas: "))
        qtd_criancas = int(input("Quantidade de crianças: "))
        qtd_adultos = int(input("Quantidade de adultos: "))
        qtd_idosos = int(input("Quantidade de idosos: "))
        qtd_mob_red = int(input("Quantidade de pessoas com mobilidade reduzida: "))
        qtd_feridos = int(input("Quantidade de feridos: "))

        soma_categorias = qtd_criancas + qtd_adultos + qtd_idosos + qtd_mob_red + qtd_feridos

        if soma_categorias == total:
            break 
        else:
            print("\nA soma das categorias NÃO corresponde ao total de pessoas afetadas.")
            print("Por favor, digite os dados novamente.\n")

    desastre = [
        tipo,
        pais,
        cidade,
        bairro,
        rua,
        total,
        qtd_criancas,
        qtd_adultos,
        qtd_idosos,
        qtd_mob_red,
        qtd_feridos
    ]

    desastres.append(desastre)

qtd_criancas = sum(desastre[6] for desastre in desastres)
qtd_adultos = sum(desastre[7] for desastre in desastres)
qtd_idosos = sum(desastre[8] for desastre in desastres)
qtd_mob_red = sum(desastre[9] for desastre in desastres)
qtd_feridos = sum(desastre[10] for desastre in desastres)

totais_afetados = []

for desastre in desastres:
    totais_afetados.append(desastre[5])

maior_afetados = max(totais_afetados)

indice_maior = totais_afetados.index(maior_afetados)

total_geral = sum(totais_afetados)

categorias = {
    "crianças": qtd_criancas,
    "adultos": qtd_adultos,
    "idosos": qtd_idosos,
    "mobilidade reduzida": qtd_mob_red,
    "feridos": qtd_feridos
}

max_valor = max(categorias.values())

categorias_mais_afetadas = [categoria for categoria, valor in categorias.items() if valor == max_valor]

print("\n\nDados dos Desastres Registrados")
print(f"\nQuantidade de desastres registrados: {qtd_desastres}")
print(f"\nResumo de pessoas afetadas por categoria: \nCrianças: {qtd_criancas} | Adultos: {qtd_adultos} | Idosos: {qtd_idosos} | Mobilidade reduzida: {qtd_mob_red} | Feridos: {qtd_feridos}")


print(f"\nTotal geral de pessoas afetadas: {total_geral}")
print("Categoria(s) mais afetada(s):")
for categoria in categorias_mais_afetadas:
    print(f"] {categoria} ({max_valor} pessoas)")

print("\n\nDesastre com MAIOR número de afetados")
maior_desastre = desastres[indice_maior]
print(f"Tipo: {maior_desastre[0]}")
print(f"Localização: {maior_desastre[4]}, {maior_desastre[3]}, {maior_desastre[2]}, {maior_desastre[1]}")
print(f"Total de afetados: {maior_desastre[5]}")
