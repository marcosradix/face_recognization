import cv2
import os


classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
camera = cv2.VideoCapture(0)
amostra = 1
numero_amostras = 25
id = input("Digite seu identificador: ")
print("Aguardando comando 'q' para captura de imagens...")

if(os.path.exists("./imagens/{}/".format(id)) == False):
    os.mkdir("./imagens/{}/".format(id))

else:
    print("diretório já existente")
largura , altura = 220, 220


while(True):
    conectado, imagem = camera.read()
    imagem_sinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces_detectadas = classificador.detectMultiScale(imagem_sinza, scaleFactor=1.5, minSize=(100, 100))

    #desenho na face detectada cor do retangulo (0, 0, 255) red
    for(x_horizontal, y_vertical, largura_l, altura_a) in faces_detectadas:
        cv2.rectangle(imagem, (x_horizontal, y_vertical), (x_horizontal + largura_l, y_vertical + altura_a), (0, 0, 255), 2)
        if(cv2.waitKey(1) & 0xFF == ord("q") ):
            imagem_rosto = cv2.resize(imagem_sinza[y_vertical:y_vertical + altura, x_horizontal:x_horizontal + largura],(largura, altura) )
            cv2.imwrite("imagens/{}/pessoa.".format(id) + str(id) + "." + str(amostra) + ".jpg", imagem_rosto)
            print("Foto {} capturada com sucesso. ".format(amostra))
            amostra +=1

    cv2.imshow("Rosto detectado", imagem)
    cv2.waitKey(1)
    if(amostra >= numero_amostras +1):
        break
print("{} faces capturadas com sucesso.".format(numero_amostras))
camera.release()
cv2.destroyAllWindows()
