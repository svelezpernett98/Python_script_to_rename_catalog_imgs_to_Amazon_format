import os
import shutil
import pandas as pd

folder_name = ""

path_fuente = os.getcwd() + "/imagenes_nombre_maaji/"

path_no_especificadas = os.getcwd() + "/posicion_no_especificada/"

destination_XS = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_XS/'
destination_S = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_S/'
destination_M = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_M/'
destination_L = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_L/'
destination_XL = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_XL/'

fileList = os.listdir(path_fuente)

# en el diccionario guardo {lo que debe buscar: el nombre nuevo}.

dict_XS = {}
dict_S = {}
dict_M = {}
dict_L = {}
dict_XL ={}

df = pd.read_excel(os.getcwd() + "/test_excel.xlsx" ,engine='openpyxl',dtype=object,header=None)
# print(df.head())
l = df.values.tolist()
# print(l)

for row in l:
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
    

def cambiar_nombres_y_ordenar_por_carpetas(destination, diccionario, talla):
    for file in fileList:
        print(file)
        new_file_name = ""
        
        for key in diccionario:
            if file == key:
                
                if "_1.jpg" in file:
                    new_file_name = "{}.MAIN.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_2.jpg" in file:
                    new_file_name = "{}.PT01.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_3.jpg" in file:
                    new_file_name = "{}.PT02.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_4.jpg" in file:
                    new_file_name = "{}.PT03.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_5.jpg" in file:
                    new_file_name = "{}.PT04.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_6.jpg" in file:
                    new_file_name = "{}.PT05.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_7.jpg" in file:
                    new_file_name = "{}.PT06.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_8.jpg" in file:
                    new_file_name = "{}.PT07.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_9.jpg" in file:
                    new_file_name = "{}.PT08.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_10.jpg" in file:
                    new_file_name = "{}.PT09.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_11.jpg" in file:
                    new_file_name = "{}.PT10.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "_12.jpg" in file:
                    new_file_name = "{}.PT10.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))     
                    
                    
                #NOMBRES PARA POSICION NO ESPACIFICADA
                    
                elif "1.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_1.1".format(str(file).replace(".jpg", ""))
                    dest = shutil.copy(path_fuente+file, path_no_especificadas)
                    os.rename((path_no_especificadas+file), (path_no_especificadas+new_file_name+talla)) 
                    
                elif "2.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_02.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "3.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_03.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "4.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_04.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "5.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_05.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "6.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_06.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "7.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_07.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "8.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_08.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "9.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_09.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "10.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_10.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name))
                    
                elif "11.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_11.jpg".format(diccionario[key])
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
                elif "12.1.jpg" in file:
                    new_file_name = "{}.POSICION_NO_ESPECIFICADA_12.jpg".format(diccionario[key])       
                    dest = shutil.copy(path_fuente+file, destination)
                    os.rename((destination+file), (destination+new_file_name)) 
                    
        
cambiar_nombres_y_ordenar_por_carpetas(destination_XS, dict_XS, "_XS")
cambiar_nombres_y_ordenar_por_carpetas(destination_S, dict_S, "S")
cambiar_nombres_y_ordenar_por_carpetas(destination_M, dict_M, "M")
cambiar_nombres_y_ordenar_por_carpetas(destination_L, dict_L, "L")
cambiar_nombres_y_ordenar_por_carpetas(destination_XL, dict_XL, "XL")