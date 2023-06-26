class Item:
    def __init__(self, id, itemName, price):
        self.id = id
        self.itemName = itemName
        self.price = price


# Create bill display function
def display(lst, cName, cAddress):
    total = 0
    print("\n\n\n")
    print("\t      DYNAMIC STORES     ")
    print("\t     ------------------  ")
    print(f"Name: {cName} \t Address: {cAddress}\n")
    for obj in lst:
        print(f"Id: {obj.id}\tItem Name: {obj.itemName}\tPrice: {obj.price}")
        print("-------------------------------------------------")
        total += obj.price
    print(f"\t\tTotal: {total}")
    print("\n")
    print("\tThanks for visiting")
    print("\n\n")


# Store object array
item_list = []

print("\n\n")
print("Hello Everyone.....")
cName = input("Enter your name: ")
cAddress = input("Enter your address: ")
totalItems = int(input("Enter total items: "))
print("\n")

# Take input item details
for i in range(totalItems):
    id = i + 1
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    item_list.append(Item(id, name, price))

# Call display function
display(item_list, cName, cAddress)
