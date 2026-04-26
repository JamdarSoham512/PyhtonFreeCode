# Step 1: Declare base price and age
base_price = 15
age = 21

# Step 2: Declare seat type and show time
seat_type = 'Gold'
show_time = 'Evening'

# Step 3: Check if user can book ticket
if age > 17:
    print('User is eligible to book a ticket')

# Step 4 & 5: Check eligibility for evening shows
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Step 6: Declare boolean variables
is_member = False
is_weekend = False

# Step 7: Initialize discount
discount = 0

# Step 8, 9, 10, 11: Membership discount logic
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Step 12, 13, 14: Extra charges logic
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Step 15, 16, 17: Ticket booking condition
if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
    print('Ticket booking condition satisfied')

    # Step 18, 19, 20: Service charges calculation
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print('Service charges:', service_charges)

    # Step 21: Final price calculation
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)

else:
    print('Ticket booking failed due to restrictions')