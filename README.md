# Python_script_to_rename_catalog_imgs_to_Amazon_format
3 different ways for renaming images from a folder, and asign them their unique Amazon product size code and position, so it can be uploaded to Amazon

V1:
In the Version 1 script the script compares the images in imagenes_nombre_maaji with the test_excel file, then it saves the unique size code for each img and renames 
the actual img with that code and its position to be uploaded on Amazon. The final images are saved in tallas/size_folder (This version ignores the non-specific image 
names like the ones ending with 1.1, 2.1, 3.1 and so on).

V2:
In the Version 2 script the script compares the images in imagenes_nombre_maaji with the test_excel file, then it saves the unique size code for each img and renames 
the actual img with that code and its position to be uploaded on Amazon. Then it creates a sub directory within the imagenes_listas folder which will be named with
the original image code. This folder will have the renamed images for each size for that specific image (This version ignores the non-specific image 
names like the ones ending with 1.1, 2.1, 3.1 and so on).

V3:
In the Version 3 script the script compares the images in fotos_prueba with the test_excel_prueba file, then it saves the unique size code for each img and renames 
the actual img with that code and its position to be uploaded on Amazon. Then it creates the tallas directory and another directory inside that one for each size 
which will contain the renamed images for each size. 
