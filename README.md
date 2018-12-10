# fshop2 - Fashion Shop

Aplicação de controle de estoque para loja de roupas desenvolvida em Python 3 utilizando princípios de orientação a objeto
como herança, abstração, sobrecarga, polimorfismo.

## Funcionalidades

- Armazenar automaticamente objeto loja e itens de estoque em arquivo.
- Criar arquivo de dados e armazenar dados de nova loja, caso arquivo não exista.
- Carregar arquivo da loja com itens de estoque caso arquivo de dados exista.
- Criar itens de estoque: vestidos, calças (tecido), chapéus, Jeans, blusas.
- Adicionar (buy) quantidade aos itens de estoque. 
- Remover (sell) quantidade dos itens de estoque. 
- Define preço mínimo e máximo para itens da loja.  (atualmente (hardcoded).
- Define quantidade máxima de item em estoque (atualmente hardcoded).
- Listar 1 item de estoque.
- Listar todos itens de estoque.
- Adicionar multiplas tags (etiquetas) para localização rápida de itens de estoque
- Buscar itens de estoque por tags (uma ou mais).

### Componentes

módulo BTC com funções que permite validação de ranges, e tipos.
Fshop2 - Versão com interface de usuário em inglês US.
Fshop3 - Versão com interface de usuário em PT-BR
Fshop2.pickle: arquivo de dados da versão US.
Fshop2.pickle: arquivo de dados da versão PT-BR

### Arquitetura

#### Classe componente de usuário FashionShopShellApplication

- Cria loja (shop), carrega ou salva arquivo de loja
- Carrega menu e funções principais

#### Classe Fashionshop

- Carrega funções da loja como adicionar, procurar, vender item.

#### Classes de dados

- item de estoque(pai)
- Vestido, calça, jeans(filho de calça), blusa, chapeu

### Documentação

O código fonte está 100% comentado em PT-BR nas duas versões, para fins de estudo.