gadgets= [("Explosive Batarangs", 3, True), ("Batarangs", 5, True), ("Smoke Pellets", 0, False), ("Tear Gas Grenades", 2, True), ("Night Vision Goggles", 1, True), ("Batclaw", 0 ,False), ("Grapple Gun", 3, True), ("Batsignal", 0, False), ("Utility Belt", 1, True), ("Batmobile Tires", 4,True)]

gadgets_sorted= sorted(
    gadgets,
    key=lambda item:(
        not item[2], #false comes 1st in sorting
        -item[1], #-ve cz we want descending to ascending
        item[0]) 
)

for product_name, quantity, in_stock in gadgets_sorted:
    print(f"Product: {product_name}, Quantity: {quantity}, In Stock: {in_stock}")
