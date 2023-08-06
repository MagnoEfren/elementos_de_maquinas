
def interpolate(x_values, y_values, x):
    """
    Realiza la interpolación lineal de un valor dado.
    Args:
        x_values (list): Lista de los valores x conocidos.
        y_values (list): Lista de los valores y conocidos.
        x (float): Valor a interpolar.
    Returns:
        float: Valor interpolado correspondiente a x.
    """
    n = len(x_values)
    if n != len(y_values):
        raise ValueError("Las listas de valores x e y deben tener la misma longitud.")    
    for i in range(1, n):
        if x < x_values[i]:
            # Realizar la interpolación lineal
            slope = (y_values[i] - y_values[i-1]) / (x_values[i] - x_values[i-1])
            interpolated_value = y_values[i-1] + slope * (x - x_values[i-1])
            return interpolated_value    
    # Si x es mayor que todos los valores x conocidos, devolver el último valor y
    return y_values[-1]

def interpolate_uno(x0,x,x1,y0,y1):
    y = round(y0 + ((y1-y0)/(x1-x0))*(x-x0), 4)
    return y
    
if __name__ == "__main__":
    pass