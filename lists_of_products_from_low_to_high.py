products = [
    {"id": 101, "name": "Laptop", "price": 55000},
    {"id": 102, "name": "Mobile", "price": 18000},
    {"id": 103, "name": "Headphones", "price": 2500}
]
def sort_by_price(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and products[j]["price"] > key["price"]:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return products
if __name__ == "__main__":  
    sorted_products = sort_by_price(products)
    for product in sorted_products:
        print(f'ID: {product["id"]}, Name: {product["name"]}, Price: {product["price"]}')