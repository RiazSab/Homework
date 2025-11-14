def add_item(inventory: list[str], item: str) -> list[str] | str:
    try:
        # Проверка что inventory является списком
        if type(inventory) is not list:
            return "inventory must be list"
        
        # Проверка что item не пустая строка
        if item == "":
            return "item is empty"
        
        # Проверка на существование предмета в инвентаре
        if item in inventory:
            return "item already exists"
        
        # Создаем новый список и добавляем предмет
        new_inventory = inventory + [item]
        return new_inventory
        
    except:
        return "Ошибка"
    

print(add_item(["Меч", "Щит"], "Копье"))
print(add_item(["Меч", "Щит"], "Щит"))
print(add_item(["Меч", "Щит"], ""))