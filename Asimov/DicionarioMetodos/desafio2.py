# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

quer_continuar = True
rodadas = 0
acertos = 0

estados_e_capitais = {'Acre':'Rio Branco', 
            'Alagoas':'Maceió',
            'Amapá':'Macapá',
            'Amazonas':'Manaus',
            'Bahia':'Salvador',
            'Ceará':'Fortaleza',
            'Distrito Federal':'Brasília',
            'Espirito Santo':'Vitória',
            'Goiás':'Goiânia',
            'Maranhão':'São Luis',
            'Mato Grosso':'Cuiabá',
            'Mato Grosso do Sul':'Campo Grande',
            'Minas Gerais':'Belo Horizonte',
            'Pará':'Belém',
            'Paraíba':'João Pessoa',
            'Paraná':'Curitiba',
            'Pernambuco':'Recife',
            'Piauí':'Teresina',
            'Rio de Janeiro':'Rio de Janeiro',
            'Rio Grande do Norte':'Natal',
            'Rio Grande do Sul':'Porto Alegre',
            'Rondônia':'Porto Velho',
            'Roraima':'Boa Vista',
            'Santa Catarina':'Florianópolis',
            'São Paulo':'São Paulo',
            'Sergipe':'Aracaju',
            'Tocantis':'Palmas'
            }

for estado, capital in estados_e_capitais.items():
    if not quer_continuar:
        break
    rodadas += 1
    print(f'Qual a capital do estado? {estado}?')

    reposta = input('Sua resposta: ')
    if reposta.lower() == capital.lower():
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta errada! O correto seria {capital}')
    
    while True:
        opcao = input('Deseja continuar? (s/n)').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com "s" para sim ou "n" oara não.')
            continue
        elif opcao == 'n':
            quer_continuar = False
        break

porcentagem = acertos / rodadas * 100

print(f'Você acertou {acertos} de {rodadas}')
print(f'Porcentagem de acertos: {porcentagem:2f}%')