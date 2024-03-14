# entrada de dados
N1 = float(input ("nota 1: "))
N2 = float(input ("nota 2: "))
N3 = float(input ("nota 3: "))
N4 = float(input ("nota 4: "))

MA = (N1+N2+N3+N4)*4
if MA>=10: print(MA, "aprovado")
elif MA>=7 and MA<=10: print(MA, "parabéns")
else: print ("reprovado")