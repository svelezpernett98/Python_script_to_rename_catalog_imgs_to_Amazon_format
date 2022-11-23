import os
import shutil
import pandas as pd
import time
import sys

#ELIMINO LAS CARPETAS DE TALLAS SI EXISTE Y LAS CREO NUEVAMENTE PARA QUE QUEDEN VACIAS
dir_path = os.getcwd() + "/tallas"

try:
        shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
except:
    print("error al eliminar carpeta de tallas")
     
        
def crear_carpetas_de_tallas(talla_name):
    try:
        parent_dir = os.getcwd() + "/"
        tallas_folder = os.path.join(parent_dir, "tallas")
        os.mkdir(tallas_folder)
    except:
        print("carpeta talla ya existe")
        
    tallas2_folder = parent_dir + "tallas/"
    tallas_individual_folder = os.path.join(tallas2_folder, talla_name)
    os.mkdir(tallas_individual_folder)
    
crear_carpetas_de_tallas("talla_XS")
crear_carpetas_de_tallas("talla_S")
crear_carpetas_de_tallas("talla_M")
crear_carpetas_de_tallas("talla_L")
crear_carpetas_de_tallas("talla_XL")
crear_carpetas_de_tallas("talla_XXL")
crear_carpetas_de_tallas("talla_XXXL")
crear_carpetas_de_tallas("talla_OS")
crear_carpetas_de_tallas("talla_SM_MD")
crear_carpetas_de_tallas("talla_L_XLD")
crear_carpetas_de_tallas("talla_02")
crear_carpetas_de_tallas("talla_04")
crear_carpetas_de_tallas("talla_06")
crear_carpetas_de_tallas("talla_08")
crear_carpetas_de_tallas("talla_10")
crear_carpetas_de_tallas("talla_12")
crear_carpetas_de_tallas("talla_14")
crear_carpetas_de_tallas("talla_16")


#TOMO LOS DATOS DEL EXCEL Y LOS GUARDO COMO LISTA EN excel_original
df = pd.read_excel(os.getcwd() + '/Fotos_excel.xlsx' ,engine='openpyxl',dtype=object,header=None)
excel_original = df.values.tolist()

#CREO EL DICT DONDE VOY A METER LOS CODIGOS MAAJI COMO LLAVES Y LA CANTIDAD DE VECES QUE SE REPITE EN EL EXCEL,
#Y EL NOMBRE DE CADA ARCHIVO QUE LLEVA ESE CODIGO EN EL EXCEL COMO  VALUE DE ESA LLAVE DENTRO DE OTRO DICCIONARIO
dict_codigos_maaji = {}

#POR CADA FILA EN EL EXCEL, SACAR SOLO EL CODIGO MAAJI DEL NOMBRE ARCHIVO QUE ESTA EN LA POSICION [O],
#Y EL NOMBRE COMPLETO 
for row in excel_original[1:]:
    start = row[0].find("_")
    
    #CODIGO MAAJI SOLO
    codigo_maaji = row[0][:start]
    
    #NOMBRE DEL ARCHIVO COMPLETO
    nombre_archivo_completo = row[0]        
    
    #SI EL CODIGO NO SE HA AÑADIDO COMO LLAVE AL DICT, SE AÑADE Y SE LE PONE LA PRIMERA SUBLLAVE CON CATIDAD 0
    if codigo_maaji not in dict_codigos_maaji:
        dict_codigos_maaji[codigo_maaji] = {}
        dict_codigos_maaji[codigo_maaji]["cantidad"] = 0
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = 0
    
    #SI EL CODIGO YA SE HA AÑADIDO SE LE SUMA UNO A LA CANTIDAD ACTUAL Y SE LE AÑADE EL NOMBRE COMPLETO COMO OTRA
    #SUBLLAVE MAS LA CANTIDAD ACTUAL PARA QUE NO SE SOBREESCRIBA ESE DATO
    dict_codigos_maaji[codigo_maaji]["cantidad"] = dict_codigos_maaji[codigo_maaji]["cantidad"] + 1
    dict_codigos_maaji[codigo_maaji]["nombre_completo"+str(dict_codigos_maaji[codigo_maaji]["cantidad"])] = nombre_archivo_completo
    
    if "_1.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_2.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_3.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_4.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_5.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_6.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_7.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_8.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_9.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_10.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_11.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    if "_12.1" in nombre_archivo_completo:
        dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
    
    if isinstance(row[1], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_XS"] = row[1]
        
    if isinstance(row[2], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_S"] = row[2]
        
    if isinstance(row[3], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_M"] = row[3]
        
    if isinstance(row[4], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_L"] = row[4]
        
    if isinstance(row[5], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_XL"] = row[5]
        
    if isinstance(row[6], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_XXL"] = row[6]
        
    if isinstance(row[7], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_XXXL"] = row[7]
        
    if isinstance(row[8], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_OS"] = row[8]
        
    if isinstance(row[9], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_SM_MD"] = row[9]
        
    if isinstance(row[10], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_L_XLD"] = row[10]
        
    if isinstance(row[11], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_02"] = row[11]
        
    if isinstance(row[12], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_04"] = row[12]
        
    if isinstance(row[13], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_06"] = row[13]
        
    if isinstance(row[14], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_08"] = row[14]
        
    if isinstance(row[15], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_10"] = row[15]
        
    if isinstance(row[16], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_12"] = row[16]
        
    if isinstance(row[17], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_14"] = row[17]
        
    if isinstance(row[18], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_16"] = row[18]
        
# print(dict_codigos_maaji)

#RUTA DE LA CARPETA DONDE SE VAN A TOMAR LAS IMAGENES CON EL NOMBRE QUE QUEREMOS CAMBIAR, Y LISTAMOS LOS ARCHIVOS
#DE DICHO DIRECTORIO
# path_fuente = os.getcwd() + "/Fotos/"

path_fuente = os.getcwd() + '/Fotos/'
# path_fuente = os.getcwd() + "/imagenes_nombre_maaji/"
fileList = os.listdir(path_fuente)

destination_XS = os.getcwd() + '/tallas/talla_XS/'
destination_S = os.getcwd() + '/tallas/talla_S/'
destination_M = os.getcwd() + '/tallas/talla_M/'
destination_L = os.getcwd() + '/tallas/talla_L/'
destination_XL = os.getcwd() + '/tallas/talla_XL/'
destination_XXL = os.getcwd() + '/tallas/talla_XXL/'
destination_XXXL = os.getcwd() + '/tallas/talla_XXXL/'
destination_OS = os.getcwd() + '/tallas/talla_OS/'
destination_SM_MD = os.getcwd() + '/tallas/talla_SM_MD/'
destination_L_XLD = os.getcwd() + '/tallas/talla_L_XLD/'
destination_02 = os.getcwd() + '/tallas/talla_02/'
destination_04 = os.getcwd() + '/tallas/talla_04/'
destination_06 = os.getcwd() + '/tallas/talla_06/'
destination_08 = os.getcwd() + '/tallas/talla_08/'
destination_10 = os.getcwd() + '/tallas/talla_10/'
destination_12 = os.getcwd() + '/tallas/talla_12/'
destination_14 = os.getcwd() + '/tallas/talla_14/'
destination_16 = os.getcwd() + '/tallas/talla_16/'


def organizar_por_tallas_y_posiciones(destination, cod_talla):

    for codigo in dict_codigos_maaji.keys():
        
        for i in range(1, (dict_codigos_maaji[codigo]["cantidad"] + 1)):
            
            for file in fileList:
                
                try:
                    if file == dict_codigos_maaji[codigo]["nombre_completo" + str(i)]:

                        if "_1.jpg" in file:
                            new_file_name = "{}.MAIN.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
        
                        elif "_2.jpg" in file:
                            new_file_name = "{}.PT01.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_3.jpg" in file:
                            new_file_name = "{}.PT02.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_4.jpg" in file:
                            new_file_name = "{}.PT03.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_5.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_6.jpg" in file:
                            new_file_name = "{}.PT05.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_7.jpg" in file:
                            new_file_name = "{}.PT06.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_8.jpg" in file:
                            new_file_name = "{}.PT07.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_9.jpg" in file:
                            new_file_name = "{}.PT08.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_10.jpg" in file:
                            new_file_name = "{}.PT09.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_11.jpg" in file:
                            new_file_name = "{}.PT10.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_12.jpg" in file:
                            new_file_name = "{}.PT11.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                            
                        #POSICIONES NO ESPECIFICADAS:    
                        elif "_1.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                            
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else: 
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1           
                                    os.remove(destination+file)
                                    pass
                            
                        elif "_2.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_3.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_4.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_5.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_6.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_7.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_8.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_9.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_10.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_11.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                                
                        elif "_12.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                                
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1 or dict_codigos_maaji[codigo]["cantidad"] == dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"]:
                                        break
                                    
                                    else:
                                        ultima_posicion_PT_asignada = dict_codigos_maaji[codigo]["cantidad"] - dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + acomulador
                                        print(str(ultima_posicion_PT_asignada) + " pos")
                                            
                                        new_file_name = dict_codigos_maaji[codigo]["cod_talla_" + cod_talla]+".PT0"+str(ultima_posicion_PT_asignada)+".jpg"
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
                                        break
                                except:
                                    print("fallo try")
                                    acomulador = acomulador + 1
                                    os.remove(destination+file)
                                    pass
                except:
                    print("talla " + cod_talla + " no existe para el producto " + str(codigo))       
                        
            # assign size
            # assign size
            size = 0
            
            
            Folderpath = destination 
            
            
            # get size
            for path, dirs, files in os.walk(Folderpath):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.stat(fp).st_size
            
            # display size       
            print("Folder size: " + cod_talla + " " +str(size))  
            if size>= 1000000000:
                
                try:
                    crear_carpetas_de_tallas('talla_' + cod_talla + '_partida')
                    destination = os.getcwd() + '/tallas/talla_' + cod_talla + '_partida/'
                    print("ADVERTENCIA: Carpeta para talla " + cod_talla + " es mayor a 1GB, se creo otra carpeta paraseguir añadiendo imagenes para esta talla")      
                    
                except:
                    
                    try:
                        crear_carpetas_de_tallas('talla_' + cod_talla + '_partida_2')
                        destination = os.getcwd() + '/tallas/talla_' + cod_talla + '_partida_2/'
                        print("ADVERTENCIA: Carpeta para talla " + cod_talla + " es mayor a 1GB, se creo otra carpeta paraseguir añadiendo imagenes para esta talla")      
                        
                    except:
                        crear_carpetas_de_tallas('talla_' + cod_talla + '_partida_3')
                        destination = os.getcwd() + '/tallas/talla_' + cod_talla + '_partida_3/'
                        print("ADVERTENCIA: Carpeta para talla " + cod_talla + " es mayor a 1GB, se creo otra carpeta paraseguir añadiendo imagenes para esta talla")      
                    
                
                  
                 
                
organizar_por_tallas_y_posiciones(destination_XS, "XS")
organizar_por_tallas_y_posiciones(destination_S, "S")
organizar_por_tallas_y_posiciones(destination_M, "M")
organizar_por_tallas_y_posiciones(destination_L, "L")
organizar_por_tallas_y_posiciones(destination_XL, "XL")
organizar_por_tallas_y_posiciones(destination_XXL, "XXL")
organizar_por_tallas_y_posiciones(destination_XXXL, "XXXL")
organizar_por_tallas_y_posiciones(destination_OS, "OS")
organizar_por_tallas_y_posiciones(destination_SM_MD, "SM_MD")
organizar_por_tallas_y_posiciones(destination_L_XLD, "L_XLD")
organizar_por_tallas_y_posiciones(destination_02, "02")
organizar_por_tallas_y_posiciones(destination_04, "04")
organizar_por_tallas_y_posiciones(destination_06, "06")
organizar_por_tallas_y_posiciones(destination_08, "08")
organizar_por_tallas_y_posiciones(destination_10, "10")
organizar_por_tallas_y_posiciones(destination_12, "12")
organizar_por_tallas_y_posiciones(destination_14, "14")
organizar_por_tallas_y_posiciones(destination_16, "16")

        
def crear_carpetas_comprimidas_partidas(talla):
    path = os.getcwd() + "/tallas/talla_"+talla
    dir = os.listdir(path)
    
    path_comprimida = os.getcwd() + "/carpeta_"+talla+".zip"
    
    try:
        os.remove(path_comprimida)
    except:
        print("...")
    
    if len(dir) != 0:
        shutil.make_archive("carpeta_"+talla, 'zip', os.getcwd() + '/tallas/talla_'+talla)
    
    if os.path.isdir(os.getcwd() + '/tallas/talla_'+talla+'_partida') == True:
        shutil.make_archive("carpeta_"+talla+"_partida", 'zip', os.getcwd() + '/tallas/talla_'+talla+'_partida')

    if os.path.isdir(os.getcwd() + '/tallas/talla_'+talla+'_partida_2') == True:
        shutil.make_archive("carpeta_"+talla+"_partida_2", 'zip', os.getcwd() + '/tallas/talla_'+talla+'_partida_2')
        
    if os.path.isdir(os.getcwd() + '/tallas/talla_'+talla+'_partida_3') == True:
        shutil.make_archive("carpeta_"+talla+"_partida_3", 'zip', os.getcwd() + '/tallas/talla_'+talla+'_partida_3')


crear_carpetas_comprimidas_partidas('XS')
crear_carpetas_comprimidas_partidas('S')
crear_carpetas_comprimidas_partidas('M')
crear_carpetas_comprimidas_partidas('L')
crear_carpetas_comprimidas_partidas('XL')
crear_carpetas_comprimidas_partidas('XXL')
crear_carpetas_comprimidas_partidas('XXXL')
crear_carpetas_comprimidas_partidas('OS')
crear_carpetas_comprimidas_partidas('SM_MD')
crear_carpetas_comprimidas_partidas('L_XLD')
crear_carpetas_comprimidas_partidas('02')
crear_carpetas_comprimidas_partidas('04')
crear_carpetas_comprimidas_partidas('06')
crear_carpetas_comprimidas_partidas('08')
crear_carpetas_comprimidas_partidas('10')
crear_carpetas_comprimidas_partidas('12')
crear_carpetas_comprimidas_partidas('14')
crear_carpetas_comprimidas_partidas('16')
    

print("PROCESO FINALIZADO! :)")
time.sleep(5)