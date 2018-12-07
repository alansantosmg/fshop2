""" 
Fashion Shop APP
@Author:  Alan Santos
Actual release: dec-7-2018

Aplicação comentada para propósito de estudos

"""


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
    
    def __init__(self, stock_ref, price, color):  # construtor da classe
        self.stock_ref = stock_ref
        self.__price = price
        self.color = color
        self.__stock_level = stock_level = 0
        self.__StockItem_version = 1

    """ propriedade com metodo acesso ao preco de estoque de 1 item instanciado """   
    @property
    def price(self): 
        return self.__price

    """ propriedade com metodo acesso a quantidade de estoque de 1 item instanciado """      
    @property
    def stock_level(self):
        return self.__stock_level

    """ propriedade com metodo de checagem de versão da classe para fins de migracao """
    def check_version(self):
        pass
    
    """ Metodo de impressao do objeto da classe """      
    def __str__(self):
        pass

class Dress(StockItem): 
    """ Subclasse de Stock Item """
    def __init__(self, stock_ref, price, color, pattern, size):  # construtor da classe               
        super().__init__(stock_ref, price, color) # herança do construtor da superclasse           
        self.pattern = pattern
        self.size = size
        self.__dress_version = 1

    """ propriedade com metodo acesso a quantidade de estoque do item pants """  
    @property
    def stock_level(self):
        return self.__stock_level

    """ propriedade com metodo de checagem de versão da classe para fins de migracao """
    def check_version(self):
        pass

    """ Metodo de impressao do objeto da classe """    
    def __str__(self):
        pass

class Pants(StockItem):
    """ Subclasse de StockItem """
    def __init__(self, stock_ref, price, color, pattern, length, waist, size):
        super().__init__(stock_ref, price, color) # heranca do contrutor da superclase 
        self.__stock_level = 0
        self.pattern = pattern
        self.length = length
        self.waist = waist
        self.size = size


    """ propriedade com metodo de acesso a quantidade de estoque do item pants """
    @property
    def stock_level(self): 
        return self.__stock_level
    
    """ propriedade com metodo de checagem de versão da instancia da classe para fins de migracao """
    def check_version(self): 
        pass

    """ Metodo de impressao da instancia  da classe """  
    def __str__(self): 
        pass

class Jeans(Pants):
    """ Subclasse de StockItem """
    def __init__(self, stock_ref, price, color, pattern, length, size, waist, style):
        super().__init__(stock_ref, price, color, pattern, length, size, waist) # heranca do contrutor da superclase 
        self.__stock_level = 0
        self.style = style


    """ propriedade com metodo de acesso a quantidade de estoque do item pants """
    @property
    def stock_level(self): 
        return self.__stock_level
    
    """ propriedade com metodo de checagem de versão da instancia da classe para fins de migracao """
    def check_version(self): 
        pass

    """ Metodo de impressao da instancia  da classe """  
    def __str__(self): 
        pass












# testes de classe

x = Dress(stock_ref ='d0001', price=10, color='red', pattern='circulos', size='m')
print(x.price)

y = Pants(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, size='m')
print(y.price)

z = Jeans(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, style='cut', size='m')
print(z.price)
