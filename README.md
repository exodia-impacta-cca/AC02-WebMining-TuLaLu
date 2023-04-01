# AC030-WebMining-TuLaLu
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
