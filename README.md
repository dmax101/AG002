# AG002

|Nome|Matrícula|Curso|
|---------|---------|---------|
|Danilo Ribeiro|1411|Eng. Computação|
|Gustavo Simões|1470|Eng. Computação|

---
## Introdução

Este trabalho tem o intúito de treinar e testar o conjunto de dados a partir do modelo de classificação Perceptron.

## Instalação

Para a instalação faça o download do arquivo zip [aqui](https://github.com/dmax101/AG002.git).

Extraia o conteúdo em uma pasta.

![Download Zip](/assets/zip.png)


Se preferir você pode clonar o projeto com o git, caso tenha instalado em sua máquina executando o comando:

```
$ git clone https://github.com/dmax101/AG002.git
```

Este comando irá criar uma pasta com o nome do projeto "AG002".

---
## Instruções para a execução
Este projeto foi feito em Python e utiliza as bibliotecas Pandas, SqlAlchemy, Numpy e Sklearn, estas que são necessárias estarem instaladas na máquina. Para isso execute o seguinte comando no terminal:

```
$ pip install pandas scikit-learn sqlalchemy numpy
```

Pronto. Agora o projeto está preparado para ser executado. Execute o seguinte comando para iniciar:

```
$ python main.py
```

---
## Programa
Após a execução, a aplicação será encarregada de treinar com 80% dos dados e testar em 20% deles.

![Janela da Aplicação](/assets/índice.jpeg)

Podemos interpretar os resultados da seguinte forma:

 - *Precision:* A precisão pode ser interpretada como: dos que eu classifiquei como certos, quantos eram realmente certos?
 - *Recall:* O recall nos diz com que frequência o classificador está encontrando exemplos de uma classe. Se for realmente dessa classe, o quanto frequente você classifica como ela? Seria esta a pergunta a ser respondida.
 - *F1-Score:* O F1 score combina o recall com a precisão de modo que tragam um único número, que quanto mais próximo de 1 melhor. Ele utiliza a seguinte fórmula para calcular:
      ```
      F1 = (2 * precision * recall)/(precision + recall)
      ```
 - *Support:* O suporte é o número de ocorrência de verdadeiros positivos (instâncias de uma determinada classe que foram classificados corretamente para esta mesma classe), e ele pode ser comparado ao número total de instâncias que são desta classe.

 - *Acuraccy:* A acurácia informa em geral o quão o seu modelo está acertando.
 - *Macro:* Calcule a métrica para cada classe e calcule a média não ponderada
 - *Weighted:* Calcula a métrica para cada classe e calcule a média ponderada com base no número de amostras por classe.
