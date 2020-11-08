# O que é e como instalar o p5py

O projeto [p5py](https://github.com/p5py/p5) é uma versão nova (experimental ainda) das ideias do Processing implementadas em Python 3. Você pode usar com um editor de código / IDE de sua preferência (em oposição ao IDE do Processing), mas precisa ter um Python 3 instalado no seu computador.

## Como instalar

Para instalar o p5py em qualquer plataforma é necessário ter previamente instalado o Python 3 e o GLFW. 

Você pode verificar a versão instalada no seu computador através do Terminal ou Prompt de Comando, através do comando:

```
python --version
```

O Python 3 e o GLFW tem instruções específicas de instalação para cada plataforma.

### Linux

### macOS

Para o macOS, é fundamental ter o Homebrew, que é um gerenciador de pacotes que te permite instalar o Python 3 e o GLFW.

As instruções de instalação do Homebrew estão disponíves [neste link](https://brew.sh/index_pt-br).

Uma vez instalado o Homebrew, execute os seguintes comandos no Terminal para instalação das dependências:

```sh
# Para instalar o Python 3
brew install python3

# Para instalar o GLFW
brew install glfw
```
 

### Windows


### Instalação comum

Ao final, para instalar o p5py, execute o seguinte comando no Terminal ou Prompt de Comando: 

```
pip install p5
```
 
