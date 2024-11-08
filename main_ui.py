from products import Products
from store import Store
from user_interface import start

def main():

    macbook_air_m2 = Products("MacBook Air M2", price=1450, quantity=100)
    bose_quietcomfort_earbuds = Products("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel_7 = Products("Google Pixel 7", price=500, quantity=250)
    
    # Set up initial stock of inventory
    product_list = [
        Products("MackBook Air M2", price=1450, quantity=100),
        Products("Bose QuietComfort Earbuds", price=250, quantity=500),
        Products("Google Pixel 7", price=500, quantity=250)                 
    ]


    best_buy = Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()
