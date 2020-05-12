## Cores com HSB (Matiz, Saturação e Brilho)

Por padrão escolhemos cores no Processing com trincas de números entre 0 e 255 que representam valores de intensidade nos canais R (*Red*, vermelho), G (*Green*, verde) e B (*Blue*, azul). Um quarto número (*Alpha*) pode ser usado para indicar cores translúcidas (0 fica totalmente transparente, e invisível, e 255 totalmente opaca, como se não tivesse sido usado o quarto número).

Mas usando `colorMode(HSB)` é possível usar números representando Matiz (*Hue*), Saturação (*Saturation*) e Brilho (*Brightness*).

