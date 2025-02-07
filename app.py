from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida



restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de beterraba', 13.0, 'Grande')
prato_feijoada = Prato('Pão', 2.0, 'Cacetinho de feijão')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)
# print(bebida_suco.aplicar_desconto())

def main():
    # Não chamar como restaurante_praca.exibir_cardapio() pq tem o @property e se torna somente leitura

    restaurante_praca.exibir_cardapio 

if __name__ == '__main__':
    main()
    
print(bebida_suco.aplicar_desconto())

