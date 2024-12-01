def adicionar_no_catalogo(catalogo : list, nome : str, diretor : str, ano : int, genero : list): #uma função auxiliar que coloca todas as informações do filme no catálogo
    filme = [nome, diretor, ano, genero] #primeiramente, ela coloca o nome, diretor, ano, e gênero em uma lista
    catalogo.append(filme) #e depois adiciona essa lista no catálogo

def verificar_catalogo(titulo : str, catalogo : list): #uma função que retorna verdadeiro, caso o filme informado esteja no catálogo e falso, caso contrário.
    for filme in catalogo: #primeiramente, ela percorre cada filme no catálogo.
        if remover_acento(filme[0]).title() == remover_acento(titulo).title(): #após isso, ela compara o título selecionado pelo for com o título informado pelo usuário. Caso eles sejam iguais, ele retorna 'True'. Caso contrário, ele passa para o próximo título no catálogo.
            return True
    return False #caso a função não encontre nenhum igual, ela retornará 'False'

def remover_acento(string : str): #uma função que retorna uma nova string com todos os acentos das vogais removidos
    c_acentos = 'áàãâéèêíìîóòõôúùûç' #primeiramente, ela cria duas variáveis: uma contendo todas as letras que podem ser acentuadas e uma com todas as versões sem acento delas, tomando cuidado para as letras correspondentes ficarem paralelas
    s_acentos = 'aaaaeeeiiioooouuuc'
    nova_string = '' #em seguida, ela cria uma variável chamada ‘nova_string’, para armazenar a palavra sem acentos
    for letra in string: #aqui ele percorre todas as letras da palavra que foi passada como argumento no for e, se a letra estiver na variável 'c_acentos', ele encontra o indice da letra e adiciona na nova variável a letra correspondente (com esse mesmo indice) da variável 's_acentos'
        if letra in c_acentos:
            indice = c_acentos.index(letra)
            nova_string += s_acentos[indice]
        else: #caso a letra não tenha sido encontrada na variável 'c_acentos', ela apenas é copiada para a nova string
            nova_string += letra
    return nova_string #por fim, ela retorna a nova string sem os acentos

def verificar_ano(ano : str): #uma função que verifica se o ano informado é numérico e se ele está dentro do intervalo de anos válidos.
    while True: #enquanto o while não for quebrado, ele ficará em loop pelos if's abaixo:
        if not ano.isdigit(): #se o ano não for um dígito, ou seja, se o usuário inserir qualquer coisa que não seja um número, ele mostrará a mensagem abaixo e perguntará o ano novamente.
            print(f'O ano deve ser numérico, ano inválido - PyFlix.')
            ano = str(input('● Digite o ano do filme: '))
        elif int(ano) < 1888 or int(ano) > 2024: #se o usuário inserir um número maior que 2024 e menor que 1888 (o ano que o primeiro filme foi criado), ele mostrará a mensagem abaixo e perguntará o ano novamente.
            print(f'O ano é anterior a 1888 ou posterior a 2024, ano inválido. - PyFlix.')
            ano = str(input('● Digite o ano do filme: '))
        else: #caso nada disso aconteça e o ano seja válido, ele quebrará o loop
            break
    return ano #após sair do loop do while, ele retornará o ano do filme

def remover_do_catalogo(catalogo : list): #uma função que remove filmes com  base no título
    titulo = str(input('● Digite o título do filme que desejas remover: ')).title() #o título do filme é recebido do usuário.
    if verificar_catalogo(titulo, catalogo): #verificamos se o titulo informado corresponde a algum filme no catalogo, usando a função verificar_catalogo
        for filme in catalogo: #percorrendo todos os filmes dentro do catálogo.
            if filme[0] == titulo: #verificando se filme[0], que corresponde ao título do filme atual, corresponde a algum filme dentro do catálogo.
                catalogo.remove(filme)#o filme com o título informado é removido do catálogo.
                print(f'{filme[0]} foi removido catálogo. - PyFlix.') #uma mensagem informativa exibindo o filme que foi removido.
        sobrescrever_catalogo(catalogo, 'dados.txt') #esse trecho chama a função responsável por fazer as alterações no arquivo txt.
    else: #mostra uma mensagem de erro para caso o filme não esteja no catálogo.
        print(f'O filme "{titulo}" não está no catálogo. - PyFlix.')
        print(' ')

def encontrar_indice(titulo : str,catalogo : list): #uma função auxiliar que encontra o indice de um filme dentro do catálogo
    tamanho = len(catalogo) #primeiramente, ele armazenará o tamanho do catálogo (a quantidade de filmes que tem nele) na variável 'tamanho'
    for i in range(tamanho): #e, para cada indice no tamanho do catálogo (cada filme), ele irá comparar o título dado pelo for ao título dado pelo usuário e o retornará na função
        if catalogo[i][0].title() == titulo.title():
            return i

def sobrescrever_catalogo(catalogo : list, file : str): #uma função que abre o arquivo dados.txt e formata os elementos do catálogo em linhas.
    with open(file, 'w') as dados: #utilizamos a instrução with open para abrir o arquivo file no modo "w" (write) para sobrescrever os dados antigos.
        for filme in catalogo: #percorremos a lista que armazena todos os filmes
            linha = ','.join(filme) #utilizamos o método join para juntar todos os elementos da lista em uma string separada por vírgulas.
            dados.write(f"{linha}\n") #a linha é escrita no arquivo txt

def adicionar_filme(catalogo : list): #uma função que adiciona um filme no catálogo, verificando se o título já está no catálogo e se o nome do diretor, ano e gênero são válidos
    nome = input("● Digite o título do filme: ").title() #o título é solicitado ao usuário.
    if not verificar_catalogo(nome, catalogo): #apenas faz sentido adicionar um filme no catalágo, se o mesmo não estiver lá ainda, então aqui é verificado se o filme não está no catálogo.
        diretor = input("● Digite o nome do diretor: ").title() #o diretor é solicitado ao usuário.
        while not diretor.replace(' ', '').isalpha(): #enquanto o nome do diretor não for formado apenas por caracteres do alfabeto, o diretor continua sendo solicitado.
            print(f'O nome do diretor não pode conter números ou caracteres especiais. - PyFlix.') #uma mensagem de erro é mostrada ao usuário, para informar que o diretor não é válido.
            diretor = input("● Digite o nome do diretor: ").title()
        ano = verificar_ano(str(input("● Digite o ano do filme: "))) #utilizamos a função verificar_ano para garantir que o ano informado seja um inteiro e esteja entre o intervalo especificado
        #o ano é representado por uma string devido ao fato de que quando os dados são carregados do arquivo txt, todos os números e todos os dados estão na forma de string.
        genero = input("● Digite o(s) gênero(s) do filme: ").title() #o gênero é pedido ao usuário.
        while not genero.replace(' ', '').isalpha(): #uma verificação que funciona da mesma forma que a verificação para diretor, garantindo que contenha somente letras do alfabeto.
            print(f'O genêro não pode conter números ou caracteres especiais. - PyFlix.') #uma mensagem de erro.
            genero = input("● Digite o(s) gênero(s) do filme: ").title() #o gênero continua a ser pedido até que seja válido.
        adicionar_no_catalogo(catalogo, nome, diretor, ano, genero) #utilizamos a função auxiliar adicionar_no_catalogo para adicionar todas as informações dentro do catálogo.
        sobrescrever_catalogo(catalogo, 'dados.txt') #chamamos a função responsável por sobrescrever os dados do catálogo.
    else: #caso o filme já esteja no catálogo, é exibido uma mensagem especial informando que o filme já está no catálogo e todas as informações dele são exibidas.
        print(' ')
        print(f'O filme "{nome}" já existe no catálogo. - PyFlix') #todas as informações são exibidas
        indice = encontrar_indice(nome, catalogo)
        print(f"⮕ Título:  {catalogo[indice][0]}")
        print(f"⮕ Diretor: {catalogo[indice][1]}")
        print(f"⮕ Ano:     {catalogo[indice][2]}")
        print(f"⮕ Gênero:  {catalogo[indice][3]}")
        if len(catalogo[indice]) == 5: #caso o tamanho da lista que representa o filme seja 5, significa que esse filme possui uma avaliação associada a ele.
            print(f"⮕ Ratting:  {float(catalogo[indice][4]) :.1f}") #a avaliação é exibida.
        else:
            print(f"⮕ Ratting: - \n") #caso não haja uma avaliação nova, é exibido um - no lugar do número de estrelas.

def menu(): #função para printar o menu
    print('\n---------------------------------------------------------------------------------')
    print("\n⮕ MENU DE FUNCIONALIDADES - PyFlix: ")
    print('\n⮕ Adicionar um filme    (1)')
    print('⮕ Listar o catálogo     (2)')
    print('⮕ Pesquisar um filme    (3)')
    print('⮕ Editar um filme       (4)')
    print('⮕ Remover um filme      (5)')
    print('⮕ Fazer uma avaliação   (6)')
    print('⮕ Sair do aplicativo    (7)\n')

def buscar_filme(titulo : str, catalogo : list, mode : str): #função para buscar filmes no catálogo baseado no título ou no gênero (com e sem acentos) e armazená-los numa lista
    resultados = [] #é criado uma lista que vai armazenar os resultados da busca.
    if mode == 't': #o parâmetro mode representa o modo como a busca vai ocorrer, onde t representa a busca por título e g representa a busca por gênero.
        for filme in catalogo: #percorrendo todos os filmes do catálogo
            if remover_acento(titulo).lower() in remover_acento(filme[0]).lower(): #verifico se o subtítulo informado está presente no filme atual, caso sim, a lista resultados recebe um append dos dados desse filme.
            #as verificações são feitas padronizando o titulo informado e o título do filme atual para uma versão minúscula e sem acentos.
                resultados.append(filme)
        return resultados #ao fim da função é retornada a lista com todos os filmes encontrados.
    elif mode == 'g': #verifico se o usuário selecionou a busca por gênero.
        for filme in catalogo: #percorro todos os filmes do catálogo.
            if remover_acento(titulo).lower() == remover_acento(filme[3]).lower(): #semelhante a verificação da pesquisa por título, aqui tanto o gênero informado quanto o gênero do filme  atual são padronizados para uma versão minúscula e sem acentos.
            #uma verificação é feita para checar se o gênero informado corresponde a ao genêro do filme atual, caso sim, a lista que contém os resultados recebe um append do devido filme.    
                resultados.append(filme) 
        return resultados #ao fim da função é retornada a lista com todos os filmes encontrados na busca.

def listar_filme(catalogo : list, mensagem : str): #uma função para listar todos os filmes do catálogo na formatação adequada
  print(mensagem) #a mensagem definida pelo usuário é printada
  for filme in catalogo: #os filmes do catalogo são percorridos, para que seja possível mostrar um a um.
    print(' ')
    print(f"⮕ Título:  {filme[0]}") #cada índice representa uma das informações do filme, 0 é o título, 1 é o diretor, 2 é o ano e 3 é o gênero
    print(f"⮕ Diretor: {filme[1]}")
    print(f"⮕ Ano:     {filme[2]}")
    print(f"⮕ Gênero:  {filme[3]}")
    if len(filme) == 5: #alguns filmes contam com uma avaliação, nesse caso o tamanho da lista do filme é 5, nesse trecho estou verificando se o filme possui avaliação, caso sim, ela será mostrada.
        print(f"⮕ Ratting:  {filme[4]}\n")
    else:
        print(f"⮕ Ratting: - \n") #caso o filme não possua avaliações, um - é exibido para representar a falta de avaliação.

def mostrar_resultados(catalogo : list, mode : str): #função apenas para mostrar os resultados da função 'buscar_filme'
    busca = str(input('● Pesquisar por: ')) #o usuário informa o título/gênero que será usado para a pesquisa.
    resultados = buscar_filme(busca, catalogo, mode) #o resultado da função buscar_filme é armazenado dentro de uma varíavel, no qual será fornecida como argumento para a função listar filme.
    tamanho = len(resultados) #apenas armazenando o tamanho da lista resultados para utilizar na função listar filmes.
    listar_filme(resultados, f'{tamanho} Resultados encontrados para "{busca}":') #chamando a função listar filmes para mostrar os resultados da busca.

def carregar_dados(file : str): #uma função apenas para carregar os dados a partir do arquivo txt e armazená-los em uma lista
    with open(file, 'r') as dados: #utilizamos a função with open para abrir o arquivo file no modo de leitura, para ler as informações do arquivo.
        linhas = dados.readlines() #o método readlines() retorna uma lista contendo todas as linhas do arquivo na forma de uma string.
        tamanho = len(linhas) #o tamanho da string é armazenado em uma variável.
        for l in range(tamanho): #percorremos a lista que possui as linhas a partir dos índices.
            linhas[l] = linhas[l].split(',') #linhas[l] que é o elemento que contém a linha atual na forma de uma string, para converter a mesma para uma lista que contém as informações do filme da linha atual.
            linhas[l][-1] = linhas[l][-1].strip() #em arquivos txt, sempre o último elemento possui \n ao final para quebrar a linha, então usamos o .strip para remover a quebra de linha, para evitar inteferências nas verificações. 
    #então usamos o linhas[l][-1] para acessar o último elemento da lista e assim trocar ele pela sua versão sem a quebra de linha.
    return linhas #os dados são retornados na forma de uma lista aninhada.

def editar_filme(catalogo : list): #função que edita um filme no catálogo, procurando por seu nome e podendo manter as informações antigas, se desejado.
    titulo = str(input('● Insira o nome do filme que deseja editar: ')) #o título do filme que será editado é informado.
    if verificar_catalogo(titulo, catalogo): #utilizamos a função verificar_catalogo para verificar se o filme está dento do catálogo.
        indice = encontrar_indice(titulo, catalogo) #utilizamos a função encontrar_indice 
        novo_titulo = str(input('● Insira o novo título [digite 0 para manter o atual]: ')) #o usuário insere o novo título, onde ele pode ou não modificar o título, digitando 0 para o caso negativo.
        if novo_titulo != '0': #o título é modificado somente se o que foi digitado é diferente de 0.
            catalogo[indice][0] = novo_titulo #atualizando o título dentro do filme no catálogo.
        novo_diretor = str(input('● Insira o novo diretor [digite 0 para manter o atual]: ')) #o usuário insere o novo diretor, da mesma forma que o título, o atual somente será atualizado se o valor digitado for diferente de 0.
        if novo_diretor != '0': #verificação semelhante ao título.
            catalogo[indice][1] = novo_diretor #atualizando o valor do diretor
        novo_ano = str(input('● Insira o novo ano [digite 0 para manter o atual]: ')) #funciona da mesma forma que os anteriores.
        if novo_ano != '0': #a mesma verificação antes comentada.
            catalogo[indice][2] = novo_ano #atualizando o ano
        novo_genero = str(input('● Insira o(s) novo(s) genero(s) [digite 0 para manter o(s) atual(is)]: ')) #o usuário insere o novo gênero ou digita 0 para manter o atual.
        if novo_genero != '0': #mesma verificação antes comentada.
            catalogo[indice][3] = novo_genero #o gênero sendo atualizado.
    else: #é mostrado uma mensagem informativa para caso o filme não esteja no catálogo.
        print(f'\nO filme "{titulo}" não está no catálogo. - PyFlix.\n') #mensagem informativa caso o filme não esteja no catálogo.
    sobrescrever_catalogo(catalogo, 'dados.txt') #a função para sobrescrever os dados com as atualizações

def menu_buscar(): #função auxiliar que exibe o menu de busca e retorna a opção selecionada pelo usuário
    print('\n---------------------------------------------------------------------------------') #primeiramente, ele mostra o menu de busca do usuário
    print("\n⮕ MENU DE BUSCA - PyFlix: ")
    print('⮕ Buscar por título   (t)')
    print('⮕ Buscar por Gênero   (g)\n')
    mode = str(input('● Insira o modo de busca: ')).lower() #após isso, ele pergunta ao usuário qual modo ele deseja usar e coloca ele em letra minúscula.
    while mode != 't' and mode != 'g': #se o modo for diferente de t ou g, ele mostra a mensagem abaixo e pede novamente o modo de busca.
        print(f'Modo de busca inválido.')
        mode = str(input('● Insira o modo de busca: ')).lower()
    return mode #quando o usuário inserir um modo válido, ele retornará o modo que ele escolheu
def validar_entrada_float(entrada : str): #uma função que valida entradas float para strings, pois o uso de strings é essencial para garantir a verificação numérica, garantindo somente números.
    if entrada.count('.') <= 1:
        for caractere in entrada: #percorrendo todos os caracteres
            if (caractere.isdigit() or caractere == '.') == False: #caso durante a iteração, seja encontrado um caractere que não seja . ou um número, é retornado False imediatamente.
                return False #retornando False para o caso de encontrar um caractere estranho.
    else:
        return False
    return True
def avaliar(catalogo : list): #uma função que permite o usuário avaliar o filme desejado e, caso ele seja avaliado uma segunda vez, faz a média das avaliações.
    titulo = str(input('● Insira o título do filme que deseja avaliar: ')).title() #o usuário ubforma o título do filme que deseja avaliar.
    if verificar_catalogo(titulo, catalogo): #A função verificar catálogo verifica se o filme está dentro do catálogo.
        indice = encontrar_indice(titulo, catalogo) #caso o filme esteja no catálogo, é necessário encontrar o índice do filme dentro do catálogo.
        avalia = str(input('● Insira a quantidade de estrelas do filme: '))#o usuário informa a quantidade de estrelas que quer dar para o filme
        while validar_entrada_float(avalia) == False:
                print(f'A avaliação deve ser um número inteiro ou decimal (float).')
                avalia = str(input('● Insira a quantidade de estrelas do filme: '))
        avalia = float(avalia)
        while avalia < 0 or avalia > 5: #uma verificação para impedir uma quantidade de estrelas menor que 0 e maior que 5.
            print(f'O mínimo de estrelas é 0 e o máximo é 5. - PyFlix.')
            avalia = float(input('● Insira a quantidade de estrelas do filme: '))

        if len(catalogo[indice]) == 4: #verifico se o filme em questão possui um tamanho 4, representando os filmes que não possuem avaliação.
            catalogo[indice].append(str(avalia)) #nesse caso a avaliação é apenas adicionada dentro dos dados do filme.
        else: #caso o tamanho do catálogo não seja 4, significa que ele já possui uma avaliação.
            media = (avalia + float(catalogo[indice][4])) / 2 #para filmes que já possuem uma avalição, é calculada a média entre a nova avaliação e a anterior, catalogo[indice] é o filme atual e o índice 4 é a avaliação, que precisa ser convertida para float para calcular a média
            catalogo[indice][4] = str(round(media, 2)) # a nova avaliação (media de ambas) substitui a avaliação anterior, arredondando o valor para duas casas decimais.
    else: #uma mensagem informativa caso o filme não esteja dentro do catálogo.
        print(f'Filme não encontrado em nosso catálogo. - PyFlix.')

catalogo = carregar_dados('dados.txt') #o resultado do carregamento dos dados é armazenada em uma variável, no caso uma lista aninhada.

while True: #o loop que vai rodar o código principal
    menu() #chamo a função menu para exibir o menu
    escolha = str(input('● Escolha uma das funcionalidades acima: ')) #o usuário seleciona uma das opções dentro do menu.
    if escolha == "1": #se o usuário selecionar a opção 1 (adicionar no catálogo), a função adicionar_filme é chamada para adicionar o filme no catálogo.
        adicionar_filme(catalogo)
    elif escolha == "2": #se a escolha for 2 (listar filmes), a função listar filmes será utilizada para exibir todos os filmes do catálogo.
        mensagem = '\n⮕ CATÁLOGO DOS FILMES' #a mensagem que será exibida na função listar filmes.
        if len(catalogo) != 0: #a listagem somente será feita se o catálogo será preenchida, esse trecho verifica exatamente isso.
            listar_filme(catalogo, mensagem) #chamando a função listar_filme, passando como argumento o catálogo e a mensagem.
        else: #se o catálogo não está preenchido uma mensagem informativa é exibida para informar ao usuário que o catálogo está vazio.
            print(f'O catálogo está vazio. - Pyflix.') #mensagem informativa
    elif escolha == "3": #caso o usuário insira a opção 3, o menu de busca será exibido e o usuário vai selecionar o modo de busca (título ou gênero.)
        mode = menu_buscar() #armazenando o resultado da função de menu de busca (o mode)
        mostrar_resultados(catalogo, mode) #chamamos a função mostrar_resultados e passamos como argumento o catálogo e o mode selecionado, assim a pesquisa será realizada.
    elif escolha == "4": #caso o usuário opte por editar um filme, a função específica será chamada para realizar essa tarefa, conforme comentado sobre essa função anteriormente.
        editar_filme(catalogo) #chamando a função para fazer a edição dos filmes.
    elif escolha == "5": #se a escolha foi 5, a função específica para remover filmes é chamada para realizar a respectiva tarefa.
        remover_do_catalogo(catalogo) #chamando a função que vai remover do catálogo.
    elif escolha == '6': #se a escolha foi 6 o usuário vai avaliar um filme, então a devida função é chamada para essa tarefa.
        avaliar(catalogo) #a função avaliar funciona conforme citado antes.
        sobrescrever_catalogo(catalogo, 'dados.txt') #chamando a função sobrescrever_catálogo para salvar as alterações no arquivo txt.
    elif escolha == "7": #caso a opção seja 7, o usuário optou por encerrar o programa, então todas as alterações são realizadas.
        sobrescrever_catalogo(catalogo, 'dados.txt') #chamando a função para realizar as alterações.
        print('\nObrigado por usar nossa plataforma! - PyFlix.\n') #mensagem de agradecimento pelo uso do programa.
        break #encerramento do loop principal
    else:
        print("\nEssa opção não existe, tente novamente. - pyFlix. \n") #uma mensagem para tratar as respostas inválidas.
