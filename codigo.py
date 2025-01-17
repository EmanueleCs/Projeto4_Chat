#importar o flet
import flet as ft
#criar funcao principal para rodar o seu apliativo
def main(pagina):
    #titulo
    titulo = ft.Text("meu zap")

    def enviar_mensagem_tunel(mensagem):
        #executar tudo o q eu quero que aconteça para 
        #todos os usuarios que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        
        #limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit = enviar_mensagem)
    botao_enviar = ft.Button("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    #botao entrar no chat
    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #sumir como o titulo
        pagina.remove(titulo)
        #sumir como botao iniciar chat
        pagina.remove(botao)
        #carregar o chat
        pagina.add(chat)
        #carregar o campo de enviar mensagem
        #carregar o botao enviar
        pagina.add(linha_enviar)

        #adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        
    
        pagina.update()

    #criar popup
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                           actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")
    #precisa ter evento como parametro pq o click no botao envia informacoes
    
    #botao enviar
    botao = ft.ElevatedButton("iniciar chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao)

#executaf essa funcao com o flet
ft.app(main, view=ft.WEB_BROWSER)