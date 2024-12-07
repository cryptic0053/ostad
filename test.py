def calculate_ticket_price(age, showtime):
    if age <= 0:
        return "Invalid input. Age must be a positive integer."
    
    if 0 <= age <= 10:
        price = 300
    elif 11 <= age <= 25:
        price = 500
    elif 26 <= age <= 60:
        price = 800
    else:
        price = 400
    
    try:
        hour = int(showtime[:2])
        minute = int(showtime[2:])
        if not (0 <= hour < 24 and 0 <= minute < 60):
            return "Invalid input. Please provide the showtime in the correct format."
    except:
        return "Invalid input. Please provide the showtime in the correct format."
    
    discount = 0
    if hour < 17:
        discount = 0.10 * price
    
    discounted_price = price - discount
    
    return f"Ticket price: {price} BDT\nDiscount: {discount:.2f} BDT\nDiscounted price: {discounted_price:.2f} BDT"

age = int(input("Age: "))
showtime = input("Showtime (HHMM): ")
result = calculate_ticket_price(age, showtime)
print(result)
