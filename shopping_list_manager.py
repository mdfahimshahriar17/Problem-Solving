cart = []
while True:
    
    item = input("Add your item to your card --When you are done type 'Done': ")
    
    if item.lower() == "done":
        break
    
    cart.append(item)

print("---CART ITEM---")
for i in range(0, len(cart)):

    print(f"{i+1}. {cart[i]}\n")
    