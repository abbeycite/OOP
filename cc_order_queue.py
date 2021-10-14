class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops in range(1, 4):
            print("Order created!")
        elif flavor not in self.flavors:
            print("Sorry, We don't have that Flavor")
            return False
        elif scoops not in range(1, 4):
            print("Choose between 1-3 scoops")
            return False
        order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
        self.orders.enqueue(order)

'''q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() ==3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
q.show_queue()'''

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
'''shop.show_all_orders()
shop.next_order()
shop.show_all_orders()'''