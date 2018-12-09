""" 
Fashion Shop APP
@Author:  Alan Santos
Actual release: dec-7-2018

Aplicação comentada para propósito de estudos

"""

# importação de dependencias externas
import btc  # biblioteca de entrada e validação de tipos
import pickle # biblioteca de armazenamento de arquivos binários


































































class StockItem(object):  # (object define superclasse de maior nível)
    """ Superclasse com atributos principais de item de estoque """
    
    # atributos estáticos da classe
    # Nao entra em init pois devem ser consultados antes do objeto ser criado
    min_price = 10
    max_price = 10000

    def __init__(self, stock_ref, price, color):  # construtor da classe
        self.stock_ref = stock_ref
        self.__price = price
        self.color = color
        self.__stock_level = 0
        self.__StockItem_version = 1

        


    @property
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem atributo)"""
        return 'Stock Item' # o valor retornado será o nome do objeto da classe

    @property
    def price(self): 
        """ propriedade com metodo acesso ao preco de estoque de 1 item instanciado """   
        return self.__price

        
    @property
    def stock_level(self):
        """ propriedade com metodo acesso a quantidade de estoque de 1 item instanciado """  
        return self.__stock_level


    @property
    def location(self):
        """ 
        Obtem o valor de atributo  definido e armazena em variavel. A seguir retorna a variável
        Se não existir valor no atributo retorna nada. 
        Sempre vem antes do setter
        """
        result = getattr(self, '_location', None)
        return result


    @location.setter        
    def location(self, location):
        """ 
        Define um atributo via setter e recebe parametro de valor para este atributo.
        Sempre vem depois do GET. Observar a ordem no programa.
        """
        self._location = location


     
    max_stock_add = 10   # Quantidade máxima de itens para estoque 
    
    def add_stock(self,count): 
        """ 
        Verifica se quantidade adicionada é menor que zero ou maior que máximo.
        Caso seja gera exceção.
        Se quantidade estiver ok adiciona ao estoque.
        """
        if count < 0 or count > StockItem.max_stock_add: 
            raise Exception('Invalid Add amount') 
        self.__stock_level = self.__stock_level + count 

    def sell_stock(self,count): 
        """ 
        metodo que retira itens do estoque.
        se quantidade for maior que estoque, entra em loop e 
        informa usuario a quantidade disponível em estoque.
        Se a quantidade for menor gera exceção.
        Se quantidade for subtrai do estoque.
        """       
        if count < 1: 
            raise Exception('Invalid number of itens to sell')
        if count > self.__stock_level: 
            raise Exception('Not enough stock to sell')
        self.__stock_level = self.__stock_level - count
        

    
    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        pass
    
         
    def __str__(self):
        """ Metodo de impressao do objeto da classe """ 
        template ='''
Stock Reference: {0}
Type: {1}
price: {2}
Stock Level: {3}
Color: {4}'''
        return template.format(self.stock_ref, self.item_name, 
                                self.price, self.stock_level, self.color)










































class Dress(StockItem): 
    """ Subclasse de Stock Item """
    def __init__(self, stock_ref, price, color, pattern, size):  # construtor da classe               
        super().__init__(stock_ref, price, color) # herança do construtor da superclasse           
        self.pattern = pattern
        self.size = size
        self.__Dress_version = 1
         
    @property # esta propriedade está sobrescrevendo (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem variavel atributo)"""
        return 'Dress' # a string retornada será o nome do objeto da classe


    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass
        
     
    def __str__(self):
        """ Metodo de impressao do objeto da classe """ 
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Pattern: {1}
Size: {2}'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details,self.pattern, self.size)






































class Pants(StockItem):
    """ Subclasse de StockItem """
    def __init__(self, stock_ref, price, color, pattern, length, waist, size):
        super().__init__(stock_ref, price, color) # heranca do contrutor da superclase 
        self.pattern = pattern
        self.length = length
        self.waist = waist
        self.size = size
        self.__Pants_version = 1
    
    @property # esta propriedade está sobrescrevendo (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem variavel atributo)"""
        return 'Pants' # a string retornada será o nome do objeto da classe
    
    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass

      
    def __str__(self): 
        """ Metodo de impressao da instancia  da classe """
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Pattern: {1}
Length: {2}
Waist: {3}
Size: {4}'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details,self.pattern, self.length, self.waist, self.size)




























class Jeans(Pants):
    """ Subclasse de StockItem """
    def __init__(self, stock_ref, price, color, pattern, length, size, waist, style):
        super().__init__(stock_ref, price, color,pattern,length,waist,size) # heranca do contrutor da superclase 
        self.style = style
        self.__Jeans_version = 1
    
    @property # esta propriedade está sobrescrevendo (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem variavel atributo)"""
        return 'Jeans' # a string retornada será o nome do objeto da classe
    
    def check_version(self): 
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass

    
    def __str__(self): 
        """ Metodo de impressao da instancia  da classe """  
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Style: {1}
'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details,self.style)





















class Blouses(StockItem):
    def __init__(self, stock_ref, price, color, size, pattern, style):
        super().__init__(stock_ref, price, color)
        self.pattern = pattern
        self.style = style
        self.size = size
        self.__Blouses_version = 1

    @property # (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático  (sem variavel atributo)"""
        return 'Blouse' # a string retornada será o nome do objeto da classe

    def check_version(self):
        """" classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Checando versão da superclass, alem da subclasse
        pass
    
    def __str__(self):
        """ Metodo de impressao da instancia  da classe """ 
        # Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Pattern: {1}
Style {2}
Size: {3}'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details, self.pattern, self.style, self.size)



























class Hats(StockItem): # subclasse de stockitem
    def __init__(self, stock_ref, price, color, size):  # construtor       
        super().__init__(stock_ref, price, color) # herda construtor de StockItem
        self.size = size
        self.__hats_version = 1

    @property # esta propriedade está sobrescrevendo (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem variavel atributo)"""
        return 'Hat' # a string retornada será o nome do objeto da classe   

    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass
    
    def __str_(self):
        """ Metodo de impressao da instancia  da classe """  
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Size: {1}'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details, self.size)







































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

    # cria objeto stock_item do tipo Dress
    # e usa entrada de usuaro como parametro
    stock_item = Dress(stock_ref = stock_ref, 
                       price = price,
                       color = color,
                       pattern = pattern,
                       size = size)

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

    # cria objeto stock_item do tipo Pants
    # usa entrada de usuário como parametros
    stock_item = Pants(stock_ref = stock_ref,
                       price = price, 
                       color = color,
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

    # cria objeto stock_item da classe hats
    # usa entrada de usuários como parametro do objeto
    stock_item = Hats(stock_ref=stock_ref,
                      price=price,
                      color=color,
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

    # cria objeto stock item da classe blouse
    # usa entrada de usuaŕio como parametros do objeto
    stock_item = Blouses(stock_ref=stock_ref, 
                         price=price,
                         color=color,
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

    # cria objeto jeans
    # usa valores de entrada como parametro do objeto
    stock_item = Jeans(stock_ref=stock_ref, 
                       price=price, 
                       color=color,
                       pattern=pattern,
                       waist=waist,
                       length=length,
                       style=style,
                       size=size)

print('\033[H\033[J') # limpa tela



#TODO: Esta acao deve ser colocada em item do menu principal a ser construido
add_stock = btc.read_int('Add stock: ') # entra quantidade para adicionar estoque
stock_item.add_stock(add_stock) # chama metodo que adiciona quantidade no estoque

print(stock_item, '\n')

#TODO: Esta ação deve ser colocada em item do menu principal a ser construido
# diminui quantidade de estoque do item
# mínimo 1 
# maximo é a quantidade de estoque no item





print(stock_item, '\n')


































class FashionShop: 
    """ 
    Componente de operação principal
    Define principais operações da loja com estoque
    criar nova loja, carregar arquivo de loja, armazenar item de estoque,
    buscar item de estoque, listar itens em estoque
    """
    def __init__(self):
        self.__stock_dictionary = {}


    @staticmethod
    def load(filename): 
        """ Necessário criar método estático para carregamento
            pois quando arquivo é carregado o objeto componente
            instanciado da classe FashionShop ainda não existe. 
            Por isso o método deve ser da "classe" e não do objeto. 
            Por questão de organização, o método estático será colocado
            sempre antes do construtor da classe. 
            caso não consiga carregar o arquivo deve criar loja vazia. 
         """
        with open(filename,'rb') as input_file:  #abre conexão
            result = pickle.load(input_file)  # carrega arquivo em result
            return result  #retorna arquivo carregado


    def save(self, filename): 
        """  Salva fashion shop item em um dado arquivo
             exceção deve ser gerada caso não consiga salvar. 
         """
        with open(filename,'wb') as out_file: # abre conexão
            pickle.dump(self,out_file)  # descarrega objeto no arquivo
        

    def store_new_stock_item(self, stock_item):
        """ Cria novo item na fashion shop
        Este item é indexado pelo atributo stock_ref
        Gera execao se item já estiver armazenado na loja
         """
        if stock_item.stock_ref in self.__stock_dictionary: #verfica se chave do indice existe no dicionário 
            raise Exception('Item já existe') # excecao se item existir no dicionário
        self.__stock_dictionary[stock_item.stock_ref] = stock_item #se não existir grava, usando stock_ref como indice
        

    def find_stock_item(self, stock_ref):  
        """ Obtem item do stock
        retorna nada se item não existir
             
         """
        if stock_ref in self.__stock_dictionary:  # busca uma chave no indice do dicionario
            return self.__stock_dictionary[stock_ref]  # se existir retorna item da chave
        else:
            return None


    def __str__(self): 
        """ Lista items da loja """
        stock = map(str, self.__stock_dictionary.values()) # mapeia valores de string do dicionario
        stock_list = '\n'.join(stock) #imprime fila de valores mapeados 1 por linha
        template = '''Itens in Stock 
{0}
''' 
        return template.format(stock_list)  #formata e retorna lista de items do dicionário








class FashionShopShellApplication: 
    """ Classe de interface do usuario """
    def __init__(self,filename): 

        #recebe parametro filename e guarda em atributo privado
        FashionShopShellApplication.__filename = filename
        
        #tenta carregar loja usando nome de arquivo guardado no atributo 
        try: 
            self.__shop = FashionShop.load(filename)
        except: 
            print('File not found.')  # Se não achar arquivo no disco avisa usuario
            print('Creating an empty Fashion Shop') 
            self.__shop = FashionShop() #inicia loja vazia

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
                self.__shop.save(FashionShopShellApplication.__filename) 
                print('Shop data saved')
                break


ui = FashionShopShellApplication('dressshop1.pickle')
ui.main_menu()






























# Definição dos itens de menu principal























# testes de classe substituidos pela instrucao print(stock_item) do menu item
'''
v = Dress(stock_ref ='d0001', price=10, color='red', pattern='circulos', size='m')
w = Pants(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, size='m')
x = Jeans(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, style='cut', size='m')
y = Blouses(stock_ref ='d0001', price=120, color='red', pattern='circulos', style='m', size='m')
z = Hats(stock_ref ='d0001', price=10, color='red', size='m')

'''

"""
test_print ='''Teste de impressão de classes)

{0}

{1}

{2}

{3}

{4}'''

print(test_print.format(v,w,x,y,z))
"""