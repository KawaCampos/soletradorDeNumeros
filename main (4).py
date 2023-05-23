num1 = int(input('Digite um número: '))
ZeroANove = {
  0:["zero"], 
  1:["um", "dez", "cem","mil", ],
  2:["dois", "vinte", "duzentos","dois mil", ],
  3:["três", "trinta", "trezentos","três mil",],
  4:["quatro","quarenta","quatrocentos","quatro mil", ],
  5:["cinco", "cinquenta","quinhentos","cinco mil",],
  6:["seis", "sessenta", "seiscentos","seis mil",],
  7:["sete","setenta","setecentos","sete mil",],
  8:["oito","oitenta","oitocentos","oito mil",],
  9:["nove","noventa","novecentos","nove mil",],
  10:["dez","onze", "doze", "treze", "quatorze", "quinze","dezesseis","dezessete","dezoito","dezenove",],
  11:["dez mil", "duzentos mil","trezentos mil", "quatrocentos mil","quinhentos mil","seiscentos mil", "setecentos mil","oitocentos mil", "novecentos mil",],}
 

if num1 < 10:
  print(ZeroANove[num1][0])
elif num1 < 20:
    print(ZeroANove[10][num1%10])
elif num1 < 100:
    dezena = int(num1 / 10)
    unidade = num1 % 10
    if unidade == 0: 
        print(ZeroANove[dezena][1])
    else: 
        print(ZeroANove[dezena][1] + " e " + ZeroANove[unidade][0])
elif num1 < 1000: 
    centena = int (num1 / 100)
    dezena = num1 % 100
    unidade = num1 % 10
    if dezena == 0 and unidade == 0:
        print(ZeroANove[centena][2])
    elif unidade == 0:
        print(ZeroANove[centena][2] + " e " + ZeroANove[dezena/10][1])
    else:
        print(ZeroANove[centena][2] + " e " + ZeroANove[int(dezena/10)][1] + " e " + ZeroANove[unidade/1][0])
elif num1 >= 1000:
    milhar = int(num1 / 1000)
    centena = int(num1 / 100) % 10
    dezena = int(num1 / 10) % 10
    unidade = num1 % 10
    if centena == 0 and dezena == 0 and unidade == 0:
        print(ZeroANove[milhar][3])
    elif dezena == 0:
        print(ZeroANove[milhar][3] + " e " + ZeroANove[(centena)][2])
    elif unidade == 0:
        print(ZeroANove[milhar][3] + " e " + ZeroANove[(centena)][2] + " e " + ZeroANove[(dezena)][1])
    else:
        print(ZeroANove[milhar][3] + " e " + ZeroANove[(centena)][2] + " e " + ZeroANove[(dezena)][1] + " e " + ZeroANove[unidade/1][0])
elif num1 > 10000:
  demilhar = int(num1 / 10000) % 10
  milhar = int(num1 / 1000) % 10
  centena = int(num1 / 100) % 10
  dezena = int(num1 / 10) % 10
  unidade = num1 % 10
  if milhar == 0 and centena == 0 and dezena == 0 and unidade == 0:
    print(ZeroANove[demilhar][0])
   


