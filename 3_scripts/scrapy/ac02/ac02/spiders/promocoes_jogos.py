import scrapy

class PromocoesJogosSpider(scrapy.Spider):
    name = "promocoes-jogos"
    allowed_domains = ["nuuvem.com"]
    # start_urls = ["http://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc", \
    #               "https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/2", \
    #                 "https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/3", \
    #                 "https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/4", \
    #                 "https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/5"]

    start_urls = ["http://www.nuuvem.com/br-pt/catalog/platforms/pc/sort/bestselling/sort-mode/desc", \
                  "https://www.nuuvem.com/br-pt/catalog/platforms/pc/sort/bestselling/sort-mode/desc/page/2", \
                    "https://www.nuuvem.com/br-pt/catalog/platforms/pc/sort/bestselling/sort-mode/desc/page/3", \
                    "https://www.nuuvem.com/br-pt/catalog/platforms/pc/sort/bestselling/sort-mode/desc/page/4", \
                    "https://www.nuuvem.com/br-pt/catalog/platforms/pc/sort/bestselling/sort-mode/desc/page/5"]

    def parse(self, response):
        for jogo in response.css(".product-card--grid"): 
            moeda = jogo.css(".product-card--grid .currency-symbol::text").get()
            inteiro = jogo.css(".product-card--grid .integer::text").get()
            decimal = jogo.css(".product-card--grid .decimal::text").get()
            yield {
                "nome": jogo.css('.product-card--grid .double-line-name::text').get() or jogo.css('.product-card--grid .single-line-name::text').get() ,
                "porcentagem_desconto": jogo.css('.product-card--grid .product-price--discount::text').get() or "sem desconto",
                "preco": f"{moeda}{inteiro}{decimal}",
                "tipo": jogo.css('.product-card--grid .product-badge__preorder::text').get() or jogo.css('.product-card--grid .product-badge__dlc::text').get() or jogo.css('.product-card--grid .product-badge__package::text').get() or "Padrão"
            }
        pass
