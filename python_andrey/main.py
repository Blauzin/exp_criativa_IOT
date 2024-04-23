def f(x):
  return (x ** 2)

def g(x):
  return (x - 1)


for _ in range(3):
  x = int(input("Digite um valor para x: "))

  f_de_f = f(f(x))
  
  g_de_g = g(g(x))

  f_de_g = f(g(x))

  g_de_f = g(f(x))

  print(f"função f = x²")
  print(f"função g = x - 1")

  print(f"F ° F: {f_de_f}")
  print(f"G ° G: {g_de_g}")
  print(f"F ° G: {f_de_g}")
  print(f"G ° F: {g_de_f}")