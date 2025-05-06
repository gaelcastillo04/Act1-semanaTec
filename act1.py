import cv2
import easyocr

#Esta funcion procesa una imagen y imprime el texto detectado.
def procesar_imagen(nombre_archivo):
    imagen=cv2.imread(nombre_archivo)  #leemmos la imagen 
    imagen_gray= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  #convertimos a gray scale
    cv2.imwrite(f"{nombre_archivo}_original.png", imagen_gray)
    ret, thresh= cv2.threshold(imagen_gray, 200, 255, cv2.THRESH_BINARY_INV)  #treshold nos ayuda a trabajar con grises y sirve para transformar la intensidad
    cv2.imwrite(f"{nombre_archivo}_thresh.png", thresh)
    img_gaussian= cv2.GaussianBlur(src=thresh, ksize=(37, 37), sigmaX=0)  #suavizamos la imagen (Gaussian filter)
    cv2.imwrite(f"{nombre_archivo}_gaussian.png", img_gaussian)
    #usamos easy orc
    reader= easyocr.Reader(["es", "en"], verbose=False)  
    result=reader.readtext(img_gaussian)
    text_detected="\n".join([text for _, text, _ in result])
    print("texto detectado: ")
    print(text_detected)


#Llamamos la funcion con ambas imagenes
procesar_imagen("placa_q.jpg")
procesar_imagen("placa_2.jpg")