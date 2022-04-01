# If we are purchasing products from Amazon, condition is
# if ur item price is >= 500 free shipment is available
# else u have to pay Rs.60 for delivery.

cart = [1999, 200, 500, 399, 780, 899, 499]

for i in cart:
    if i >= 500:
        print('Dear customer free shipment is available')
    else:
        print('You have to pay Rs.60 for shipment')
        
