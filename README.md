# AC030-WebMining-TuLaLu
## Integrantes do trabalho
- Arthur Vinicius Santos Silva  RA:1903665
- Larissa Ionafa                RA:1903166
- Lucas da Silva Santos         RA:1904201

Abaixo comandos utilizados para a execução da AC02.

Habilitar o modo Shell do Scrapy para testes:

```shell
scrapy shell   
```


Comando para criar um projeto Scrapy:

```shell
scrapy startproject <<nome-projeto>>
```

Comando para criar um spider (robo para o scrap) no Scrapy:

```shell
scrapy genspider <<nome-spider>> <<url-site>>
```

comando para executar spider e salvar o retorno:

```shell
scrapy crawl <<nome-spider>> -O nome-do-arquivo.tipo-arquivo(csv,json,etc...)
scrapy crawl promocoes-jogos -O ../../../0_bases_originais/original.csv
```
