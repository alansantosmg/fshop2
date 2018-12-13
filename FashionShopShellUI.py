from ShellUI import FashionShopShell
from Storage import FashionShop

# referencia a classe FashionShopShell que está 
# dentro do arquivo FashionShopShell
ui = FashionShopShell.FashionShopShell

# referencia a classe FashionShop que está dentro do arquivo FashionShop
shop = FashionShop.FashionShop

# Diz qual arquivo de dados a classe referenciada vai usar
# Diz qual classe de loja vai usar 
app = ui(filename='fshop2.picke', storage_class=shop)

#
# Carrega do método do menu principal da classe refernciada FashionShop
app.main_menu()

