def validar(texto):
  if texto.isdigit():
    return int(texto)

  else:
    print("Letra/ Este número não é válido.")
    return None
  
def mudar(novo):
  if len(calcu) == 0:
      calcu.append(novo)

  else:
    calcu.clear()
    calcu.append(novo)


def soma():
    item = input("Quantos números deseja somar? ")
    item = validar(item)
  
    if item is None: return 0 
    somar = 0

    for a in range(item):
      numero = input(f"Digite o {a+1}º número: ")
      numero = validar(numero)

      if numero is not None:
        somar += numero
      
      print()
    print(f"A soma entre os números é {somar}")
    return somar


def sub():
    item = input("Quantos números deseja subtrair? ")
    item = validar(item)

    if item is None:
      return 0

    u = input("Digite o 1º número: ")
    u = validar(u)

    while u is None:
       print("Letra não é válida. Tente novamente.")
       u = input(f"Digite o {b+1}º número: ")
       u = validar(u)
    
    for b in range(1, item):
      n = input(f"Digite o {b+1}º número: ")
      n = validar(n)

      while n is None: 
        print("Letra não é válida. Tente novamente.")
        n = input(f"Digite o {b+1}º número: ")
        n = validar(n)
    
      u-=n
      print()
    print(f"A subtração entre os números é {u}")
    return u

def multi():
  item = input("Quantos números deseja multiplicar? ")
  item = validar(item)
  if item is None:
    return 0

  m = input("Digite o 1º número: ")
  m = validar(m)

  if m is None:
    m = 1

  for f in range(1, item):
    o = input(f"Digite o {f+1}º número: ")
    o = validar(o)

    if o is not None:
      m = m*o

    print()
  print(f"O produto entre os números é {m}")
  return m

def pot():
  p = input("Qual o primeiro número? ")
  p = validar(p)
  if p is None:
   return 0

  l = input("Qual o número a ser elevado? ")
  l = validar(l)
  if l is None:
    return 0

  popot = p**l

  print()
  print(f"A potência entre os números é {popot}")
  return popot

def div():
  j = input("Digite o dividendo: ")
  j = validar(j)
  if j is None:
    return 0
  
  w = input("Digite qual o divisor: ")
  w = validar(w)
  
  while w == 0 or w is None:
    print("Não há como dividir por 0, tente outro número")
    w = input("Digite qual o divisor: ")
    w = validar(w)
  
  tata = j/w

  print()
  print(f"A divisão entre os números é {tata}")
  return tata

def raizQ():
  q = input("Digite um número: ")
  q = validar(q)
  if q is None:
    return 0

  number = q**(1/2)

  print()
  print(f"A Raiz Quadrada entre os números é {number}")
  return number

def raizC():
  s = input("Digite um número: ")
  s = validar(s)
  if s is None:
    return 0

  numbe = s**(1/3)

  print()
  print(f"A Raiz Cúbica entre os números é {numbe}")
  return numbe


calcu = []
rascunho = []

while True:
    escolha = input("""Digite uma operação:
  [1] Soma
  [2] Subtração
  [3] Multiplicação/ Potência
  [4] Divisão
  [5] Raiz Quadrada/ Cúbica
  [6] Sair
  => """)
    escolha = validar(escolha)
    if escolha is None:
      continue

    if escolha == 1:
      resultado = soma()
      rascunho.append(resultado)
      mudar(resultado)
      print(f"Resultado atual: Somatória {calcu}")
      print(f"Rascunho acumulado: {rascunho}\n")

    elif escolha == 2:
      result = sub()
      rascunho.append(result)
      mudar(result)
      print(f"Resultado atual: Subtração {calcu}")
      print(f"Rascunho acumulado: {rascunho}\n")

    elif escolha == 3:
      opcao = ''
      while opcao != 1 and opcao != 2:
        print("Faça uma escolha")
        opcao = input("""Escolha qual deseja realizar:
        [1] Multiplicação
        [2] Potência
        => """)
        opcao = validar(opcao)

      if opcao == 1:
        resu = multi()
        rascunho.append(resu)
        mudar(resu)
        print(f"Resultado atual: Produto {calcu}")
        print(f"Rascunho acumulado: {rascunho}\n")

      elif opcao == 2:
        res = pot()
        rascunho.append(res)
        mudar(res)
        print(f"Resultado atual: Potênciação {calcu}")
        print(f"Rascunho acumulado: {rascunho}\n")

    elif escolha == 4:
      re = div()
      rascunho.append(re)
      mudar(re)
      print(f"Resultado atual: Divisão {calcu}")
      print(f"Rascunho acumulado: {rascunho}\n")

    elif escolha == 5:
      option =''
      while option != 1 and option != 2:
        print("Faça uma escolha")
        option = input("""Escolha qual deseja realizar:
        [1] Raiz Quadrada
        [2] Raiz Cúbica
        => """)
        option = validar(option)

      if option == 1:
        r = raizQ()
        rascunho.append(r)
        mudar(r)
        print(f"Resultado atual: Raiz Quadrada {calcu}")
        print(f"Rascunho acumulado: {rascunho}\n")


      elif option == 2:
        rs = raizC()
        rascunho.append(rs)
        mudar(rs)
        print(f"Resultado atual: Raiz Cúbica {calcu}")
        print(f"Rascunho acumulado: {rascunho}\n")

      else:
        print("Escolha uma das opções. ")

    elif escolha == 6:
      print("Tchau! ")
      print(f"Resultado final: {calcu}")
      print(f"Rascunho acumulado: {rascunho}\n")
      break

    else:
        print("Escolha uma das operações disponíveis\n")
