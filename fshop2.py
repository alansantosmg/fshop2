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

    
    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        pass
    
         
    def __str__(self):
        """ Metodo de impressao do objeto da classe """ 
        template ='''Stock Reference: {0}
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

    @property # esta propriedade está sobrescrevendo (overriding) a da superclasse
    def item_name(self): 
        """ Retorna um valor estático guardado na propriedade (sem variavel atributo)"""
        return 'Blouse' # a string retornada será o nome do objeto da classe

    def check_version(self):
        """" classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass
    
    def __str__(self):
        """ Metodo de impressao da instancia  da classe """ 
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
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




























v = Dress(stock_ref ='d0001', price=10, color='red', pattern='circulos', size='m')

w = Pants(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, size='m')

x = Jeans(stock_ref ='d0001', price=10, color='red', pattern='circulos', waist='m', length=10, style='cut', size='m')

y = Blouses(stock_ref ='d0001', price=120, color='red', pattern='circulos', style='m', size='m')

z = Hats(stock_ref ='d0001', price=10, color='red', size='m')




test_print ='''Teste de impressão de classes)

{0}

{1}

{2}

{3}

{4}'''

print(test_print.format(v,w,x,y,z))