#para esse progrma funcionar e preciso passar a imagem para o terminal 


from rembg import remove
from PIL import Image

while True:
    try:
        imagem= input("Informe o nome da imagem com a extençao ou 'Enter' para encerrar o programa : ")
        if imagem:
             nova_img =f"nova_{imagem}.png"
             original =Image.open(imagem)
             img_sem_fundo = remove(original)
             img_sem_fundo.save(nova_img)
             continue
        else:
            ...
    except Exception as e:
            print(f"Não foi possível remover o fundo da imagem .{e}.")
    finally:
            break    
        