from Storage import StockItem

class Hats(StockItem.StockItem ): # subclasse de stockitem
    def __init__(self, stock_ref, price, color, tags, size):  # construtor       
        super().__init__(stock_ref=stock_ref, price=price, color=color,tags=tags) # herda construtor de StockItem
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

