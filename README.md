# estrutura_de_dados_p2

Pedro Monteiro Silva - 2000328
Jhuan Gustavo Pereira Costa - 1993392
Giulio Rafael Nogueira Cruz – 1991759

Para a criação do sistema foi utilizado python, JSON e a biblioteca “os” do python.

Tema
O tema escolhido foi de um sistema de criação de personagem, no qual é possível definir um “tipo” de personagem, sendo sugerido entre herói, vilão, anti-herói, etc, cadastra um personagem a esse tipo que foi definido utilizando informações como id do personagem, o tipo (que já foi cadastrado previamente), o nome real do personagem, o codinome do personagem, poder do personagem, idade, gênero e origem do personagem. Caso durante a criação do personagem seja deixado um campo vazio ele será preenchido automaticamente como “desconhecido”.
Após a criação do personagem é possível edita-lo ou exclui-lo através do ID e mostrar todos os personagens ligados a um “tipo” e seus respectivos IDs, assim como também é possível mostrar todos os “tipos” definidos e editar e excluir eles através do nome que foi definido para cada um.
Também é possível adicionar os personagens em uma missão e apresentar todos que foram enviados para ela e também convocar de volta (retirar da missão) os personagens enviados através da ordem de adição e mostrar os últimos 5 personagens que estão participando de alguma missão. 

Listas (filas e pilhas)
No sistema as filas e pilhas foi utilizada para gerenciar os personagens que foram enviados em uma missão garantindo que sejam chamados de volta na mesma ordem em que foram recrutados. Esse contexto no qual usamos foi o que consideramos que poderia ser melhor utilizado
No sistema a fila foi utilizada para fazer o gerenciamento de personagens para ser enviados para a missão e depois para serem convocados de volta na ordem FIFO (First-In, First-Out). Já a pilha foi utilizada para armazenar os últimos personagens cadastrados, usando LIFO (Last-In, First-Out) permitindo acessar os personagens mais recentemente adicionados que no caso também preferimos que fosse apresentado 5 de cada vez, deixando a lista mais fácil de acompanhar e visualizar deixando organizado também. As pilhas e filhas foram adicionadas nesta parte em específico porque foi o contexto em que melhor se encaixava.

Tuplas
O uso das tuplas foi utilizado na criação da função “info_personagem_id()”, onde ela foi escolhida para que os dados não pudessem ser alterados, pois essas informações devem ser imutáveis quando criadas para somente depois caso necessários fossem alteradas através de uma função específica para isso, além de que essas informações só seriam utilizadas para visualização do usuário do sistema. Com as tuplas armazenando os dados com pares de chave e valor a visualização dessas informações ficaria apresentada da forma que seria de fácil visualização.

Dicionário
O uso de dicionários foi usado bastante no código para criar e buscar as informações de “tipos” já que este campo pode ser variado e ter várias adições e alterações (criação de tipo, de personagem, etc). No inicio do código ele é declarado como vazio justamente por poder ter adições feitas pelo usuário desde o início. Quando um novo tipo de personagem é cadastrado e na exclusão dele também é utilizado o dicionário. Também foi utilizado para armazenar e editar dados dos personagens e exibir as informações dele.

Listas encadeadas 
As listas encadeadas foram usadas na estrutura pela classe “PersonagemNode” e da variável “personagem_head”, que serve como ponto de inicial da lista através e através do atributo “next” ele aponta para o próximo nó (personagem). A lista encadeada é usada para armazenar os personagens no programa, onde cada nó contem os dados de um personagem. Usamos a lista encadeada neste momento pois achamos que era onde ela melhor se encaixava no contexto do sistema, acaba sendo mais prático que uma lista normal para o controle dos dados, seja para inserir ou remover os personagens já que são informações que podem ser bastante alteradas, não precisando ser reorganizada como em uma lista comum. Para exibir o personagem por ID o código percorre a lista encadeada verificando os Ids até encontrar o nó informado (personagem) e o mesmo vale para a exclusão do personagem.

Sets
Usamos os sets para evitar duplicidade de informações como em “tipos” ou em Ids, para que eles sejam únicos deixando com melhor performance para operações usadas no contexto do nosso sistema 

