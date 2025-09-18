temperatura = (float(input("Digite a temperatura:")))
umidade = (float (input("Digite a umidade:")))

if temperatura > 25 and umidade > 60:
    print ("AR QUENTE E ÚMIDO!!")
if temperatura > 25 and umidade < 60:
    print ("AR QUENTE E SECO!!")
if temperatura <= 25 and umidade > 60:
    print ("AR FRIO E ÚMIDO!!")
if temperatura <= 25 and umidade < 60:
    print ("AR FRIO E SECO!!")