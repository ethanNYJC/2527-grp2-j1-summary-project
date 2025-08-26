class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_item(self, item):
        newNode = Node(item)
        if self.count >= 4:
            self.show_inventory()
            choice = input("Your inventory is full. Would you like to remove some items? (y/n)").lower()
                           
            if choice == "n":
                return
            elif choice == "y":
                removed_item = input("Which item would you like to remove?")

                if not self.sell_item(removed_item):
                    print(f'{removed_item} was not added to inventory.')
                    return
                else:

        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = newNode
        
        self.count += 1
        print(f'{item.name} has been added to inventory.')


    def sell_item(self, item):
        
        while True:
            current = self.head
            prev = None

            while current:
                if current.item == item:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    
                    self.count -= 1
                    print(f'{item.name} sold for {item.value} and removed from inventory.')
                    return True
            
                
