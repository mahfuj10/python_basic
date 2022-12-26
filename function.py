def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name} !')


greet_user(first_name='Mahfujur', last_name='Rahman')


def calc_cost(total_cost, shipping, discount):
    print(f'''
    Total cost:    {total_cost}
    Shipping cost: {shipping}
    Discount:      {discount}
    ------------------
    Pay:           {round(  (discount / 100) * (total_cost + shipping))} 
    ''')


calc_cost(total_cost=90, shipping=10, discount=10)
