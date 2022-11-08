import os
import shutil
import pandas as pd

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
crear_carpetas_de_tallas("talla_02")
crear_carpetas_de_tallas("talla_04")
crear_carpetas_de_tallas("talla_06")
crear_carpetas_de_tallas("talla_08")
crear_carpetas_de_tallas("talla_10")
crear_carpetas_de_tallas("talla_12")
crear_carpetas_de_tallas("talla_14")
crear_carpetas_de_tallas("talla_16")


#TOMO LOS DATOS DEL EXCEL Y LOS GUARDO COMO LISTA EN excel_original
df = pd.read_excel(os.getcwd() + '/test_excel_prueba.xlsx' ,engine='openpyxl',dtype=object,header=None)
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
    
    # if "PINK_2" in nombre_archivo_completo:
    #     dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] = dict_codigos_maaji[codigo_maaji]["cantidad_posicion_no_especifica"] + 1
    
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
        dict_codigos_maaji[codigo_maaji]["cod_talla_02"] = row[6]
        
    if isinstance(row[7], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_04"] = row[7]
        
    if isinstance(row[8], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_06"] = row[8]
        
    if isinstance(row[9], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_08"] = row[9]
        
    if isinstance(row[10], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_10"] = row[10]
        
    if isinstance(row[11], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_12"] = row[11]
        
    if isinstance(row[12], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_14"] = row[12]
        
    if isinstance(row[13], str):
        dict_codigos_maaji[codigo_maaji]["cod_talla_16"] = row[13]
        
# print(dict_codigos_maaji)

#RUTA DE LA CARPETA DONDE SE VAN A TOMAR LAS IMAGENES CON EL NOMBRE QUE QUEREMOS CAMBIAR, Y LISTAMOS LOS ARCHIVOS
#DE DICHO DIRECTORIO
path_fuente = "C:/Users/svelez/Desktop/Fotos_Prueba/"
# path_fuente = os.getcwd() + "/imagenes_nombre_maaji/"
fileList = os.listdir(path_fuente)

destination_XS = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_XS/'
destination_S = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_S/'
destination_M = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_M/'
destination_L = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_L/'
destination_XL = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_XL/'
destination_02 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_02/'
destination_04 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_04/'
destination_06 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_06/'
destination_08 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_08/'
destination_10 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_10/'
destination_12 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_12/'
destination_14 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_14/'
destination_16 = 'C:/Users/svelez/Documents/automatizacion_Amazon/tallas/talla_16/'

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
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_7.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_8.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_9.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_10.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_11.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                        elif "_12.jpg" in file:
                            new_file_name = "{}.PT04.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                            dest = shutil.copy(path_fuente+file, destination)
                            os.rename((destination+file), (destination+new_file_name))
                            
                            
                        #POSICIONES NO ESPECIFICADAS:    
                        elif "_1.1" in file:
                            acomulador = 0
                            
                            for n in range(1, dict_codigos_maaji[codigo]["cantidad_posicion_no_especifica"] + 1):
                            
                                try:
                                    new_file_name = ""
                                    
                                    if dict_codigos_maaji[codigo]["cantidad"] == 1:
                                        new_file_name = "{}.MAIN.jpg".format(dict_codigos_maaji[codigo]["cod_talla_" + cod_talla])
                                        dest = shutil.copy(path_fuente+file, destination)
                                        os.rename((destination+file), (destination+new_file_name))
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
                    
                                 
organizar_por_tallas_y_posiciones(destination_XS, "XS")
organizar_por_tallas_y_posiciones(destination_S, "S")
organizar_por_tallas_y_posiciones(destination_M, "M")
organizar_por_tallas_y_posiciones(destination_L, "L")
organizar_por_tallas_y_posiciones(destination_XL, "XL")
organizar_por_tallas_y_posiciones(destination_02, "02")
organizar_por_tallas_y_posiciones(destination_04, "04")
organizar_por_tallas_y_posiciones(destination_06, "06")
organizar_por_tallas_y_posiciones(destination_08, "08")
organizar_por_tallas_y_posiciones(destination_10, "10")
organizar_por_tallas_y_posiciones(destination_12, "12")
organizar_por_tallas_y_posiciones(destination_14, "14")
organizar_por_tallas_y_posiciones(destination_16, "16")
                    
        