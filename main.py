# data types for restaurant
from pyscript import display, document

# variables
product_names = ['Bean Sprouts',  'Noodles', 'Mango Shake', 'Fried Rice', 'Tokwa'] #list with an extra two products
menu_prices = {'Bean Sprouts': 120.50, 'Noodles': 145.20, 'Mango Shake': 99.99, 'Fried Rice': 130.75, 'Tokwa': 30.2} #dict
tax_rate = 0.20 #float

# Equation with Tax
bean_sprouts_with_tax = menu_prices['Bean Sprouts'] * (1 + tax_rate)
noodles_with_tax = menu_prices['Noodles'] * (1 + tax_rate)
mango_shake_with_tax = menu_prices['Mango Shake'] * (1 + tax_rate)
fried_rice_with_tax = menu_prices['Fried Rice'] * (1 + tax_rate)
tokwa_with_tax = menu_prices['Tokwa'] * (1 + tax_rate)

# Order Form
def orderform(e): #creating calculating functions in python
    document.getElementById("receipts").innerHTML = "" #clearing the output field
    document.getElementById("total_amount").innerHTML = "" #clearing the output field

    Mango_Shake_qty = float(document.getElementById("mango_shake_qty").value or 0) #getting value from an input field
    Noodles_qty = float(document.getElementById("noodles_qty").value or 0)
    Fried_Rice_qty = float(document.getElementById("fried_rice_qty").value or 0)
    Tokwa_qty = float(document.getElementById("tokwa_qty").value or 0)
    Bean_Sprouts_qty = float(document.getElementById("bean_sprouts_qty").value or 0)
    Address = document.getElementById("address").value.strip()
    Contact_Number = document.getElementById("phone").value.strip()
    Name = document.getElementById("name").value.strip()
    Email = document.getElementById("email").value.strip()

    # CalculatingTotal
    total = (float(Mango_Shake_qty) * mango_shake_with_tax) + (float(Noodles_qty) * noodles_with_tax) + (float(Fried_Rice_qty) * fried_rice_with_tax) + (float(Tokwa_qty) * tokwa_with_tax) + (float(Bean_Sprouts_qty) * bean_sprouts_with_tax)

    # Validating if they completed the input field
    if not Name or not Email or not Contact_Number or not Address:
        display("Please fill out personal details before checkout", target="receipts")
        return
    
    if (Mango_Shake_qty + Noodles_qty + Fried_Rice_qty + Tokwa_qty + Bean_Sprouts_qty) == 0:
        display("Order is invalid without item purchased.", target="receipts")
        return

    # Displays
    display(
        f"Hello, {Name}! Thank you for ordering! " 
        f"Your order will be delivered to {Address}, and "
        f"your receipt will be sent to {Contact_Number} and {Email}.",
        target="receipts"
    ) 

    display(
        f" Your Total Cost is:  {round(total, 2)} PHP",
        target="total_amount"
    )