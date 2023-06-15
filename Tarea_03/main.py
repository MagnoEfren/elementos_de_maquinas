# importacion de las librerias
from datetime import datetime
import numpy as np 
import pandas as pd
df = pd.read_excel('datos.xlsx')  # Lectura del archivo excel
# Lectura de las columnas usadas y convertidas a lista.
material = df.iloc[0:, 1].tolist()
procesamiento = df.iloc[0:, 2].tolist()
fluencia_mpa = df.iloc[0:, 5].tolist()
fluencia_kpsi = df.iloc[0:, 6].tolist()
estado = []  # Lista para alamacenar si falla o no el material 
while True:
    tipo_unidades = str(input('\nIngrese el número que desea:\n1. Unidades SI\n2. Unidades Inglesas\n3. Salir \n --> '))
    if tipo_unidades == '1' or tipo_unidades== '2': 
        try: 
            sigma_x = float(input('Ingrese el esfuerzo en X: '))
            sigma_y = float(input('Ingrese el esfuerzo en Y: '))
            sigma_z = float(input('Ingrese el esfuerzo en Z: '))
            Tau_xy = float(input('Ingrese el esfuerzo cortante en XY: '))
            Tau_yz = float(input('Ingrese el esfuerzo cortante en YZ: '))
            Tau_zx = float(input('Ingrese el esfuerzo cortante en ZX: '))
            N = float(input('Ingrese el Factor de Seguridad: '))
            break
        except ValueError:
            print('Ingrese valores validos')
    elif tipo_unidades == '3':
        break
    else:
        print("Entrada inválida. Intente de nuevo.")

     # Creamos un archivo Excel con los datos y lo guardamos en disco
if tipo_unidades == '1' or tipo_unidades== '2':
    sigma = np.sqrt(1/2*((sigma_x-sigma_y)**2 + (sigma_y - sigma_z)**2 +(sigma_z-sigma_x)**2)+ 3*(Tau_xy**2 + Tau_yz**2 + Tau_zx**2))
    if tipo_unidades == '1':   
        for dato in fluencia_mpa:   
            if sigma > (dato*1000000)/N:      
                estado.append('Falla')
            else:
                estado.append('No Falla')
    elif tipo_unidades == '2':
        for dato in fluencia_kpsi:   
            if sigma > (dato*1000)/N:      
                estado.append('Falla')
            else:
                estado.append('No Falla')
    else:
        print('Error, Debe Ingresar el numero 1 o 2')

    #Creamos una lista de valores para agregar al excel
    sigma_x_list  = [sigma_x]*23
    sigma_y_list = [sigma_y]*23
    sigma_z_list = [sigma_z]*23
    Tau_xy_list = [Tau_xy]*23
    Tau_yz_list = [Tau_yz]*23
    Tau_zx_list = [Tau_zx]*23
    N_list = [N]*23

    datos = {
            'Sigma_x': sigma_x_list,
            'Sigma_y': sigma_y_list,
            'Sigma_z': sigma_z_list,
            'Tau_xy': Tau_xy_list,
            'Tau_yz': Tau_yz_list,
            'Tau_zx': Tau_zx_list,
            'Factor de Seguridad': N_list,
            'Material':material, 
            'Procesamiento':procesamiento, 
            'Resistencia a la Fluencia(MPa)':fluencia_mpa, 
            'Resistencia a la Fluencia(kpsi)':fluencia_kpsi,
            'Estado': estado,
             }

    df = pd.DataFrame(datos, columns =  [
                                        'Sigma_x',
                                        'Sigma_y',
                                        'Sigma_z',
                                        'Tau_xy',
                                        'Tau_yz',
                                        'Tau_zx',
                                        'Factor de Seguridad',
                                        'Material', 
                                        'Procesamiento', 
                                        'Resistencia a la Fluencia(MPa)', 
                                        'Resistencia a la Fluencia(kpsi)', 
                                        'Estado'
                                         ])
    # Guarda el archivo Excel con las columnas ajustadas y centradas
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    print(estado)
    df.to_excel(f'DATOS {fecha_actual}.xlsx')
    print('DATOS GUARDADOS CORRECTAMENTE')
