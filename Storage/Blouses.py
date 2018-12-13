
from Storage import StockItem

class Blouses(StockItem.StockItem):
    def __init__(self, stock_ref, price, color, tags, size, pattern, style):
        super().__init__(stock_ref=stock_ref, price=price, color=color, tags=tags)
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

if __name__=='__main__': 
    pass