## Mais sobre definir cores

Vamos falar aqui sobre como definir as cores, fingindo que podemos definí-las pelas emissões de frequências das 'luzinhas' no monitor ou no projetor que vai mostrar nosso trabalho, mas a verdade é de que a síntese final da cor acontece em um lugar escuro e úmido, o cérebro. A percepção de cor no final das contas depende do contexto em que ela se apresenta, um pixel que em teoria emite uma determinada cor vai ser entendido como outra dependendo do resto da imagem à sua volta. Se quiser ler mais sobre isso, procure sobre a neurociência da percepção das cores.

### Definindo cores com RGB (ou RGBA)

Por padrão escolhemos cores no Processing com trincas de números entre 0 e 255 que representam valores de intensidade nos canais R (*Red*, vermelho), G (*Green*, verde) e B (*Blue*, azul). Um quarto número (*Alpha*) pode ser usado para indicar cores translúcidas (0 fica totalmente transparente, e invisível, e 255 totalmente opaca, como se não tivesse sido usado o quarto número).

### Cores com HSB (Matiz, Saturação e Brilho)

Se chamaramos a função *colorMode* com a constante **HSB**, `colorMode(HSB)`, podemos passar a usar números representando Matiz (*Hue*), Saturação (*Saturation*) e Brilho (*Brightness*). É possível reverter pra o modo **RGB** chamando `colorMode(RGB`.

