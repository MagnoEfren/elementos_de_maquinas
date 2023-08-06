# LABORATORIO SEMANA 13
# Integrantes:
# Araujo Rodriguez Magno Efren
# Garay Alcantara Alex
# Victorio Esteban Edwin
# Ventura Yaipen Bryan

from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.uic import loadUi
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

        self.tablas(self.tableWidget_15,'TABLA 17-15' )
        self.tablas(self.tableWidget_19_1,'TABLA 17_19_1' )
        self.tablas(self.tableWidget_19_2,'TABLA 17_19_2' )
        self.tablas(self.tableWidget_20,'TABLA 17-20' )
        self.tablas(self.tableWidget_22,'TABLA 17-22' )
        self.tablas(self.tableWidget_23,'TABLA 17-23' )

        m_imp = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-15', na_values='')
        m_imp_list = m_imp.iloc[2:, 0].tolist()
        self.comboBox.addItems(m_imp_list)
    def tablas(self, tabla, hoja):
        excel_data = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name=hoja)  # Lee la primera hoja (índice 0)
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
        Cp = self.in_C.value() 
        n_motor = self.in_n_motor.value()
        n_d = self.in_n_d.value()
        N1 = (self.in_ndientes_impulsora.value())
        Rv =  self.in_rv.value()
        N2 = N1*Rv
        # CALCULAMOS KS (FACTOR DE SERVICIO  DE LA TABLA  17-15)
        m_imp = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-15', na_values='')
        m_imp_list = m_imp.iloc[2:, 0].tolist()
        v_selec = self.comboBox.currentText()
        index = m_imp_list.index(v_selec)
        if self.rb_caracteristica.isChecked():
            torsion_normal = m_imp.iloc[2:, 2].tolist()
            Ks = torsion_normal[index]
        elif self.rb_torcion_alto.isChecked():
            torsion_alto = m_imp.iloc[2:, 4].tolist()
            Ks = torsion_alto[index]
        #(N_DIENTE_MENOR/17)**(1.08)
        k1 = (N1/17)**(1.08)
        # obtenemos el k2 de la tabla: TABLA 17-23
        tab_17_23 = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-23', na_values='')
        n_hileras_list = tab_17_23.iloc[0:, 0].tolist()     
        k2_list = tab_17_23.iloc[0:, 1].tolist()
        # Potencia de diseño
        Hd = Ks*Hnom*n_d
        H_req_list = []

        for k2 in k2_list:
            H_req_list.append(round(Hd/(k1*k2), 4))

        # obtener el Htab  TABLA 17-20
        tab_17_20A = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-20_A')
        tab_17_20B = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-20_B')
        tab_17_20C1 = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-20_C')
        tab_17_20C2 = pd.read_excel('Tablas_Cadenas.xlsx', sheet_name='TABLA 17-20_C2')

        #Convertir cada fila del DataFrame en una lista
        A_17_20 = tab_17_20A.values.tolist()
        n_ansi_list = A_17_20.pop(0)
        n_ansi_list.pop(0)
        B_17_20 = tab_17_20B.values.tolist()
        B_17_20.pop(0)
        C1_17_20 = tab_17_20C1.values.tolist()
        C1_17_20.pop(0)
        C2_17_20 = tab_17_20C2.values.tolist()
        C2_17_20.pop(0)

        # tipos de  lubricacion # A,B,C1,C2
        H_tabA = self.obtener_Htab(A_17_20, n_motor, H_req_list)
        H_tabB = self.obtener_Htab(B_17_20, n_motor, H_req_list )
        H_tabC1 = self.obtener_Htab(C1_17_20, n_motor, H_req_list )
        H_tabC2 = self.obtener_Htab(C2_17_20, n_motor, H_req_list )

        x1 = self.obtener_tabla2(H_tabA, n_ansi_list,'A') 
        x2 = self.obtener_tabla2(H_tabB, n_ansi_list,'B') 
        x3 = self.obtener_tabla2(H_tabC1, n_ansi_list,'C') 
        x4 = self.obtener_tabla2(H_tabC2, n_ansi_list,'C1') 
        hileras = x1[0] + x2[0]+ x3[0] + x4[0]
        n_ANSI = x1[1]+x2[1]+ x3[1] + x4[1]
        H_tab = x1[2]+x2[2]+ x3[2] + x4[2]
        lubr = x1[3]+x2[3]+ x3[3] + x4[3]
        Lp =  np.ceil(2*Cp + (N1+N2)/2 + (N2-N1)**2/(4*np.pi**2*Cp)) 
        list_Lp = len(lubr)*[Lp]
        list_Cp =  len(lubr)*[Cp]

        ################ tabla 1##############
        # numero de hilera, K2, req: 
        datos1 = [n_hileras_list ,k2_list, H_req_list]
        self.agregar_datos(datos1, self.tableWidget_result1)

        ############### tabla 2 ###################
        # index, #hileras, # H_tab, Tipo de lubricacion, ANSI, Lp(pasos), Lc(pasos)
        self.datos2 = [hileras, H_tab, lubr, n_ANSI, list_Lp, list_Cp]
        self.agregar_datos(self.datos2, self.tableWidget_result2)

    def obtener_tabla2(self, datos, ANSI, Lubricante):
        hileras = []
        n_ANSI = []
        H_tab = []
        lubr = []
        n = 0
        for hilera in datos:
            n +=1 
            for pos in hilera:
                if pos !=0:
                    H_tab.append(pos)
                    index = hilera.index(pos)
                    n_ANSI.append(ANSI[index])
                    if n ==7:
                        n = 8
                        hileras.append(n)
                    else:
                        hileras.append(n)
                    if Lubricante=='A':
                        lubr.append('A')
                    elif Lubricante=='B':
                        lubr.append('B')
                    elif Lubricante=='C':
                        lubr.append('C')
                    elif Lubricante=='C1':
                        lubr.append('C1')
        x = [hileras,n_ANSI,H_tab, lubr ]
        return  x

    def obtener_Htab(self, A_17_20, n_motor, H_req_list):
        Htab_A = []
        Htab_por_hileraA = []
        fila_a_HtabA = []
        for i in range(len(A_17_20)):
            if A_17_20[i][0] == n_motor:
                A_17_20[i].pop(0)
                fila_a_HtabA = A_17_20[i]
            elif A_17_20[i][0] < n_motor < A_17_20[i+1][0]:
                A_17_20[i+1].pop(0)
                fila_a_HtabA = A_17_20[i+1].pop(0)
        for  H_req in H_req_list :
            Htab_por_hileraA = []
            for H_tab in fila_a_HtabA:
                try:
                    if H_req < H_tab:
                        Htab_por_hileraA.append(H_tab)
                    else:
                        Htab_por_hileraA.append(0)
                except ValueError:
                    print('')
            Htab_A.append(Htab_por_hileraA)
        return Htab_A

    def agregar_datos(self, datos, tabla):
        filas = len(datos[0])
        columnas = len(datos)
        tabla.setRowCount(filas)
        tabla.setColumnCount(columnas)      
        for fila in range(filas):
            for columna in range(columnas):
                item = QTableWidgetItem(str(datos[columna][fila]))
                tabla.setItem(fila, columna, item)
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabla.resizeColumnsToContents()
        tabla.resizeRowsToContents()

    def save_data(self):
        datos = {
        '# Hileras': self.datos2[0],
        'H_req': self.datos2[1],
        'Tipo de lubricacion': self.datos2[2],
        'ANSI': self.datos2[3],
        'Lp (pasos)': self.datos2[4],
        'Lc (pasos)': self.datos2[5]}
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

