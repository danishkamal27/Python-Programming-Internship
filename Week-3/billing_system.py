"""
Mini Project (W3): OOP-Based Billing System
Demonstrates object interactions, calculations, data formatting,
and tabular presentation in Python.
"""


class Product:
    """Class representing an individual item or product in a bill."""

    def __init__(self, name, price, quantity=1):
        """Initialize product details with name, price, and quantity."""
        self.name = str(name).strip()
        self.price = float(price) if price >= 0 else 0.0
        self.quantity = int(quantity) if quantity > 0 else 1

    def get_total(self):
        """Calculate total price for this product item (price * quantity)."""
        return self.price * self.quantity


class Bill:
    """Class representing a customer's bill, managing items, taxes, and total calculation."""

    def __init__(self, customer_name="Valued Customer", tax_rate=5.0):
        """Initialize bill with customer name and tax percentage rate."""
        self.customer_name = customer_name
        self.tax_rate = float(tax_rate) if tax_rate >= 0 else 0.0
        self.items = []

    def add_product(self, product):
        """Add a Product object to the bill."""
        if isinstance(product, Product):
            self.items.append(product)
            print(f"[ADDED] Added '{product.name}' (Qty: {product.quantity}, Price: ${product.price:.2f}) to bill.")
            return True
        print("[FAILED] Error: Invalid product object provided.")
        return False

    def add_item(self, name, price, quantity=1):
        """Helper method to create and add a product directly by attributes."""
        product = Product(name, price, quantity)
        return self.add_product(product)

    def calculate_subtotal(self):
        """Calculate subtotal before tax."""
        return sum(item.get_total() for item in self.items)

    def calculate_tax(self):
        """Calculate tax amount based on subtotal and tax rate percentage."""
        return self.calculate_subtotal() * (self.tax_rate / 100.0)

    def calculate_total(self):
        """Calculate grand total (subtotal + tax)."""
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        """Display the final bill in a clean, formatted ASCII table."""
        subtotal = self.calculate_subtotal()
        tax_amount = self.calculate_tax()
        grand_total = self.calculate_total()

        print("\n" + "=" * 62)
        print(f"{'INVOICE / RECEIPT':^62}")
        print("=" * 62)
        print(f" Customer Name : {self.customer_name}")
        print(f" Tax Rate      : {self.tax_rate:.1f}%")
        print("-" * 62)

        # Table Header
        print(f" {'#':<3} | {'Product Name':<25} | {'Price':<9} | {'Qty':<4} | {'Total':<10}")
        print("-" * 62)

        # Table Rows
        if not self.items:
            print(f" {'No items added to bill.':^60}")
        else:
            for idx, item in enumerate(self.items, 1):
                print(
                    f" {idx:<3} | {item.name:<25} | ${item.price:>8.2f} | {item.quantity:>4} | ${item.get_total():>9.2f}"
                )

        print("-" * 62)
        # Summary Rows
        print(f" {'Subtotal':>47} : ${subtotal:>9.2f}")
        print(f" {'Tax (' + str(self.tax_rate) + '%)':>47} : ${tax_amount:>9.2f}")
        print("=" * 62)
        print(f" {'GRAND TOTAL':>47} : ${grand_total:>9.2f}")
        print("=" * 62)
        print(f"{'Thank you for your business!':^62}\n")


def demonstrate_billing_system():
    """Demonstrate Billing System workflow with products and tabular invoice generation."""
    print("=========================================")
    print("  DEMONSTRATING OOP BILLING SYSTEM       ")
    print("=========================================\n")

    # Create a new Bill instance
    bill = Bill(customer_name="John Doe", tax_rate=8.5)

    # Create Product objects
    p1 = Product("Wireless Mouse", price=25.99, quantity=2)
    p2 = Product("Mechanical Keyboard", price=79.50, quantity=1)
    p3 = Product("USB-C Hub / Adapter", price=19.99, quantity=3)

    # Add products to bill
    bill.add_product(p1)
    bill.add_product(p2)
    bill.add_product(p3)

    # Can also add directly using add_item convenience method
    bill.add_item("HDMI Cable (6ft)", price=9.99, quantity=2)

    # Display final bill in tabular format
    bill.display_bill()


if __name__ == "__main__":
    demonstrate_billing_system()
