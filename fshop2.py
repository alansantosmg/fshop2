""" 
Fashion Shop APP
@Author:  Alan Santos
Actual release: dec-7-2018

Aplicação comentada para propósito de estudos

"""

# importação de dependencias externas
import btc  # biblioteca de entrada e validação de tipos
import pickle # biblioteca de armazenamento de arquivos binários























# Definição dos itens de menu principal
'''Alan's Loja de Roupas

1: Criar novo item de estoque
2: Adicionar estoque a item existente
3: Vender estoque
4: Relatório de estoque
5: Sair

Digite sua opção: '''




























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
        """ Verifica se quantidade adicionada é menor que zero ou maior que máximo """
        if count < 0 or count > StockItem.max_stock_add: 
            raise Exception('Invalid Add amount') # exceção caso quantidade invalida
        self.__stock_level = self.__stock_level + count # soma nova quantidade a existente



    
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
menu = '''\033[H\033[J
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
add_stock = btc.read_int('Add stock: ') # entra quantidade estoque
stock_item.add_stock(add_stock) # chama metodo que adiciona quantidade no estoque

print(stock_item, '\n')























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