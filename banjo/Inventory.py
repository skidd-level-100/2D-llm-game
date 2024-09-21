#from dataclasses import dataclass
#from typing import List


##need to add a delete or flag after quantity < 1
class Food:
    def __init__(self,name,health_increase,quantity,inventory_parent=None,entity_parent=None) -> None:
        #name referered to when adding, removing, or printing this item
        self.name = name
        #property of health related effect items
        self.health_increase = health_increase
        self.quantity = quantity
        #this enables the item to directly effect the the owner of the item, also important to reassign ownership on tranfer of item to or from inventory
        self.entity_parent = entity_parent
        #a a nice looking way to access the owner's inventory. could also access through enitity parent.
        self.inventory_parent = inventory_parent
        #a tag that is used to see if you can stack this item in a inventory.
        self.is_stackable = True

    def eat(self):
        self.quantity -= 1
        self.entity_parent.health += self.health_increase
        if self.entity_parent.health > self.entity_parent.max_health:
            self.entity_parent.health = self.entity_parent.max_health
        if self.quantity <= 0:
            self.inventory_parent.remove(self)


class Inventory:
    #parent lets the inventory modify its owner.
    def __init__(self,parent=None) -> None:
        self.items = []
        self.parent = parent
    #certain items have info to access and thats how they have there effect, e.g. armor
    #when scaping armor you can keep one of its components



    #a function for adding a single item or stack of items
    def add(self,item):
        if item.name in [ii.name for ii in self.items] and item.is_stackable:
            #print("ran")
        #if you reduce the items in inventory by filtered list comprhension and change the object in list, does the item in non filtered list change as well.
            for i in self.items:
                #print(f"function inventory {i.name}")
                #print(f"{item.name} ==? {i.name} & item being added is stackable = {item.is_stackable}")
                if item.name == i.name and i.is_stackable and item.is_stackable:
                    i.quantity += item.quantity
                    #print("ran")
                    break
                    #does break stop that whole function?
                #used for if there are no matching items in inventory that are stackable
        #used for if there are no matching items in inventory that are stackable  
        else:
            #print("else2")
            item.inventory_parent = self
            item.entity_parent = self.parent
            self.items.append(item)

    def remove(self,item):
        #this will always for the first of the names items first
        #this deletes from this inventory object
        #deleting them from  the container tranfered can be done outside of this function by deep copying its contents then using remove ite items using that. or just running the clear command.
        for i in self.items:
            if i.name == item.name:
                i.quantity -= item.quantity
                if i.quantity < 1:
                    name_list = [ii.name for ii in self.items]
                    index1 = name_list.index(item.name)
                    del self.items[index1]
        
        
        
        
        
        
        
        
        

    def clear(self):
        self.items = []

    #def take items
    #its like remove items except if you dont have enough it give back a "insufient value" value


    #used to tranfer whole inventories or containers # used for when looting and other things
    def add_items(self,items:list):
        if type(items) == list:
            for item in items:
                self.add(item)
        if type(items) == Inventory:
            for item in items.items:
                self.add(item)

    #used to remove a bulk items from container from container. an example would be crafting something takes a list of items and this is how you could take those items
    def remove_items(self,items):
        if type(items) == list:
            for item in items:
                #needs to be name based like the add function
                self.remove(item)
        if type(items) == Inventory:
            for item in items.items:
                self.remove(item)


    
    def print_inventory(self):
        for i in self.items:
            print(f" - {i.name} x{i.quantity}")

#Inventory_1 = Inventory()
#Inventory_1.add(food(
#    name="burger",
#    health_increase=10,
#    quantity=5
#))
#Inventory_1.add(food(
#    name="ice cream",
#    health_increase=5,
#    quantity=1
#))
#Inventory_1.add(food(
#    name="popcorn",
#    health_increase=30,
#    quantity=2
#))

#Inventory_1.print_inventory()
#print("\n")
#Inventory_2 = Inventory()
#Inventory_2.add(food(
#    name="cheese_burger",
#    health_increase=10,
#    quantity=5
#))
#Inventory_2.add(food(
#    name="potato",
#    health_increase=5,
#    quantity=3
#))
#Inventory_2.add(food(
#    name="popcorn",
#    health_increase=30,
#    quantity=2
#))
#Inventory_2.print_inventory()
#print("\n")

#Inventory_1.add_items(Inventory_2)

#Inventory_1.print_inventory()

#Inventory_1.remove_items(Inventory_2)
#print("\n")
#Inventory_1.print_inventory()










#average 10
#change base_damage*strength

#programmable genes, what you do and focuses on grows, xp. and everyone can develope and gain ablities and just start with some.
#healer

#when calculating gained parent Xp give them the same xp as move xp increase


    #gol the entity's stats to enable easy stat changing
    #scope the variables
    #inventory.parent