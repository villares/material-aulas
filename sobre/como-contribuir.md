
# Como contribuir com este material

> **Antes de contribuir com *Pull Request*, converse em uma  issue!** Ao contribuir você está doando a propriedade intelectual do material produzido para este projeto iniciado por Alexandre B A Villares, que conta com as licenças GPL v3 para o código e CC BY-NC-SA 4.0 para texto e imagens, como descrito na página inicial. Tenha cuidado caso pretenda adaptar materiais de outras fontes, discutindo se isso é apropriado com as pessoas mantenedoras.

## Passo 0

Crie uma conta no GitHub
- Como criar uma conta no GitHub?
  [Preencha este formulário](https://github.com/join)

## Issue tracking (acompanhamento de problemas ou questões)

As chamadas _issues_ são registros de problemas ou desejos de aprimoramento em um projeto. Este projeto tem suas *issues* aqui: [github.com/villares/material-aulas/issues](https://github.com/villares/material-aulas/issues)

**Criar uma *issue* pode ser já uma boa contribuição para um projeto.**

Para criar uma *issue*:

- leia com cuidado o material para identificar lacunas ou problemas;
- veja se não tem uma _issue_ parecida já (você pode comentar nela algum detalhe);
- clique no botão verde [**New issue**](https://github.com/villares/material-aulas/issues/new).

### Maneiras de usar o GitHub

- use a interface web <- *comece agora mesmo usando o navegador!*
- ou baixe o GitHub Desktop: [MacOS / Window](https://desktop.github.com/) ou [Linux](https://github.com/shiftkey/desktop)
    [falta um link para um guia para iniciantes em português]
- ou trabalhe com `git` no terminal/linha de comando se preferir.
    [falta um link para um guia para iniciantes em português]

### Para propor correções ou acrescentar novos materiais

#### Preparo
- **Sempre converse antes com as ṕessoas mantenedoras por meio de uma issue antes de propor uma contribuição (*Pull Request*).**
- faça um _fork_ (que é uma cópia deste repositório com o material que vai ficar na sua conta do GitHub, e é onde você vai fazer as contribuições)
- crie um _branch_ (_branch_ é uma etiqueta que marca alternativas ou variantes de um projeto, use algo como: 'melhoria-descrição-abc')
  - Um passo opcional é fazer um *clone* do seu computador, o que permite usar um editor local, aí vocẽ vai precisar aprender a fazer locamente os processos de de `commit` e `push`...

#### Faça modificações no material

- Modifique arquivos, editando os arquivos Markdown (.md) que compõe o material-aulas, no seu clone local ou usando o **botão com o lápis** na interface web do GitHub

- Como se escreve markdown ou [GFM](https://github.github.com/gfm/)? 
  - Guias de markdown em português:
     * [github.com/luong-komorebi/Markdown-Tutorial](https://github.com/luong-komorebi/Markdown-Tutorial/blob/master/README_pt-BR.md#syntax)
     * [github.com/leticiadasilva/notas-de-aula](https://github.com/leticiadasilva/notas-de-aula/blob/master/markdown/anota%C3%A7oes-markdown.md)
   - Para vazer subtítulos use múltiplos `#` , como `##`, `###` e etc. Um só `#` é o título principal da página.
   - Para fazer links `[texto](url)`
        - Exemplo: `[Referência do Processing modo Python](https://py.processing.org/reference)`<br>
          Resultado: [Referência do Processing modo Python](https://py.processing.org/reference)
   - Para formatar texto como código no markdown use a "crase" também chamada de *backtick* ``` ` ``` ou a tripla-crase assim:
       - bloco com ` ```python ___``` `<br>Exemplo:
          ```
              ```python
              def setup():
                  size(400, 400)
              ```
          ```
          Resultado:
          ```python
          def setup():
              size(400, 400)
          ```
      - no meio da frase ` `` `  <br>Exemplo: ```*Use  `noFill()` para desligar o preenchiemto.*```<br>Resultado: *Use  `noFill()` para desligar o preenchiemto.*

#### Acrescentando novos arquivos

- Você pode também criar novos arquivos, use seu editor de código preferido e suba, ou use o botão **Create New File** na interface web para criar um arquivo `.md`.
- Para subir arquivos na interface web, visite a pasta do repositório onde vai ficar o arquivo e o arraste sobre a janela do navegador.
- para inserir imagens no markdown
   - suba o arquivo da imagem (.png preferencialmente)
   - use em uma página o código de um link precedido de uma exclamação `![nome da imagem](local/arquivo.png)`

#### A conclusão do processo com um PR

- faça um *Pull Request* (PR)
  - o que é um PR, pra quê serve, como funciona? 
     - _Pull Request_ é um pedido ao mantenedor para aceitar uma contribuição/modificação no projeto
     - Se possível faça a partir de um _branch_ separado para cada contribuição
     - Seja claro no título e descrição descrevendo a natureza da contribuição
  - Como é a conversa com a pessoa mantenedora? Ela pode te pedir modificações/correções!
  - **Importante: Não dê `CLOSE` quando terminar de fazer as modificações pedidas (isso seria desistir do PR)!!!**
  - [FALTA ESCREVER MELHOR - Como não se frustrar: como calibrar as suas expectativas.]
  
### Exemplos de contribuições úteis

- Procure um material que tem um código exemplo significativo mas que não mostra o resultado visual do código: 
     - copiar no seu IDE o código, e ver se funciona (se não funcionar, pesquisar e possivelmente abrir um issue);
     - capturar o resultado (de preferência em .png);
     - subir a imagem para o seu *fork* deste repositório (de preferência em um *branch* como 'acrescentando-imagens-XXX');
     - editar o arquivo .md com o código acrescentando a referência a imagem `![nome da imagem](assets/imagem-xxx.png)`;
     - fazer um _Pull Request_ descrevendo a sua contribuição!

- Procure uma issue que você acha que consegue "resolver", escrevendo um material novo ou corrigindo um existente.
   
   

### Como atualizar o seu fork em relação ao repositório de origem quando este já "evoluiu"?
<details>
  <summary>Usando a interface web</summary>

     - simplesmente entre no repositório que você precisa atualizar no seu perfil e procure pelo botão verde __Fetch Upstream__.
     - um menu abrirá indicando a situação do seu repositório. Se não houver conflitos, você poderá atualizar apertando o botão verde __Fetch and Merge__.
     ![Botão Fetch](https://github.com/rgobatto/material-aulas/blob/update-como-contribuir/sobre/fetch.png)
     - no caso de existir conflitos, é possível comparar os repositórios e entender onde ocorrem os conflitos, e isso pode ser um pouco mais complexo.

</details>
 
<details>
   <summary>Usando a interface da linha de comando (aponte o terminal para a pasta local do repositório)</summary>

```shell
 # Primeiro você precisa adicionar como remote o repositório original
 
 git remote add upstream https://github.com/usuario/nome-do-repositorio.git

 # depois, você recupera todos os branches daquele remote, incluindo o branch master
 
 git fetch upstream

 # certifique-se que localmente você está na master
 
 git checkout master

 # você pode re-escrever o seu branch 
 # re-escreva a sua master, de forma que seus commits que ainda não estão na
 # master não se percam no meio do caminho
 
 git rebase upstream/master

 # essas alterações todas são feitas apenas localmente. se você quiser atualizar o seu fork,
 # precisa "forçar" o push com as alterações. o -f (de force) só precisa ser usado uma vez após o rebase
 
 git push -f origin master
 
```

 </details>
 
- [Tutorial em português](https://blog.da2k.com.br/2014/01/19/manter-repositorio-github-forkado-sincronizado-com-o-original/)
- Mais informações em inglês [aqui](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) e [aqui](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository)

### Contribua sobre como contribuir

- Meta-contribuição! Dá pra melhorar esta página sobre como melhorar o material.


