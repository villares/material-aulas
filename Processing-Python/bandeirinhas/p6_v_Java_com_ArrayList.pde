/*  Exemplo de uso da classe Bandeirinhas, com mudança de cor 'mouse over'
 *  clique para acrescentar um objeto, tecle 'espaço' para remover.
 */

ArrayList<Bandeirinha> bandeirinhas; // lista de objetos

void setup() {
  /* define área de desenho e popula lista de bandeirinhas */
  size(400, 400);  // área de desenho
  float meia_largura = width / 2;
  float meia_altura = height / 2;
  bandeirinhas = new ArrayList<Bandeirinha>();
  for (int i=0; i <50; i++) {
    bandeirinhas.add(new Bandeirinha(meia_largura, meia_altura, 0));
  }
}

void draw() {
  /* Limpa a tela, desenha e atualiza bandeirinhas */
  background(0);  // atualização do desenho, fundo preto
  for (Bandeirinha bandeira : bandeirinhas) {
    bandeira.desenha();
    bandeira.anda();
  }
}

void mousePressed() {
  /* Acrescenta pequena bandeirinha branca */
  Bandeirinha nova_bandeirinha = new Bandeirinha(mouseX, mouseY, 25);
  nova_bandeirinha.cor = color(255);  // forçando que seja branca!
  bandeirinhas.add(nova_bandeirinha);
}

void keyPressed() {  
  /* tecla 'espaço' remove a última bandeirinha da lista */
  int num_bandeirinhas =  bandeirinhas.size();
  if (key == ' ' && num_bandeirinhas > 1) {
     bandeirinhas.remove(num_bandeirinhas - 1);
  }
}

class Bandeirinha {
  /* Classe Bandeirinha, cor sorteada, tamanho sorteado por voidault */
  float x, y, vx, vy, tamanho;
  color cor;
  Bandeirinha(float px, float py, float ptamanho) {
    x = px;
    y = py;
    if (ptamanho != 0) {
      tamanho = ptamanho;
    } else {
      tamanho = random(50, 200);
    }
    vx = random(-1, 1);
    vy = random(-1, 1);
    cor = color(random(255), // R
      random(255), // G
      random(255), // B
      200);  // alpha
  }

  void desenha() {
    /* Desenha polígono em torno das coordenadas do objeto */
    float metade = tamanho / 2;
    pushMatrix();   // preseservando o sistema de coordenadas anterior
    translate(x, y);  // translada o sistema de coordenadas
    noStroke() ; // sem contorno
    // se o mouse estiver longe, normal, senão, branca
    if (dist(mouseX, mouseY, x, y) > metade) {
      fill(cor);
    } else {
      fill(255, 100);
    }
    beginShape();  // inicia polígono
    vertex(-metade, -metade);
    vertex(-metade, metade);
    vertex(0, 0);
    vertex(metade, metade);
    vertex(metade, -metade);
    endShape(CLOSE);  // encerra polígono, fechando no primeiro vértice
    popMatrix();
  }
  void anda() {
    /* atualiza a posição do objeto e devolve do lado oposto se sair */
    x += vx;
    y += vy;
    float metade = tamanho / 2;
    if (x > width + metade) x = -metade;
    if (y > height + metade) y = -metade;
    if (x < -metade) x = width + metade;
    if (y < -metade) y = height + metade;
  }
}
