def add_item(inventory: list[str], item: str) -> list[str] | str:
    try:
        if type(inventory) is not list:
            return "inventory must be list"
        
        if item == "":
            return "item is empty"
        
        if item in inventory:
            return "item already exists"
        
        new_inventory = inventory + [item]
        return new_inventory
        
    except:
        return "Ошибка"
    

print(add_item(["Меч", "Щит"], "Копье"))
print(add_item(["Меч", "Щит"], "Щит"))

print(add_item(["Меч", "Щит"], ""))
