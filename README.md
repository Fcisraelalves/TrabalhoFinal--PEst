# PyFlix - Sistema de Catálogo de Filmes

## Descrição do Projeto

PyFlix é um sistema simples de catálogo de filmes em Python. Ele permite que os usuários adicionem, editem, removam e avaliem filmes, além de listar os filmes cadastrados e realizar pesquisas no catálogo por título ou gênero.

O projeto faz uso de manipulação de arquivos para carregar e salvar os dados em um arquivo de texto, permitindo que o catálogo seja persistido entre as execuções do programa.

## Funcionalidades

- **Adicionar Filme**: Permite adicionar novos filmes ao catálogo informando título, diretor, ano e gênero.
- **Listar Filmes**: Exibe todos os filmes cadastrados no catálogo, com informações como título, diretor, ano, gênero e avaliação (se houver).
- **Buscar Filme**: Permite realizar buscas por título ou por gênero no catálogo.
- **Editar Filme**: Possibilita alterar informações de um filme existente no catálogo, como título, diretor, ano e gênero.
- **Remover Filme**: Remove um filme do catálogo, caso ele esteja cadastrado.
- **Avaliar Filme**: Permite que o usuário avalie um filme de 0 a 5 estrelas.
- **Salvar Dados**: Os dados são salvos no arquivo `dados.txt` após cada alteração, garantindo a persistência dos filmes cadastrados.

## Arquivos

- **main.py**: Contém a lógica principal do programa, com todas as funções e o menu interativo.
- **dados.txt**: Arquivo de texto que armazena as informações do catálogo de filmes, com título, diretor, ano, gênero e avaliação (se houver).

## Estrutura do Catálogo

O catálogo é representado como uma lista de filmes. Cada filme é armazenado como uma lista com os seguintes atributos:

- **[0]** Título: Nome do filme
- **[1]** Diretor: Nome do diretor
- **[2]** Ano: Ano de lançamento
- **[3]** Gênero: Gênero(s) do filme
- **[4]** Avaliação: Média das avaliações (se houver)

Exemplo de uma entrada no catálogo:

## Menu de Funcionalidades

O usuário interage com o sistema por meio de um menu de opções:

1. **Adicionar um filme**
2. **Listar o catálogo**
3. **Pesquisar um filme**
4. **Editar um filme**
5. **Remover um filme**
6. **Fazer uma avaliação**
7. **Sair do aplicativo**

## Obs: lembrar de criar um arquivo dados.txt, caso não queira baixar o mesmo, pois caso não exista um arquivo dados.txt, uma mensagem de erro será retornada. 
