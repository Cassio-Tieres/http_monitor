# HTTP Monitor

Projeto de estudo desenvolvido em python com o objetivo de aprimorar meu conhecimento quanto ao protocolo HTTP.

## Objetivo
Principalmente desenvolvido para monitorar mudanças repentinas de status code de um site, no sentido de encontrar erros e falhas no processamento de informações, prevenindo problemas com o cliente final e colaborando para a resolução destas falhas.

## Tools e Libs

* Requests
* Socket
* Logging
* Time

## Utilização
Clone este repositório em alguma pasta de sua escolha. Em seguida, abra o terminal na pasta do projeto e execute o comando:

````bash
python main.py
````
Após a execução do arquivo, escreva o nome do site que você quer monitorar:

````bash
Digite o link do site https://
````
Escreva o nome do site, sem utilizar o "https://".
Ex: google.com.br

Após isso, o código irá verificar o status HTTP a cada 3 segundos, retornando um erro, caso o código HTTP seja diferente de 200.