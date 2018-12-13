""" 
Fashion Shop APP
@Author:  Alan Santos
Actual release: dec-7-2018

Aplicação comentada para propósito de estudos

"""

# importação de dependencias externas
from ShellUI import btc  # biblioteca de entrada e validação de tipos
import pickle # biblioteca de armazenamento de arquivos binários
from Storage import StockItem, Dress, Pants, Jeans, Blouses, Hats 




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



    def find_matching_with_tags(self, search_tags): 
        """ Retorna item de estoque que contem tags procuradas (subset of tag_list) """

        def match_tags(item):
            """ Retorna  as tags do item contem as tags procuradas  """
            # compara tags fornecidas pelo usuário com tags do item
            return search_tags.issubset(item.tags)

        # retorna a filtragem do que foi encontrado por match_tags dentro do dicionario
        return filter(match_tags,self.__stock_dictionary.values())



    def __str__(self): 
        """ Lista items da loja """
        stock = map(str, self.__stock_dictionary.values()) # mapeia valores de string do dicionario
        stock_list = '\n'.join(stock) #imprime fila de valores mapeados 1 por linha
        template = '''Itens in Stock 
{0}
''' 
        return template.format(stock_list)  #formata e retorna lista de items do dicionário








