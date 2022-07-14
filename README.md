# TODO4: CONTRATADO

## Objetivo do Projeto

Este projeto foi feito como atividade do Módulo 2 do 
curso Data Analytics da Resilia Educação da turma 20.

## Descrição do Projeto

A ideia deste trabalho é realizar a contagem de 
currículos para determinadas vagas e classificar 
quantos candidatos tem o perfil necessário e quantos
candidatos estão concorrendo para cada vaga.
Este projeto é feito utilizando dicionários que irão
gravar a quantidade de currículos para cada vaga e 
quantas pessoas têm pelo menos uma das palavras 
chaves necessárias no currículo. Para isso, nosso 
código Python vai checar quantos candidatos estão se
inscrevendo, para qual vaga, nome do candidato e um 
resumo que a pessoa está enviando.
O critério de qualificação do candidato para a vaga é
que o seu resumo possua pelo menos uma das
palavras-chave determinadas.
Serão analisadas 2 vagas com as respectivas 
palaras-chave:

	- Vaga analista de dados com as palavras-chave: 
	Python, PowerBI, SQL, Boa comunicação.

e

	- Vaga cientista de dados com as palavras chaves:
	Python, Banco de dados, Machine Learning, 
	Resolução De Problemas, Estatística

## Funcionamento

Este código possui duas versões distintas de 
funcionamento, cada uma delas será explicada abaixo:

	Versão 1:

Esta versão se comporta como o específicado na 
descrição do projeto. São feitas as perguntas: 
Quantos candidatos serão cadastrados; 
Qual o nome do candidato; 
Para qual vaga está se inscrevendo; 
E um pequeno texto com o resumo do currículo do 
participante; O texto do resumo vai ser informado 
pelo usuário e então vamos verificar se pelo menos 
uma palavra chave da vaga está presente no resumo 
enviado pelo candidato.

Ao final, nosso código deve mostrar como saída: 
quantas pessoas estão inscritas em cada vaga; 
e quantas pessoas tem o resumo com as palavras 
que estamos buscando.

	Versão 2:

Esta versão abre os resumos a partir de arquivos
.txt colocados no mesmo diretório do código. 
São feitas as perguntas: 
Quantos candidatos serão cadastrados; 
Qual o nome do candidato; 
Para qual vaga está se inscrevendo; 
É pedido um pequeno texto com o resumo do currículo do 
participante; O texto do resumo deverá ser colocado em
um arquivo .txt e nomeado como: 
'summary[índice do candidato].txt', começando pelo 
índice 0 para o 1º candidato e sendo incrementado 
por uma unidade até chegar a quantidade informada de 
candidatos. Por exemplo, se uma quantidade n 
informada de canditados, no mesmo diretório do 
código teremos os seguintes arquivos:

	summary0.txt   (RESUMO 1)
	summary1.txt
	     ...
	sumaryn-1.txt  (RESUMO N)


No arquivo vamos verificar se pelo menos 
uma palavra chave da vaga está presente no resumo 
enviado pelo candidato.

Ao final, nosso código deve mostrar como saída: 
quantas pessoas estão inscritas em cada vaga; 
e quantas pessoas tem o resumo com as palavras 
que estamos buscando.
