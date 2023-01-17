def neurona(x, w)-> float:
  try: 
    return w * x
  except ValueError:
    print("El valor debe ser numérico")


def neurona2(x1, x2, w1,w2)-> float:
  try: 
    x_values = [x1, x2]
    return (x_values[0] * w1) + (x_values[1] * w2)
  except ValueError:
    print("El valor debe ser numérico")


def biased(X0, X1, X2, w0, w1, w2,  bias) -> float:
  try:
    pesos = [w0, w1, w2]
    
    entrada = [X0, X1, X2]
    return (entrada[0] * pesos[0]) + (entrada[1] * pesos[1]) + (entrada[2] * pesos[2])  + bias
  except:
    ValueError("Debes introducir números")