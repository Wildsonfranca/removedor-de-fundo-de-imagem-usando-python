#para esse progrma funcionar e preciso passar a imagem para o terminal 

import flet as ft
from rembg import remove
from PIL import Image
import io

def main(page: ft.Page):
    page.title = "Remover Fundo da Imagem"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Controle para mostrar mensagens ao usuário
    message = ft.Text("")
    page.add(message)

    def on_upload(e):
        if e.files:
            try:
                # Lê a imagem do arquivo
                img = Image.open(io.BytesIO(e.files[0].read()))
                
                # Remove o fundo
                img_sem_fundo = remove(img)

                # Salvar a nova imagem sem fundo
                nova_img = f"nova_{e.files[0].name}"
                img_sem_fundo.save(nova_img)

                # Atualiza a mensagem de sucesso
                message.value = f"Imagem salva como: {nova_img}"
            except Exception as ex:
                # Atualiza a mensagem de erro
                message.value = f"Não foi possível remover o fundo da imagem: {ex}"
            page.update()

    # Cria o FilePicker
    upload_button = ft.FilePicker(on_result=on_upload)
    upload_btn = ft.ElevatedButton("Carregar Imagem", on_click=lambda _: upload_button.pick_files())

    # Adiciona os controles à página
    page.add(upload_btn, upload_button)

# Iniciar a aplicação
ft.app(target=main)
