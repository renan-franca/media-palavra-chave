# Média de palavras-chave no Google Trends
Projeto em Python para buscar as médias de palavras-chave no Google Trends.

## Contexto: 
O projeto foi desenvolvido como trabalho final da disciplina de Pensamento Computacional, do professor Álvaro Justen (Turicas), da Pós-Graduação em Jornalismo de Dados, Automação e Storytelling do Insper. A ferramenta usada para escrever o código foi o Google Colab.

## Como o projeto está organizado?
O repóstório é simples. Além do compartilhamento do código, a página da licença escolhida, há o arquivo README.md em que existe uma explicação sobre os detalhes e as motivações do trabalho. 

## Por que o projeto foi criado?
O projeto foi feito para descobrir boas oportunidades de palavras-chave muito buscadas e que se mantêm estáveis ao longo do tempo no [Google Trends](https://trends.google.com.br/trends/). A ferramenta é boa, mas a opção padrão disponível não permite comparar mais de 5 buscas de palavras-chave ao longo do tempo.

## Objetivo
Usar uma API do Google Trends para criar um programa que me permita buscar a média de buscas de cada palavra-chave e não fique restrito a apenas a 5 buscas.

## Instalação
É necessário usar o Python acima da versão 2.7+.

```bash
!pip install pytrends
```
## Como usar
Você pode clonar o projeto e editar o arquivo main-keyword.py, adicionado as palavras-chave que você gostaria de consultar e selecionando o período de tempo. Ao rodar o código, você verá o print no console das médias de todas as palavras-chave. Além disso, será gerada uma planilha .csv com todas as palavras-chaves e suas médias durante o período de tempo selecionado.

Veja abaixo o código em destaque:

Na variável "all-keywords" é possível inserir a palavra-chave que deseja buscar. No exemplo, estou inserindo nomes de linguagens de programação.

![image](https://user-images.githubusercontent.com/83841256/136832193-a8caddea-3be3-433f-bc91-16a9bc688a88.png)

Ao rodar o código, temos o resultado da média de busca de cada palavra-chave.

![image](https://user-images.githubusercontent.com/83841256/136832336-7d6ba2cc-4975-450b-a5d8-cddcccb4441b.png)

O resultado é automaticamente exportado para uma planilha no formato .csv.

![image](https://user-images.githubusercontent.com/83841256/136832423-ce117adb-ef1c-471f-a385-0199cb260fa4.png)


## Por que usamos a biblioteca Pytrends
Pytrends é uma API não-oficial do Google Trends. A lib permite uma interface simples para automatizar o download de relatórios do Google Trends.
