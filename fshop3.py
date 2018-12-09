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
        return 'Item de estoque' # o valor retornado será o nome do objeto da classe

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
            raise Exception('Quantidade adicionada inválida!') 
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
            raise Exception('Quantidade inválida de itens para vender!')
        if count > self.__stock_level: 
            raise Exception('Quantidade insuficiente!')
        self.__stock_level = self.__stock_level - count
        

    
    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        pass
    
         
    def __str__(self):
        """ Metodo de impressao do objeto da classe """ 
        template ='''
Referência de estoque: {0}
Tipo: {1}
preço: {2}
Quantidade em estoque: {3}
Cor: {4}'''
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
        return 'vestido' # a string retornada será o nome do objeto da classe


    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass
        
     
    def __str__(self):
        """ Metodo de impressao do objeto da classe """ 
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Padrão: {1}
Tamanho: {2}'''
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
        return 'Calça (tecido)' # a string retornada será o nome do objeto da classe
    
    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass

      
    def __str__(self): 
        """ Metodo de impressao da instancia  da classe """
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Padrão: {1}
Comprimento: {2}
Cintura: {3}
Tamanho: {4}'''
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
        return 'Calça Jeans' # a string retornada será o nome do objeto da classe
    
    def check_version(self): 
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass

    
    def __str__(self): 
        """ Metodo de impressao da instancia  da classe """  
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Estilo: {1}
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
        return 'Blusa feminina' # a string retornada será o nome do objeto da classe

    def check_version(self):
        """" classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Checando versão da superclass, alem da subclasse
        pass
    
    def __str__(self):
        """ Metodo de impressao da instancia  da classe """ 
        # Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Padrão: {1}
Estilo: {2}
Tamanho: {3}'''
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
        return 'Chapéu' # a string retornada será o nome do objeto da classe   

    def check_version(self):
        """ classe na versão 1 não precisa atualizar nada"""
        super().check_version() # Precisa checar versão da superclasse, tb alem da subclasse
        pass
    
    def __str_(self):
        """ Metodo de impressao da instancia  da classe """  
        #Exemplo de polimorfismo: Mescla atributos e métodos da super e subclasse         
        stock_details = super().__str__()  #Guarda retorno do método str da superclasse
        template ='''{0}
Tamanho: {1}'''
        # retorna o retorno do metodo str da superclasse e de atributos da subclasse
        return template.format(stock_details, self.size)













































































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
        template = '''Itens de estoque 
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
            print('Arquivo não encontrado.')  # Se não achar arquivo no disco avisa usuario
            print('Criando novo Fashion Shop.') 
            self.__shop = FashionShop() #inicia loja vazia

    def sell_stock(self):      
        """ 
        Vende uma quantidade de item do stoque. 
        Procura por um item e le numero de itens vendidos
        Não permite vender mais itens do que já existe no estoque
       
        """
        print('Vender item')

        # le entrada do usuario sobre item que quer vender
        item_stock_ref = btc.read_text('Digite referência de estoque: ')
        
        # busca entrada do usuário no dicionario com metodo find
        item = self.__shop.find_stock_item(item_stock_ref)

        # se não encontrar nada retorna None
        if item == None : 
            print('Este item de estoque não foi encontrado.')
            return

        # se encontrar item no dicionario inicia venda
        print('Venda')
        print(item)

        # se estoque for zero, retorna
        if item.stock_level == 0:
            print ('Referência de estoque não encontrada')
            return

        # se quantidade for menor que zero ou maior que maximo
        # solicita novo numero via funcao de BTC
        number_sold = btc.read_range_int(prompt='Vender item (ou zero para sair): ', 
                                min_value=0, 
                                max_value=item.stock_level) # entra quantidade a subtrair do estoque
        
        # se quantidade for zero retorna
        if number_sold == 0: 
            print('Venda cancelada.')
            return
        # se quantidade for maior que zero e menor/igual que max_value efetua venda
        item.sell_stock(number_sold)

        # informa que item foi vendido
        print('Item vendidos.')

    def create_new_stock_item(self):

        # prompt do menu mostrado para inclusão de itens
        menu = '''
        Criar novo item de estoque

        1: Vestido
        2: Calça
        3: Chapéu
        4: Blusa
        5: Jeans

        Digite a opção de item para inclusão: '''

        """ Definição das ações dos itens de menu """
        # receber entrada do usuario p/ menu de inclusao de itens
        item = btc.read_range_int(prompt=menu, min_value=1, max_value=5)

        if item == 1: 
            print('Criando vestido')
            
            # recebe entrada do usuario para item
            stock_ref = btc.read_text('Digite referência de estoque: ')
            price = btc.read_range_float(prompt = 'Digite preço: ', 
                                        min_value = StockItem.min_price, 
                                        max_value = StockItem.max_price)
            color = btc.read_text('Digite cor: ')
            pattern = btc.read_text('Digite padrão: ')
            size = btc.read_text('Digite tamanho: ')

            # cria objeto stock_item do tipo Dress
            # e usa entrada de usuaro como parametro
            stock_item = Dress(stock_ref = stock_ref, 
                            price = price,
                            color = color,
                            pattern = pattern,
                            size = size)

        elif item ==2: 
            print('Criando calça')

            # recebe entrada do usuario para item
            stock_ref = btc.read_text('Digite referência de estoque: ')
            price = btc.read_range_float(prompt = 'Digite preço: ', 
                                        min_value = StockItem.min_price,
                                        max_value = StockItem.max_price)
            color = btc.read_text('Digite cor: ')
            pattern = btc.read_text('Digite padrão: ')
            waist = btc.read_int('Digite cintura: ')
            length = btc.read_int('Digite comprimento: ')
            size = btc.read_text('Digite tamanho: ')

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
            print('Criando chapéu')

            #recebe entrada de usuario para item
            stock_ref = btc.read_text('Digite referência de estoque: ')
            price = btc.read_range_float(prompt='Digite preço: ',
                                        min_value=StockItem.min_price, 
                                        max_value=StockItem.max_price)
            color = btc.read_text('Digite cor: ')
            size = btc.read_text('Digite tamanho: ')

            # cria objeto stock_item da classe hats
            # usa entrada de usuários como parametro do objeto
            stock_item = Hats(stock_ref=stock_ref,
                            price=price,
                            color=color,
                            size=size)

        elif item == 4:
            print('Criando blusa')

            # recebe entrada de usuario para item
            stock_ref = btc.read_text('Digite referência de estoque: ')
            price = btc.read_range_float(prompt='Digite preço: ',
                                        min_value=StockItem.min_price,
                                        max_value=StockItem.max_price)
            color = btc.read_text('Digite cor: ')
            pattern = btc.read_text('Digite padrão: ')
            style = btc.read_text('Digite estilo: ')
            size = btc.read_text('Digite tamanho: ')

            # cria objeto stock item da classe blouse
            # usa entrada de usuaŕio como parametros do objeto
            stock_item = Blouses(stock_ref=stock_ref, 
                                price=price,
                                color=color,
                                pattern=pattern,
                                style=style,
                                size=size) 

        elif item == 5: 
            print('Criando Jeans')

            # recebe entrada de usuario para item
            stock_ref = btc.read_text('Digite referência de estoque: ')
            price = btc.read_range_float(prompt='Digite preço: ', 
                                        min_value=StockItem.min_price,
                                        max_value=StockItem.max_price)
            color = btc.read_text('Digite cor: ')
            pattern = btc.read_text('Digite padrão: ')
            waist = btc.read_int('Digite cintura: ')
            length = btc.read_int('Digite comprimento: ')
            style = btc.read_text('Digite estilo: ')
            size = btc.read_text('Digite tamanho: ')

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
        self.__shop.store_new_stock_item(stock_item)
        print(stock_item)


    def add_stock(self):
        print('Adicionar item')

        # le entrada do usuario sobre item que quer vender
        item_stock_ref = btc.read_text('Digite referência de estoque: ')
                
        # busca entrada do usuário no dicionario com metodo find
        item = self.__shop.find_stock_item(item_stock_ref)

        # se não encontrar nada retorna None
        if item == None : 
            print('Referência não encontrada')
            return

        # se encontrar item no dicionario inicia reposicao de estoque
        print('Adicionando quantidade ao item de estoque')
        print(item)

        # se quantidade for menor que zero ou maior que maximo
        # solicita novo numero via funcao de BTC
        number_add = btc.read_int('Adicione quantidade (ou zero para sair): ')
                
        # se quantidade for zero retorna
        if number_add == 0: 
            print('Inclusão cancelada')
            return
        # se quantidade for maior que zero e menor/igual que max_value efetua venda
        item.add_stock(number_add)

        print(item)

    def do_report(self):
        prompt ='''
1: Listar item de estoque
2: Listar todos itens de estoque

Escolha opção que quer listar: '''

        command = btc.read_range_int(prompt, min_value=1, max_value=2)
        if command == 1: 
            # le entrada do usuario sobre item que quer vender
            item_stock_ref = btc.read_text('Entre referência de estoque: ')
                
            # busca entrada do usuário no dicionario com metodo find
            item = self.__shop.find_stock_item(item_stock_ref)

            # se não encontrar nada retorna None
            if item == None : 
                print('Referência não encontrada')
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
                print('Dados da loja salvos em arquivo')
                break


ui = FashionShopShellApplication('fshop3.pickle')
ui.main_menu()

































