import os
import shutil
import pandas as pd

dir_path = os.getcwd() + "/tallas2"
try:
        shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
except:
    print("error al eliminar carpeta de tallas")
    
    
    
    
        
def crear_carpetas_de_tallas(talla_name):
    try:
        parent_dir = os.getcwd() + "/"
        tallas_folder = os.path.join(parent_dir, "tallas2")
        os.mkdir(tallas_folder)
    except:
        print("carpeta talla ya existe")
        
    tallas2_folder = parent_dir + "tallas2/"
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