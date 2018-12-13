from Storage import StockItem

class Dress(StockItem.StockItem ): 
    """ Subclasse de Stock Item """
    def __init__(self, stock_ref, price, color, tags, pattern, size):  # construtor da classe               
        super().__init__(stock_ref=stock_ref, price=price, color=color,tags=tags) # herança do construtor da superclasse           
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

