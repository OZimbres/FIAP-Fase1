# Git Cheat Sheet

Git é o sistema de controle de versão distribuído, livre e de código aberto, responsável por tudo relacionado ao GitHub que acontece localmente em seu computador. Esta folha de referência apresenta os comandos Git mais importantes e comumente utilizados para fácil consulta.

## INSTALAÇÃO E GUIs

Com instaladores específicos para cada plataforma para o Git, o GitHub também oferece a facilidade de se manter atualizado com as últimas versões da ferramenta de linha de comando, enquanto fornece uma interface gráfica do usuário para interações diárias, revisão e sincronização de repositórios.

- **GitHub para Windows**
  - [Download](https://windows.github.com)

- **GitHub para Mac**
  - [Download](https://mac.github.com)

Para plataformas Linux e Solaris, a última versão está disponível no site oficial do Git.

- **Git para Todas as Plataformas**
  - [Site do Git](http://git-scm.com)

## CONFIGURAÇÃO

Configurando informações de usuário usadas em todos os repositórios locais:

>Defina um nome que seja identificável para crédito ao revisar o histórico de versões.
~~~sh
git config --global user.name "[nome sobrenome]"
~~~

<br>

>Defina um endereço de email que será associado a cada marcador de histórico.
~~~sh
git config --global user.email "[email-válido]"
~~~

<br>

>Defina a coloração automática da linha de comando para o Git para facilitar a revisão
~~~sh
git config --global color.ui auto
~~~

## CONFIGURAÇÃO E INICIALIZAÇÃO

Configurando informações do usuário, inicializando e clonando repositórios:

>Inicializa um diretório existente como um repositório Git.
~~~sh
git init
~~~

<br>

>Recupera um repositório inteiro de um local hospedado via URL.
~~~sh
git clone [url]
~~~

<br>

Esses comandos são úteis para configurar um novo repositório Git ou clonar um repositório existente para o seu computador local.

## STAGE E SNAPSHOT

Trabalhando com snapshots e a área de preparação (staging) do Git:

>Mostra os arquivos modificados no diretório de trabalho, preparados para o próximo commit.
~~~sh
git status
~~~

<br>

>Adiciona um arquivo ao próximo commit (estágio).
~~~sh
git add [arquivo]
~~~

<br>

>Remove um arquivo da área de preparação (staging), mantendo as alterações no diretório de trabalho.
~~~sh
git reset [arquivo]
~~~

<br>

>Mostra as diferenças do que foi alterado mas não foi preparado (staged).
~~~sh
git diff
~~~

<br>

>Mostra as diferenças do que está preparado (staged) mas ainda não foi commitado.
~~~sh
git diff --staged
~~~

<br>

>Commita o conteúdo preparado (staged) como um novo snapshot de commit.
~~~sh
git commit -m "[mensagem descritiva]"
~~~

<br>


Estes comandos são úteis para gerenciar as alterações nos arquivos e prepará-los para os próximos commits no Git.
