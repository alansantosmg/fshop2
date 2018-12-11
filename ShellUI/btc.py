
def read_text(prompt):
        '''
        Mostra um prompt que lê uma string de 
        texto e valida se o usuário não está
        usando sequencias de escape para abortar
        '''
        while True: 
                try:
                        result = input(prompt) 
                        break
                except KeyboardInterrupt:
                        print('Entre com o texto')
        return result




def read_int(prompt):
        ''' 
        Roda em conjunto com funçao de entrada de texto. 
        Se entrada for numero, verifica se é int
        se não for int gera excecao e solicita nova entrada
        '''

        while True:
                try:
                        entrada_numero = read_text(prompt)
                        result = int(entrada_numero)
                        break
                except ValueError:
                        print('\nEntre com valor numérico.\n')
        return result




def read_float(prompt):
        ''' 
        Roda em conjunto com funçao de entrada de texto. 
        Se entrada for numero, verifica se é float
        se não for float gera excecao e solicita nova entrada
        '''

        while True:
                try:
                        entrada_numero = read_text(prompt)
                        result = float(entrada_numero)
                        break
                except ValueError:
                        print('Entre com numero')
        return result



def read_range_int(prompt, min_value, max_value):
    '''
    Verifica se entrada de numero está dentro
    do range especificado nos parametros
    Caso não esteja, solicita nova entrada
    '''
    while True:
        entrada_range = read_int(prompt)
             
        if min_value > max_value:  #Detecta inversao de parametros
            raise Exception('Minimo é maior do maximo. Corrija')
           
        if entrada_range < min_value:
            print('Valor muito baixo.')
            continue
        elif entrada_range > max_value:
            print('Valor muito alto.')
            continue
        break  
    return entrada_range




def read_range_float(prompt, min_value, max_value):
    '''
    Verifica se entrada de numero está dentro
    do range especificado nos parametros
    Caso não esteja, solicita nova entrada
    '''
    while True:
        entrada_range = read_float(prompt)
             
        if min_value > max_value:  #Detecta inversao de parametros
            raise Exception('Minimo é maior do maximo. Corrija')
           
        if entrada_range < min_value:
            print('Valor muito baixo.')
            continue
        elif entrada_range > max_value:
            print('Valor muito alto.')
            continue
        break  
    return entrada_range








# solicita entrada string                
#seu_texto = read_text('entre com seu texto: ')


# solicita entrada de numero e usa funcao string para entrada.
#seu_numero = read_float("Entre com seu numero: ")


# solicita entrada de numero dentro de maximo e minimo
# usa funções de range como parametro
# os parametros são definidos fora da função 
#seu_numero_range = read_range('Entre com seu numero: ',min_value = 5, max_value = 1)



