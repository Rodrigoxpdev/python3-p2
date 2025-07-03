import pywhatkit
import time



# Número do destinatário no formato: +55DDDNUMERO
numero = '+5591984376828'

# Opções de mensagens
op = [
    'Renovação 🔄',
    'Suporte técnico 👨🏻‍🔧',
    'Mudança de aplicativo📲',
    'Duvidas 🤔'
]

mensagens = [
    'Olá! Você escolheu Renovação.',
    'Olá! Você escolheu Suporte técnico.',
    'Olá! Você escolheu Mudança de aplicativo.',
    'Olá! Você escolheu Dúvidas.'
]

def enviar_menu():
    menu = "Olá! Escolha uma opção e responda com o número:\n"
    for i, opcao in enumerate(op, 1):
        menu += f"{i} - {opcao}\n"
    pywhatkit.sendwhatmsg_instantly(numero, menu)
    print("Menu enviado no WhatsApp!")

def enviar_resposta(opcao):
    mensagem = mensagens[opcao - 1]
    pywhatkit.sendwhatmsg_instantly(numero, mensagem)
    print(f"Resposta enviada: {mensagem}")

# Loop de automação (simulação de bot)
while True:
    enviar_menu()
    # Aguarda o usuário responder no terminal (simulação)
    try:
        pergunta1 = int(input('Digite aqui a opção escolhida pelo usuário (1-4), ou 0 para sair: '))
        if pergunta1 == 0:
            print("Bot encerrado.")
            break
        if 1 <= pergunta1 <= 4:
            print(f'Você selecionou: {op[pergunta1 - 1]}')
            enviar_resposta(pergunta1)
        else:
            print('Opção inválida!')
    except ValueError:
        print('Digite um número válido!')
    # Aguarda alguns segundos antes de reiniciar o loop
    time.sleep(2)
















