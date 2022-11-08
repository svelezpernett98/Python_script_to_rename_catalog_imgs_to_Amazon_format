#EN IMAGENES_LISTAS CREA LAS CARPETAS PARA CADA REF. MAAJI Y SU TALL Y DENTRO DE ESTA LAS IMAGENES RESPECTIVA

import os
import shutil
import pandas as pd

path_fuente = os.getcwd() + "/imagenes_nombre_maaji/"

fileList = os.listdir(path_fuente)

dict_XS = {}
dict_S = {}
dict_M = {}
dict_L = {}
dict_XL ={}

df = pd.read_excel(os.getcwd() + "/test_excel.xlsx" ,engine='openpyxl',dtype=object,header=None)
l = df.values.tolist()


for row in l[1:]:
    # print(row)
    if isinstance(row[1], str):
        dict_XS[str(row[0])] = str(row[1])
    
    
    if isinstance(row[2], str):
        dict_S[str(row[0])] = str(row[2])
    
    
    if isinstance(row[3], str):
        dict_M[str(row[0])] = str(row[3])
    
    
    if isinstance(row[4], str):
        dict_L[str(row[0])] = str(row[4])
    
    
    if isinstance(row[5], str):
        dict_XL[str(row[0])] = str(row[5])
        

def cambiar_nombres_y_ordenar_por_carpetas(diccionario, talla):
    for file in fileList:
        # print(file)
        new_file_name = "" 
        
        for key in diccionario:
            if file == key:
                if "_1.jpg" in file:
                    new_file_name = "{}.MAIN.jpg".format(diccionario[key])
                    
                elif "_2.jpg" in file:
                    new_file_name = "{}.PT01.jpg".format(diccionario[key])
                    
                elif "_3.jpg" in file:
                    new_file_name = "{}.PT02.jpg".format(diccionario[key])
                    
                elif "_4.jpg" in file:
                    new_file_name = "{}.PT03.jpg".format(diccionario[key])
                    
                elif "_5.jpg" in file:
                    new_file_name = "{}.PT04.jpg".format(diccionario[key])
                    
                elif "_6.jpg" in file:
                    new_file_name = "{}.PT05.jpg".format(diccionario[key])
                    
                elif "_7.jpg" in file:
                    new_file_name = "{}.PT06.jpg".format(diccionario[key])
                    
                elif "_8.jpg" in file:
                    new_file_name = "{}.PT07.jpg".format(diccionario[key])
                    
                elif "_9.jpg" in file:
                    new_file_name = "{}.PT08.jpg".format(diccionario[key])
                    
                elif "_10.jpg" in file:
                    new_file_name = "{}.PT09.jpg".format(diccionario[key])
                    
                elif "_11.jpg" in file:
                    new_file_name = "{}.PT10.jpg".format(diccionario[key])
                    
                elif "_12.jpg" in file:
                    new_file_name = "{}.PT10.jpg".format(diccionario[key])
                    
                    
                #NOMBRES PARA POSICION NO ESPACIFICADA
                
                elif "1.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_01.jpg".format(diccionario[key])
                
                elif "2.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_02.jpg".format(diccionario[key])
                    
                elif "3.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_03.jpg".format(diccionario[key])
                    
                elif "4.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_04.jpg".format(diccionario[key])
                    
                elif "5.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_05.jpg".format(diccionario[key])
                    
                elif "6.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_06.jpg".format(diccionario[key])
                    
                elif "7.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_07.jpg".format(diccionario[key])
                    
                elif "8.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_08.jpg".format(diccionario[key])
                    
                elif "9.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_09.jpg".format(diccionario[key])
                    
                elif "10.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_10.jpg".format(diccionario[key])
                    
                elif "11.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_11.jpg".format(diccionario[key])
                    
                elif "12.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_12.jpg".format(diccionario[key])
                    
                print(file)
                start = file.find("_", file.find("_")+1)
                var_final = file[:start]
                print(var_final)
                directory = var_final + talla
                parent_dir = os.getcwd() + "/" + "imagenes_listas/"
                destination_fileList = os.listdir(parent_dir)
                
                if directory not in destination_fileList:
                    new_folder = os.path.join(parent_dir, directory)
                    os.mkdir(new_folder)
                    dest = shutil.copy(path_fuente+file, parent_dir+directory)
                    os.rename((parent_dir+directory+"/"+file), (parent_dir+directory+"/"+new_file_name))
                    
                else:
                    dest = shutil.copy(path_fuente+file, parent_dir+directory)
                    os.rename((parent_dir+directory+"/"+file), (parent_dir+directory+"/"+new_file_name))
        
        
cambiar_nombres_y_ordenar_por_carpetas(dict_XS, "_XS")
cambiar_nombres_y_ordenar_por_carpetas(dict_S, "_S")
cambiar_nombres_y_ordenar_por_carpetas(dict_M, "_M")
cambiar_nombres_y_ordenar_por_carpetas(dict_L, "_L")
cambiar_nombres_y_ordenar_por_carpetas(dict_XL, "_XL")
