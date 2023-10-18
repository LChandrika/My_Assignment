class Big_basket:
    def items(self):
        print("Big basket")

class item_1(Big_basket):
    def display_1(self):
        print("Furits : Apple,Banana")

class item_2(Big_basket):
    def display_2(self):
        print("Chocholets : Dairy Milk , kitkat")

b=item_1()
b.items()
b.display_1()
b1=item_2()
b1.display_2()
