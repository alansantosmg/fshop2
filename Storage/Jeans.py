from Storage import Pants
class Jeans(Pants.Pants):
    """ Subclasse de StockItem """
    def __init__(self, stock_ref, price, color, tags, pattern, length, size, waist, style):
        super().__init__(stock_ref=stock_ref,
                        price=price,
                        color=color,
                        tags=tags,
                        pattern=pattern,
                        length=length,
                        size=size,
                        waist=waist) # heranca do contrutor da superclase 
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

