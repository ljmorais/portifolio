times = ('Palmeiras','Internacional','Fluminense','Corithians',
         'Flamengo', 'Athelico-PR', 'Atletico-MG', 'America',
         'Fortaleza', 'Botafogo','Santos', 'Goias', 'SP',
         'Bragantino', 'Coritiba', 'Ceara', 'Cuiaba', 'Avai',
         'Atletico-GO', 'Juventude')

print(f'lista de times: {times}')

print('-'*53)

for pos, posicoes4 in enumerate (times):
    print(f'Os 05 primeiros time na tabela são {times[0:5]}')
    break

print('-----------------------------------------------------')

for pos, ultimas_posições in enumerate(times):
    print(f'Os 04 ultimos lugares da tabela são {times[-5:-1]}')
    break

print('-----------------------------------------------------')

print(f'Os times da serie A em ordem alfabetica: {sorted(times)}')

print('-'*53)

print(f'O time do fluminense se encontra na {times.index("Goias")+1} posição do brasileiro')