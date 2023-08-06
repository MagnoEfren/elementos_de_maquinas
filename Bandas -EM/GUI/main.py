# LABORATORIO SEMANA 11
# Integrantes:
# Araujo Rodriguez Magno Efren
# Garay Alcantara Alex
# Victorio Esteban Edwin
# Ventura Yaipen Bryan

from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from interpolador import interpolate, interpolate_uno
from datetime import datetime
import pandas as pd
import numpy as np
import math
import sys
from design import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_calcular.clicked.connect(self.calculation)
        self.bt_save_data.clicked.connect(self.save_data)
        self.tablas(self.tableWidget_9,'17-9' )
        self.tablas(self.tableWidget_10,'17-10' )
        self.tablas(self.tableWidget_11,'17-11' )
        self.tablas(self.tableWidget_12,'17-12' )
        self.tablas(self.tableWidget_13,'17-13' )
        self.tablas(self.tableWidget_14,'17-14' )
        self.tablas(self.tableWidget_15,'17-15' )
        m_imp = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-15', na_values='')
        m_imp_list = m_imp.iloc[2:, 0].tolist()
        self.comboBox.addItems(m_imp_list)
    def tablas(self, tabla, hoja):
        excel_data = pd.read_excel('Tablas_Bandas.xlsx', sheet_name=hoja)  # Lee la primera hoja (índice 0)
        excel_data.fillna('', inplace=True)
        tabla.setRowCount(excel_data.shape[0])
        tabla.setColumnCount(excel_data.shape[1])
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ancho de columna adaptable
        # Llenar la tabla con los datos de Excel
        for i in range(excel_data.shape[0]):
            for j in range(excel_data.shape[1]):
                item = QTableWidgetItem(str(excel_data.iloc[i, j]))
                tabla.setItem(i, j, item)
        tabla.resizeColumnsToContents()
        tabla.resizeRowsToContents()

    def calculation(self):
        # Datos de entrada
        Hnom = self.in_horm.value()
        n_motor = self.in_n_motor.value() 
        fac_dis = self.in_n_d.value()
        D_polea = self.in_D_polea.value()
        d_polea = self.in_d_polea.value()

        Circ_D = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-10', na_values='')
        Circ_D_list = Circ_D.iloc[0:, 3].tolist()

        Suma_D = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-11')
        Suma_D_list = Suma_D.iloc[0,1:].tolist()    
        L_aprox = 1.1*np.pi*(D_polea + d_polea)

        for i  in Circ_D_list:
            if i >=L_aprox:
                Circ = i
                self.label_17_10.setText(f'EL VALOR SELECCIONADO FUE: {str(i)} DE LA BANDA TIPO "D"')  # mostramos el valor seleccionado
                break
        Lp = Circ + Suma_D_list[3]
        self.label_17_11.setText(f'EL VALOR SELECCIONADO FUE: {str(Suma_D_list[3])} ') # mostramos el valor seleccionado
        C = round(0.25*(Lp-np.pi/2*(D_polea+d_polea)+((Lp-np.pi/2*(D_polea+d_polea))**2-2*(D_polea-d_polea)**2)**0.5),3) #DIAMETRO C 
        if C > D_polea and C < 3*(D_polea+d_polea):
            print("-> Este valor para C está en el rango adecuado")
        elif C < D_polea: #3*(D_polea+d_polea):
            pass
            # seleccionar un Circ anterior 
        else:
            print('Intentelo De nuevo')
        #  CALCULAR KTETHA Y KL:
        k1_D = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-13')
        k1_D_list = k1_D.iloc[1:,2].tolist()
        D_d_list = k1_D.iloc[1:,0].tolist() 
        # De la tabla 17-13 obtenemos KTetha (k1)
        D_d = round((D_polea-d_polea)/C, 5)
        k1 = interpolate(D_d_list,k1_D_list,D_d) 
        self.label_17_13.setText(f'EL VALOR DE K1 FUE: {str(k1)} ')
        self.label_17_9.setText(f'SELECCION DE BANDA TIPO "D"')
        #  De la tabla 17-14 obtenemos KL (K2)
        # De la bada D verificamos el rango y obtenemos el numero (Factor de longitud)
        L_nominal = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-14')
        factor_L_list = L_nominal.iloc[1:,0].tolist()
        L_nominal_list = L_nominal.iloc[1:,4].tolist()

        k2 = 1 # valor inicial por defecto
        if Lp < 128:
            k2 = factor_L_list[0]
        elif Lp >= 540:
            k2 = factor_L_list[-1]
        else:
            for rango in L_nominal_list:
                if isinstance(rango, int):
                    if Lp == rango:
                        k2 = factor_L_list[L_nominal_list.index(rango) + 1]
                        break
                else:
                    inicio, fin = map(int, rango.split('-'))
                    if Lp >= inicio and Lp <= fin:
                        k2 = factor_L_list[L_nominal_list.index(rango)]
                        break
        self.label_17_14.setText(f'EL FACTOR DE LONGITUD SELECCIONADO FUE: {str(k2)} n BANDA TIPO "D"')
        V = (np.pi*d_polea*n_motor)/(12)
        # De la tabla 17-12 Ingresamos con velocidad  de linea (V) , y d_polea para obtener H_tab
        V_banda = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-12')
        #d_polea_list = V_banda.iloc[23:31, 1].tolist()
        #vel_list = V_banda.iloc[0, 2:].tolist()
        v_1000_list = [1000]+V_banda.iloc[23:31, 2].tolist()
        v_2000_list = [2000]+V_banda.iloc[23:31, 3].tolist()
        v_3000_list = [3000]+V_banda.iloc[23:31, 4].tolist()
        v_4000_list = [4000]+V_banda.iloc[23:31, 5].tolist()
        v_5000_list = [5000]+V_banda.iloc[23:31, 6].tolist()

        velocidades = [v_1000_list, v_2000_list, v_3000_list,v_4000_list,v_5000_list]

        d_f1_list = V_banda.iloc[23, 1:].tolist()
        d_f2_list = V_banda.iloc[24, 1:].tolist()
        d_f3_list = V_banda.iloc[25, 1:].tolist()
        d_f4_list = V_banda.iloc[26, 1:].tolist()
        d_f5_list = V_banda.iloc[27, 1:].tolist()
        d_f6_list = V_banda.iloc[28, 1:].tolist()
        d_f7_list = V_banda.iloc[29, 1:].tolist()
        d_f8_list = V_banda.iloc[30, 1:].tolist()
        diametros = [d_f1_list, d_f2_list, d_f3_list, d_f4_list,d_f5_list,d_f6_list,d_f7_list,d_f8_list ]

        dx,fila_if_dx,fila_sup_dx = 0,0,0
        Vx, colum_if_vx,colum_sup_vx = 0,0,0

        for i in range(9):
            if d_polea == diametros[i][0]:
                dx = diametros[i]
                break
            if  diametros[i][0] < d_polea < diametros[i+1][0]:
                fila_if_dx = diametros[i]
                fila_sup_dx = diametros[i+1]
                break
            if d_polea > diametros[-1][0]:
                dx = diametros[-1]
                break
        for i in range(6):
            if V < velocidades[0][0]:
                Vx = velocidades[0]
                break
            if V == velocidades[i][0]:
                Vx = velocidades[i]
                break
            if  velocidades[i][0] < V < velocidades[i+1][0]:
                colum_if_vx = velocidades[i]
                colum_sup_vx = velocidades[i+1]
                break
            if V > velocidades[-1][0]:
                Vx = velocidades[-1]
                break
        if Vx == 0  and dx== 0:
            x1 = list(set(colum_if_vx) & set(fila_if_dx))[0]
            x2 = list(set(colum_sup_vx) & set(fila_if_dx))[0]
            x3 = list(set(colum_if_vx) & set(fila_sup_dx))[0]
            x4 = list(set(colum_sup_vx) & set(fila_sup_dx))[0]

            self.label_17_12.setText(f'BANDA TIPO "D": \n LOS VALORES USADOS FUERON: {str(x1)}-{str(x2)}-{str(x3)}-{str(x4)}')

            Fe = ((colum_sup_vx[0] - V)/(colum_sup_vx[0]-colum_if_vx[0]))*x1 + ((V-colum_if_vx[0])/(colum_sup_vx[0]-colum_if_vx[0]))*x2
            F_f = ((colum_sup_vx[0] - V)/(colum_sup_vx[0]-colum_if_vx[0]))*x3 + ((V-colum_if_vx[0])/(colum_sup_vx[0]-colum_if_vx[0]))*x4
            H_tab = ((fila_sup_dx[0] - d_polea)/(fila_sup_dx[0]-fila_if_dx[0]))*Fe + ((d_polea - fila_if_dx[0])/(fila_sup_dx[0]-fila_if_dx[0]))*F_f

        elif Vx != 0  and dx!= 0:
            H_tab = list(set(dx) & set(Vx))[0]
            self.label_17_12.setText(f'BANDA TIPO "D": \n EL VALOR SELECCIONADO FUE: {H_tab}')
        elif Vx == 0  and dx!= 0:
            v1 = list(set(colum_if_vx) & set(dx))[0]
            v2 = list(set(colum_sup_vx) & set(dx))[0]   
            H_tab = interpolate_uno(colum_if_vx[0], V, colum_sup_vx[0], v1, v2) 
            self.label_17_12.setText(f'BANDA TIPO "D": \n LOS VALORES USADOS FUERON: {colum_if_vx[0]}-{colum_sup_vx[0]}-{str(v1)}-{str(v2)}')
        elif Vx != 0  and dx== 0:
            d1 = list(set(fila_if_dx) & set(Vx))[0]
            d2 = list(set(fila_sup_dx) & set(Vx))[0]
            H_tab = interpolate_uno(fila_if_dx[0], d_polea, fila_sup_dx[0], d1, d2) 
            self.label_17_12.setText(f'BANDA TIPO "D": \n  LOS VALORES USADOS FUERON: {fila_if_dx[0]}-{fila_sup_dx[0]}-{str(d1)}-{str(d2)}')

        Ha =  H_tab*k1*k2 # Ha (potencia admisible) de la faja

        # CALCULAMOS KS (FACTOR DE SERVICIO  DE LA TABLA  17-15)
        m_imp = pd.read_excel('Tablas_Bandas.xlsx', sheet_name='17-15', na_values='')
        m_imp_list = m_imp.iloc[2:, 0].tolist()
        v_selec = self.comboBox.currentText()
        index = m_imp_list.index(v_selec)
        if self.rb_caracteristica.isChecked():
            torsion_normal = m_imp.iloc[2:, 2].tolist()
            Ks = torsion_normal[index]
            self.label_17_15.setText(f'TIPO DE MAQUINA SELECCIONADA: {v_selec} ({Ks}) Y CON FUENTE DE POTENCIA: PAR DE TORSIÓN NORMAL')
        elif self.rb_torcion_alto.isChecked():
            torsion_alto = m_imp.iloc[2:, 4].tolist()
            Ks = torsion_alto[index]
            self.label_17_15.setText(f'TIPO DE MAQUINA SELECCIONADA: {v_selec} ({Ks}) Y CON FUENTE DE POTENCIA: PAR DE TORSIÓN ALTO')
        # Potencia de diseño:
        Hd = Hnom*Ks*fac_dis
        N_fajas = math.ceil(Hd/Ha)

        self.datos = [round(Lp,4),round(C,4), 'D' + str(int(Circ)),N_fajas,round(Ha,4),round(Hd,4),round(V,4) ]
        self.out_Lp.setText(f'Longitud de paso: {self.datos[0]} [pulg]')
        self.out_C.setText(f'Distancia entre centros: {self.datos[1]} [pulg]')
        self.out_tipo_banda.setText(f'Tipo de banda: {self.datos[2]}')
        self.out_numero_banda.setText(f'Numero de banda: {self.datos[3]}')
        self.out_Ha.setText(f'Potencia admisible de una banda: {self.datos[4]} [HP]')
        self.out_Hd.setText(f'Potencia de diseño: {self.datos[5]} [HP]')
        self.out_V.setText(f'Velocidad de linea: {self.datos[6]} [pie/min]')

    def save_data(self):
        # Datos de entrada
        Hnom = self.in_horm.value()
        n_motor = self.in_n_motor.value() 
        fac_dis = self.in_n_d.value()
        D_polea = self.in_D_polea.value()
        d_polea = self.in_d_polea.value()

        datos = {
        'Potencia [HP]': [Hnom, ],
        'Velocidad del motor [RPM]': [n_motor, ],
        'Factor de diseño': [fac_dis, ],
        'Diametro Polea mas grande': [D_polea, ],
        'Diametro Polea mas pequeña': [d_polea ],
        'Longitud de paso': [self.datos[0], ],
        'Distancia entre centros': [self.datos[1], ],
        'Tipo de banda': [self.datos[2], ],
        'Numero de banda': [self.datos[3], ], 
        'Potencia admisible de una banda': [self.datos[4], ],
        'Potencia de diseño': [self.datos[5], ], 
        'Velocidad de linea': [self.datos[6], ] }
        # Convertir los valores en DataFrames y guardarlos en una lista
        lista_dataframes = [pd.DataFrame({clave: valor}) for clave, valor in datos.items()]
        df = pd.concat(lista_dataframes, axis=1 )
        df.columns = list(datos.keys())
        try:
            filename = QFileDialog.getSaveFileName(None,"Save File", "", "Excel Files (*.xlsx);;All Files (*)")[0]
            if len(filename) != 0:
                df.to_excel(filename, index=True)
                print('Datos guardados correctamente')
            else:
                print('Ingrese un nombre correcto')
        except Exception as e:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())

