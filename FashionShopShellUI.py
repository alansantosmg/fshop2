from ShellUI import FashionShopShell
from Storage import FashionShop

ui = FashionShopShell.FashionShopShell
shop = FashionShop.FashionShop

app = ui(filename='fshop2.picke', storage_class=shop)
app.main_menu()