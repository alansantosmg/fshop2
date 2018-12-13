class StockItem(object):  # (object define superclasse de maior nível)
    """ Superclasse com atributos principais de item de estoque """
    
    # atributos estáticos da classe
    # Nao entra em init pois devem ser consultados antes do objeto ser criado
    min_price = 10
    max_price = 10000

    def __init__(self, stock_ref, price, color,tags):  # construtor da classe
        self.stock_ref = stock_ref
        self.__price = price
        self.color = color
        self.__stock_level = 0
        self.__StockItem_version = 1
        self.tags = tags




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
Color: {4}
tags {5}'''
        return template.format(self.stock_ref, self.item_name, 
                                self.price, self.stock_level, self.color,self.tags)

    @staticmethod  # chamado pela classe não pela instancia
    def get_tag_set_from_text(tag_text):
        """ Converte valores entrados pelo usuário em tags """   
        tag_text = str.lower(tag_text) #converte strings para minusculo
        tag_list = str.split(tag_text, sep=',') # tranforma strings em lista, usando virgula como delimitador
        tag_list = map(str.strip,tag_list) # aplica metodo str.strip p/ tirar espaços em branco dos itens da lista
        return set(tag_list) #converte a lista em sets - para não ter elementos repetidos

  