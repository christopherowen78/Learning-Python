basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

print('Basket List:', basket)
print('Basket Length:', len(basket))
print('Crate List:', crate)
print('Crate Length:', len(crate))

basket.append('Damson')
print('\nAppend Damson to Basket List:', basket)
print('Basket Length:', len(basket))
print('Last Item Removed from Basket List:', basket.pop())
print('Basket List after pop():', basket)

basket.extend(crate)
print('\nExtend Basket List with Crate List:', basket)
del basket[1]
print('Item at Index 1 Removed from Basket List:', basket)
del basket[1:3]
print('Items at Index 1 to 2 Removed from Basket List:', basket)