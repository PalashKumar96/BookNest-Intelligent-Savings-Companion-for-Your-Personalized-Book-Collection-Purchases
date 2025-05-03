def main():
    print("Welcome to the Book Cost Calculator!")
    
    n = int(input("Enter how many different books you want to buy: "))
    total_cost = 0
    
    for i in range(1, n + 1):
        price = float(input(f"Enter the price of book {i}: "))
        quantity = int(input(f"Enter the quantity of book {i}: "))
        cost = price * quantity
        total_cost += cost
        print(f"Cost for book {i}: {cost:.2f}")
    
    print("\n----------------------------")
    print(f"Total cost for all books: {total_cost:.2f}")
    print("----------------------------")

if __name__ == "__main__":
    main()
