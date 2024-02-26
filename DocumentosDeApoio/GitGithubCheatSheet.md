<p align="left">(<a href="../../README.md">readme.md</a>)</p>
<div name="top">
  <h1 align=center>Git Cheat Sheet</h1>
</div>
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

<p align="right">(<a href="#top">back to top</a>)

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

<p align="right">(<a href="#top">back to top</a>)

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

<p align="right">(<a href="#top">back to top</a>)

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

Estes comandos são úteis para gerenciar as alterações nos arquivos e prepará-los para os próximos commits no Git.

<p align="right">(<a href="#top">back to top</a>)

## BRANCH & MERGE

Isolando o trabalho em branches, alterando contexto e integrando mudanças.

>Lista suas branches. Um * aparecerá ao lado da branch atualmente ativa.
~~~sh
git branch
~~~

<br>

>Cria uma nova branch no commit atual.
~~~sh
git branch [nome-da-branch]
~~~

<br>

>Muda para outra branch e a verifica no seu diretório de trabalho.
~~~sh
git checkout
~~~

<br>

>Mescla a história da branch especificada na atual.
~~~sh
git merge [branch]
~~~

<br>

>Mostra todos os commits na história da branch atual.
~~~sh
git log
~~~

<p align="right">(<a href="#top">back to top</a>)

## INSPECT & COMPARE

Examinando logs, diffs e informações de objetos.

>Mostra o histórico de commits para a branch atualmente ativa.
~~~sh
git log
~~~

<br>

>Mostra os commits na branchA que não estão na branchB.
~~~sh
git log branchB..branchA
~~~

<br>

>Mostra os commits que mudaram o arquivo, mesmo em renomeações.
~~~sh
git log --follow [arquivo]
~~~

<br>

>Mostra a diferença do que está na branchA que não está na branchB.
~~~sh
git diff branchB...branchA
~~~

<br>

>Mostra qualquer objeto no Git em formato legível para humanos.
~~~sh
git show [SHA]
~~~

<p align="right">(<a href="#top">back to top</a>)

## IGNORING PATTERNS

Evitando o staging ou commit acidental de arquivos.

>Salva um arquivo com os padrões desejados como .gitignore com correspondências diretas ou globos curinga.
~~~sh
logs/
*.notes
pattern*/
~~~

<br>

>Padrão de ignore para evitar o staging ou commit de arquivos específicos.
~~~sh
git config --global core.excludesfile [arquivo]
~~~

<p align="right">(<a href="#top">back to top</a>)

## SHARE & UPDATE

Recuperando atualizações de outro repositório e atualizando repositórios locais.

>Adiciona um URL do git como um alias.
~~~sh
git remote add [alias] [url]
~~~

<br>

>Baixa todas as branches daquele repositório Git remoto.
~~~sh
git fetch [alias]
~~~

<br>

>Mescla uma branch remota na sua branch atual para atualizá-la.
~~~sh
git merge [alias]/[branch]
~~~

<br>

>Transmite commits da branch local para a branch remota do repositório.
~~~sh
git push [alias] [branch]
~~~

<br>

>Baixa e mescla quaisquer commits da branch remota de rastreamento.
~~~sh
git pull
~~~

## REWRITE HISTORY

Reescrevendo branches, atualizando commits e limpando o histórico.

>Aplica quaisquer commits da branch atual à frente da especificada.
~~~sh
git rebase [branch]
~~~

<br>

>Limpa a área de preparação, reescreve a árvore de trabalho a partir do commit especificado.
~~~sh
git reset --hard [commit]
~~~

## TEMPORARY COMMITS

Armazenar temporariamente arquivos modificados e rastreados para mudar de branches.

>Listar as mudanças salvas temporariamente.
~~~sh
git stash list
~~~

<br>

>Salvar as mudanças modificadas e preparadas.
~~~sh
git stash
~~~

<br>

>Aplicar as mudanças do topo da pilha de stash.
~~~sh
git stash pop
~~~

<br>

>Descartar as mudanças do topo da pilha de stash.
~~~sh
git stash drop
~~~