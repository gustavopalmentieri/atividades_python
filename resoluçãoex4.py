funcionarios = []
nome = input("Digite um nome:")
setor = input("Digite o setor:")
periodo = input("Digite o período:")


for i in range(3):

    dic = {}
    dic ["nome"] = nome
    dic ["setor"] = setor
    dic["periodo"] = periodo

    print ("O funcionário", dic ["nome"], "trabalha no setor", dic ["setor"], "e no período", dic ["periodo"])
