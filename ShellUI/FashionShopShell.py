
from ShellUI import btc
import pickle
from Storage.StockItem import StockItem
from Storage.Dress import Dress
from Storage.Pants import Pants
from Storage.Blouses import Blouses
from Storage.Jeans import Jeans
from Storage.Hats import Hats


class FashionShopShell: 
    """ Classe de interface do usuario """
    def __init__(self,filename, storage_class): 

        #recebe parametro filename e guarda em atributo privado
        FashionShopShell.__filename = filename
        
        #tenta carregar loja usando nome de arquivo guardado no atributo 
        try: 
            self.__shop = storage_class.load(filename)
        except: 
            print('File not found.')  # Se não achar arquivo no disco avisa usuario
            print('Creating an empty Fashion Shop') 
            self.__shop = storage_class() #inicia loja vazia

    def sell_stock(self):      
        """ 
        Vende uma quantidade de item do stoque. 
        Procura por um item e le numero de itens vendidos
        Não permite vender mais itens do que já existe no estoque
       
        """
        print('Sell Item')

        # le entrada do usuario sobre item que quer vender
        item_stock_ref = btc.read_text('Enter the stock reference: ')
        
        # busca entrada do usuário no dicionario com metodo find
        item = self.__shop.find_stock_item(item_stock_ref)

        # se não encontrar nada retorna None
        if item == None : 
            print('This item was not found')
            return

        # se encontrar item no dicionario inicia venda
        print('selling')
        print(item)

        # se estoque for zero, retorna
        if item.stock_level == 0:
            print ('There are none in stock')
            return

        # se quantidade for menor que zero ou maior que maximo
        # solicita novo numero via funcao de BTC
        number_sold = btc.read_range_int(prompt='Sell stock (ou zero para sair): ', 
                                min_value=0, 
                                max_value=item.stock_level) # entra quantidade a subtrair do estoque
        
        # se quantidade for zero retorna
        if number_sold == 0: 
            print('Sell item abandoned')
            return
        # se quantidade for maior que zero e menor/igual que max_value efetua venda
        item.sell_stock(number_sold)

        # informa que item foi vendido
        print('Items sold')

    def create_new_stock_item(self):

        # prompt do menu mostrado para inclusão de itens
        menu = '''
        Create new stock item

        1: Dress
        2: Pants
        3: Hat
        4: Blouse
        5: Jeans

        What kind of item do you want to add: '''

        """ Definição das ações dos itens de menu """
        # receber entrada do usuario p/ menu de inclusao de itens
        item = btc.read_range_int(prompt=menu, min_value=1, max_value=5)

        if item == 1: 
            print('Creating Dress')
            
            # recebe entrada do usuario para item
            stock_ref = btc.read_text('Enter stock reference: ')
            price = btc.read_range_float(prompt = 'Entre price: ', 
                                        min_value = StockItem.min_price, 
                                        max_value = StockItem.max_price)
            color = btc.read_text('Enter color: ')
            pattern = btc.read_text('Enter pattern: ')
            size = btc.read_text('Enter size: ')

            tag_string = btc.read_text('Enter tags (separated by commas): ') #entra dados
            tag_string = StockItem.get_tag_set_from_text(tag_string)

            # cria objeto stock_item do tipo Dress
            # e usa entrada de usuaro como parametro
            stock_item = Dress(stock_ref = stock_ref, 
                            price = price,
                            color = color,
                            pattern = pattern,
                            size = size,
                            tags = tag_string)

        elif item ==2: 
            print('Creating pants')

            # recebe entrada do usuario para item
            stock_ref = btc.read_text('Enter stock reference: ')
            price = btc.read_range_float(prompt = 'Enter price: ', 
                                        min_value = StockItem.min_price,
                                        max_value = StockItem.max_price)
            color = btc.read_text('Enter color: ')
            pattern = btc.read_text('Enter pattern: ')
            waist = btc.read_int('Enter waist: ')
            length = btc.read_int('Enter length: ')
            size = btc.read_text('Enter size: ')

            tag_string = btc.read_text('Enter tags (separated by commas): ') #entra dados
            tag_string = StockItem.get_tag_set_from_text(tag_string) # formata tags



            # cria objeto stock_item do tipo Pants
            # usa entrada de usuário como parametros
            stock_item = Pants(stock_ref = stock_ref,
                            price = price, 
                            color = color,
                            tags = tag_string,
                            pattern = pattern,
                            waist = waist, 
                            length = length,
                            size = size)

        elif item == 3: 
            print('Creating hat')

            #recebe entrada de usuario para item
            stock_ref = btc.read_text('Enter stock reference: ')
            price = btc.read_range_float(prompt='Enter price: ',
                                        min_value=StockItem.min_price, 
                                        max_value=StockItem.max_price)
            color = btc.read_text('Enter color: ')
            size = btc.read_text('Enter size: ')

            tag_string = btc.read_text('Enter tags (separated by commas): ') #entra dados
            tag_string = StockItem.get_tag_set_from_text(tag_string) # formata tags


            # cria objeto stock_item da classe hats
            # usa entrada de usuários como parametro do objeto
            stock_item = Hats(stock_ref=stock_ref,
                            price=price,
                            color=color,
                            tags = tag_string,
                            size=size)

        elif item == 4:
            print('Creating Blouse')

            # recebe entrada de usuario para item
            stock_ref = btc.read_text('Enter stock reference: ')
            price = btc.read_range_float(prompt='Enter price: ',
                                        min_value=StockItem.min_price,
                                        max_value=StockItem.max_price)
            color = btc.read_text('Enter color: ')
            pattern = btc.read_text('Enter pattern: ')
            style = btc.read_text('Enter style: ')
            size = btc.read_text('Enter size: ')

            tag_string = btc.read_text('Enter tags (separated by commas): ') #entra dados
            tag_string = StockItem.get_tag_set_from_text(tag_string) # formata tags


            # cria objeto stock item da classe blouse
            # usa entrada de usuaŕio como parametros do objeto
            stock_item = Blouses(stock_ref=stock_ref, 
                                price=price,
                                color=color,
                                tags = tag_string,
                                pattern=pattern,
                                style=style,
                                size=size) 

        elif item == 5: 
            print('Creating Jeans')

            # recebe entrada de usuario para item
            stock_ref = btc.read_text('Enter stock reference: ')
            price = btc.read_range_float(prompt='Enter price: ', 
                                        min_value=StockItem.min_price,
                                        max_value=StockItem.max_price)
            color = btc.read_text('Enter color: ')
            pattern = btc.read_text('Enter pattern: ')
            waist = btc.read_int('Enter waist: ')
            length = btc.read_int('Enter length: ')
            style = btc.read_text('Enter style: ')
            size = btc.read_text('Size: ')

            tag_string = btc.read_text('Enter tags (separated by commas): ') #entra dados
            tag_string = StockItem.get_tag_set_from_text(tag_string) # formata tags


            # cria objeto jeans
            # usa valores de entrada como parametro do objeto
            stock_item = Jeans(stock_ref=stock_ref, 
                            price=price, 
                            color=color,
                            tags = tag_string,
                            pattern=pattern,
                            waist=waist,
                            length=length,
                            style=style,
                            size=size)

        print('\033[H\033[J') # limpa tela
        self.__shop.store_new_stock_item(stock_item)
        print(stock_item)


    def add_stock(self):
        print('add Item')

        # le entrada do usuario sobre item que quer vender
        item_stock_ref = btc.read_text('Enter the stock reference: ')
                
        # busca entrada do usuário no dicionario com metodo find
        item = self.__shop.find_stock_item(item_stock_ref)

        # se não encontrar nada retorna None
        if item == None : 
            print('This item was not found')
            return

        # se encontrar item no dicionario inicia reposicao de estoque
        print('Adding stock')
        print(item)

        # se quantidade for menor que zero ou maior que maximo
        # solicita novo numero via funcao de BTC
        number_add = btc.read_int('Add stock (ou zero para sair): ')
                
        # se quantidade for zero retorna
        if number_add == 0: 
            print('Sell item abandoned')
            return
        # se quantidade for maior que zero e menor/igual que max_value efetua venda
        item.add_stock(number_add)

        print(item)

    def do_report(self):
        prompt ='''
1: Listar item de estoque
2: Listar todos itens de estoque
3: Buscar item de estoque por tags

Escolha opção que quer listar: '''

        command = btc.read_range_int(prompt, min_value=1, max_value=3)
        if command == 1: 
            # le entrada do usuario sobre item que quer vender
            item_stock_ref = btc.read_text('Enter the stock reference: ')
                
            # busca entrada do usuário no dicionario com metodo find
            item = self.__shop.find_stock_item(item_stock_ref)

            # se não encontrar nada retorna None
            if item == None : 
                print('This item was not found')
                return
            # se item for encontrado, mostra item
            print('Item de estoque:\n')
            print(item,) #imprime item
            input('\nPressione qualquer tecla...')

        elif command ==2:
            # imprime objeto FashionShop.__shop
            # Como é o próprio objeto instanciado que faz isso, pode usar self.
            print(self.__shop)
            input()
        elif command ==3: 

        
            # busca solicita entrada de tags a localizar
            search_tags = btc.read_text('Entre com tags a buscar: ')
            
            # formata tags
            search_tags = StockItem.get_tag_set_from_text(search_tags)
            
            # Chama metodo de localização de tags
            itens = self.__shop.find_matching_with_tags(search_tags)
            
            # Converte / mapeia dados do objeto em forma de strings
            stock = map(str,itens)
            # Extrai dados em forma de string para lista dados extraídos
            stock_list = '\n'.join(stock)
            # formta dados para impressão
            template = '''Match itens

{0}'''      
            # mostra dados para usuário
            print (template.format(stock_list))
            

    def main_menu(self):  #metodo que carrega menu principal
        prompt = '''Alan's Loja de Roupas

1: Criar novo item de estoque
2: Adicionar estoque a item existente
3: Vender estoque
4: Relatório de estoque
5: Sair

Digite sua opção: '''

        while(True):
            command = btc.read_range_int(prompt, 1, 5)
            if command == 1:
                self.create_new_stock_item()
            elif command ==2: 
                self.add_stock()
            elif command == 3: 
                self.sell_stock()
            elif command == 4: 
                self.do_report()
            elif command == 5: 
                self.__shop.save(FashionShopShell.__filename) 
                print('Shop data saved')
                break

