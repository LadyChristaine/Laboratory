print("Task 1")
while True:
    phone = input("Enter your phone number: ")

    cleaned = phone.replace(" ", "").replace("-", "")
    digits = ''.join(filter(str.isdigit, cleaned))

    if len(digits) == 11:
        formatted = f"({digits[:4]}) {digits[4:7]}-{digits[7:]}"
        print("Formatted phone number:", formatted)
        break
    else:
        print("❌ Invalid phone number. Please enter 11 digits.")
print("\n")

print("Task 2")
item = "Book"
price = 15.99
quantity = 2

total = price * quantity

print(f"{quantity} x {item} @ ${price:.2f} ea. = ${total:.2f}")
print("\n")

print("Task 3")
def is_valid_username(username):
     
    return username.isalnum() and 5 <= len(username) <= 12

while True:
    user=input("Enter a username (5–12 alphanumeric characters: ")
    result=is_valid_username(user)
    print(result)
    
    if result:
        break
print("\n")

print("Task 4")
def mask_credit_card(card_number):

    digits = ''.join(filter(str.isdigit, card_number))

    masked = '*' * (len(digits) - 4) + digits[-4:]
    return masked

print(mask_credit_card("0985308016012345"))


    