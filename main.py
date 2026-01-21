from database import create_table
from services import add_customer, add_debt, get_all_customers, get_debts_by_customer

create_table()

def show_customers():
    print("\n--- Customer List ---")
    for cust in get_all_customers():
        debts = get_debts_by_customer(cust.id)
        total = sum(d.amount for d in debts)
        print(f"{cust} | Total Debt: {total}")
        if debts:
            for d in debts:
                print(f"   {d}")
        else:
            print("   No debts")

def main():
    while True:
        print("\n--- Debt System ---")
        print("1. Add Customer")
        print("2. Add Debt")
        print("3. View Customers and Debts")
        print("4. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            address = input("Address: ")
            customer = add_customer(name, phone, address)
            print(f"✅ Customer added: {customer}")
        
        elif choice == "2":
            customers = get_all_customers()
            if not customers:
                print("No customers found. Add a customer first.")
                continue
            print("Select Customer ID:")
            for cust in customers:
                print(f"{cust.id} - {cust.name}")
            try:
                customer_id = int(input("Customer ID: "))
                if customer_id not in [c.id for c in customers]:
                    print("Invalid Customer ID.")
                    continue
                amount = float(input("Amount: "))
                note = input("Note: ")
                debt = add_debt(customer_id, amount, note)
                print(f"✅ Debt added: {debt}")
            except ValueError:
                print("Invalid input.")
        
        elif choice == "3":
            show_customers()
        
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()