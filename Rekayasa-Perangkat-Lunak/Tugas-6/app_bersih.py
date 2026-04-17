# app_bersih.py

class FruitInventory:
    def __init__(self):
        # SOLUSI 1 & 2: Encapsulation & Meaningful Names
        # Data dibungkus dalam class, tidak lagi global. Nama variabel deskriptif.
        self.fruits = []

    def add_fruit(self, name, price, stock):
        # SOLUSI 3: No Redundant Comments
        # Nama parameter sudah jelas (name, price, stock), tidak butuh komentar penjelasan.
        fruit = {
            "name": name, 
            "price": price, 
            "stock": stock
        }
        self.fruits.append(fruit)

    def calculate_total_asset_value(self, fruit):
        # SOLUSI 5 (Part 1): Single Responsibility Principle
        # Fungsi ini KHUSUS hanya untuk menghitung, tidak mencetak apa-apa.
        return fruit["price"] * fruit["stock"]

def display_inventory_report(inventory):
    # SOLUSI 5 (Part 2): Single Responsibility Principle
    # Fungsi ini KHUSUS hanya untuk menampilkan laporan.
    print("=== LAPORAN STOK BUAH ===")
    for fruit in inventory.fruits:
        total_value = inventory.calculate_total_asset_value(fruit)
        # SOLUSI 4: F-Strings & Formatting
        # Lebih rapi, aman, dan mudah diatur tata letaknya (alignment :<10).
        print(f"Buah: {fruit['name']:<10} | Nilai Aset: Rp{total_value:,}")

def main():
    inventory = FruitInventory()
    inventory.add_fruit("Apel", 5000, 10)
    inventory.add_fruit("Mangga", 8000, 5)
    display_inventory_report(inventory)

if __name__ == "__main__":
    main()