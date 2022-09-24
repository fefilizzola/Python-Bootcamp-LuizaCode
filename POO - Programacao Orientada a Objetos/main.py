from cart_class import cart

qtd = int(input("Insira a quantidade de itens do carrinho:"))
id_user = input("Insira o id do usuário:")

# Adicionar itens no carrinho
count = 0
while count < qtd:
    id_product = input("Insira o id do produto:")
    price_product = float(input("Insira o preço do produto:"))
    quantity_product = int(input("Insira a quantidade de produto:"))
    cart.add_item_cart(id_product, id_user, price_product, quantity_product)
    count += 1
    
print("Itens no carrinho:", cart.carts)

# Pegar o item pelo id_produto filtrado
id_product_filter = input("Insira o id do produto que você deseja filtrar:")
item = cart.get_item_cart_by_product(id_product_filter)
print('Item filtrado', item)

# Remover o item pelo id_produto
id_product_remove = input("Insira o id do produto que você deseja remover do carrinho:")
item = cart.remove_item_id_product(id_product_remove)
print("Resultado do carrinho com o item removido:", cart.carts)

#calcular o total do carrinho
sum=0
for c in cart.carts:
    sum+=c[2]*c[3]
print(f"O valor total do carrinho é R$", "{:.2f}".format(sum))