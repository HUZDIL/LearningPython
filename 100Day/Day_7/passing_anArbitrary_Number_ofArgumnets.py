

def make_pizza (*toppings):# * isareti daha fazla arguman girmemize neden oluyor
   for topping in toppings:
       print(f"- {topping}")

make_pizza("mushrooms","green_peppers","extra_cheese","red_peppers")



def make_new_pizza (size,*toppings):
    print (f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_new_pizza(14,"cheese","green_cheese")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
print(user_profile)