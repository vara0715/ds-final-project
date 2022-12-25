import re

def payment():
    option = int(input("\n1-UPI \n2-Debit Card \n3-Credit Card \n4-Cod(Cash On Dilivery)"))
    #  UPI method
    if option == 1:
        phone = input("Enter your 10 digit UPI number : ")
        data = re.findall(r"^[1-9]{1}[0-9]{9}$", phone)
        if data:
            print(f"Thanku Your payment has been done through {phone} \n !!! Order Placed !!!")
        else:
            print("Enter a valid UPI number")
            payment()
    #  Debit card details
    elif option == 2 :
        name = input("Enter the card holder name : ")
        print("Card Holder Name : ",name)
        if name:
            cardno = input("Enter Your 16 digit card number : ")
            data1 = re.findall(r"^[1-9]{1}[0-9]{15}$",cardno)
            if data1 :
               valid = input("Enter Expiry date and month detail : ")
               valid1 = re.findall(r"^[0-9]{4}$",valid)
               if valid1 :
                  cvv = input("Enter your cvv : ")
                  cvv1 = re.findall(r"^[0-9]{3}$",cvv)
                  if cvv1 :
                      print(f"Thanku Your payment has been done through debit card number {cardno}\n !!! Order Placed !!!")                         
                  else:    
                    print("Enter valid details")
                    payment()
               else:
                    print("Enter valid details")
                    payment()
            else:
                print("Enter valid details")
                payment()
        else:
            print("Enter valid details")
            payment()
    #  Credit Card Details
    elif option == 3:
        name = input("Enter the card holder name : ")
        print("Card Holder Name : ",name)
        if name:
            cardno = input("Enter Your 16 credit card number : ")
            data1 = re.findall(r"^[1-9]{1}[0-9]{15}$",cardno)
            if data1 :
               valid = input("Enter Expiry date and month detail : ")
               valid1 = re.findall(r"^[0-9]{4}$",valid)
               if valid1 :
                  cvv = input("Enter your cvv : ")
                  cvv1 = re.findall(r"^[0-9]{3}$",cvv)
                  if cvv1 :
                      print(f"Thanku Your payment has been done through credit card number {cardno}\n !!! Order Placed !!!")
                  else:
                      print("Enter valid details")
                      payment()
               else:
                    print("Enter valid details")
                    payment()
            else:
                print("Enter valid details")
                payment()
        else:
            print("Enter valid details")
            payment()
    # Address Details
    elif option == 4 :
        house = input("House/Flat no : ")
        street = input ("street no :")
        city = input("City name : ")
        pin = input("Enter a 6 digit Pin code : ")
        result = re.findall(r"^[1-9]{1}[0-9]{5}$", pin)
        state = input("State name : ")
        if result :
            print(f"!!! Order sucessfully Placed !!!")
            print(f"\nAddress \n{house} {street} {city} {pin} {state}")
        else:
            print("Enter valid pin code")
            payment()
    
    else:
        print("Payment declined try again ")
        payment()
