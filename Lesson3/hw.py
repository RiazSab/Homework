from abc import ABC, abstractmethod
from typing import List

class User(ABC):
    
    def __init__(self, name: str, email: str) -> None:
       
        self.name = name
        self.email = email
    
    @abstractmethod
    def get_info(self) -> str:
        
        pass


class Customer(User):
   
    def __init__(self, name: str, email: str, address: str) -> None:
        
        super().__init__(name, email)
        self.address = address
        self._order_history: List[int] = []  
    
    def get_info(self) -> str:

        return f"Customer {self.name}, address: {self.address}"
    
    def place_order(self, order: 'Order') -> None:
    
        print(f"{self.name} placed an order: {order.items}")
        self._order_history.append(order.order_id)
    
    def get_order_history(self) -> List[int]:
        
        return self._order_history
    
    def get_total_orders(self) -> int:
       
        return len(self._order_history)
    
    def apply_discount_to_order(self, order: 'Order', discount_percent: float) -> None:
     
        current_price = order.get_price()
        discount_amount = current_price * (discount_percent / 100)
        new_price = current_price - discount_amount
        order.set_price(new_price)
        print(f"Discount of {discount_percent}% applied! New price: {new_price}")


class Courier(User):
    
    
    def __init__(self, name: str, email: str, vehicle: str) -> None:
       
        super().__init__(name, email)
        self.vehicle = vehicle
        self._delivered_orders_count: int = 0  
    
    def get_info(self) -> str:
        
        return f"Courier {self.name}, vehicle: {self.vehicle}"
    
    def deliver_order(self, order: 'Order') -> None:
        
        print(f"{self.name} is delivering order #{order.order_id} using {self.vehicle}")
        self._delivered_orders_count += 1
    
    def change_vehicle(self, new_vehicle: str) -> None:
       
        print(f"{self.name} changed vehicle from {self.vehicle} to {new_vehicle}")
        self.vehicle = new_vehicle
    
    
class Order:
    
    def __init__(self, order_id: int, items: List[str], price: float) -> None:
        
        self.order_id = order_id
        self.items = items
        self.__price = price  
    
    def get_total(self) -> float:
        
        return self.__price
    
    def __str__(self) -> str:
        
        return f"Order #{self.order_id}: items={self.items}, price={self.__price}"
    
    def get_price(self) -> float:
       
        return self.__price
    
    def set_price(self, new_price: float) -> None:
       
        if new_price < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = new_price
    
    def add_item(self, item: str, additional_price: float = 0) -> None:
        
        self.items.append(item)
        if additional_price > 0:
            self.__price += additional_price
        print(f"Added '{item}' to order #{self.order_id}")
    
    def remove_item(self, item: str) -> bool:
       
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from order #{self.order_id}")
            return True
        print(f"Item '{item}' not found in order #{self.order_id}")
        return False
    

def main() -> None:
   
    print("=== Информация о пользователях ===")
    customer = Customer("Alice", "alice@example.com", "Baker Street 221B")
    courier = Courier("Bob", "bob@example.com", "bike")
    print(customer.get_info())
    print(courier.get_info())
    
    print("\n=== Клиент делает заказ ===")
    order = Order(1, ["pizza", "cola"], 1200.0)
    customer.place_order(order)
    
    print("\n=== Информация о заказе ===")
    print(order)
    print(f"Order price: {order.get_price()}")
    
    print("\n=== Добавляем товар в заказ ===")
    order.add_item("dessert", 200.0)
    print(order)
    
    print("\n=== Применяем скидку 10% ===")
    customer.apply_discount_to_order(order, 10)
    print(order)
    
    print("\n=== Пробуем установить отрицательную цену ===")
    try:
        order.set_price(-100.0)
    except ValueError as e:
        print(f"Error: {e}")
    
    
    print("\n=== Курьер доставляет заказ ===")
    courier.deliver_order(order)
    
    print("\n=== Курьер меняет транспорт ===")
    courier.change_vehicle("car")
    
    print("\n=== История заказов клиента ===")
    history = customer.get_order_history()
    print(f"{customer.name}'s order history: {history}")
    print(f"Total orders: {customer.get_total_orders()}")
    
    print("\n=== Удаляем товар из заказа ===")
    order.remove_item("cola")
    print(order)


if __name__ == "__main__":
    main()