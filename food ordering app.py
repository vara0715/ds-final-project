#admin  Information..
pin = 3996
username = "Admin"
username1 = input("Enter the username : ")
pin1 = int(input("Enter the pin : "))
if pin1 == pin and username1 == username :

    print("\nWelcome Admin!!")
    

    class Restaurant:
    
        def __init__(self, name):
            self.restro_name=name
            self.food={}
            self.food_ID=len(self.food)+1
            self.admin_details={}
            self.user_details={}
            self.ordered_item=[]
        
        def option(self):
            print("1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item")
            while True :
                z=input()
                if z=="1":
                    self.add_food_item()
                elif z=="2":
                    self.edit_food_item()
                elif z=="3":
                    self.view_food_item()
                elif z=="4":
                    self.delete_food_item()
                elif z == 5 :
                    break
                else: 
                    print("Enter valid option")
                    break
        def add_food_item(self):
            name=input("Enter the food name : ")
            quantity=(input("Enter the quantity in values only : "))
            price=(input("Enter the price in Rs only : "))
            discount=(input("Enter the discount in Rs only : "))
            stock=(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
       
        
        
        def edit_food_item(self):
        
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
          
            
            
        def view_food_item(self):
            print("List of Food Items : \n")
            if len(self.food)!=0:    
                for i in self.food:
                    print(f"Food Id : {i}")
                    for j in self.food[i]:
                        print(j, ":", self.food[i][j])
                    print()
            else:
                print("!! Sorry No Food Items is Added !!\n")
            

        def delete_food_item(self):
        
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
      
obj = Restaurant(0)
obj.option()



#payment information....
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
  #profile updating.....
import re

def update_profile():
    option = int(input("\n1-To Update Name \n2-To Update Phone Number \n3-To Update Email ID \n4-To Update Address \n5-To Update Password \n6- Main Option"))

    if option == 1:
        name = input("\nEnter the name : ")
        print("\nUpdated Name : ",name)
    elif option == 2:
        phone = input("\nEnter your 10 digit phone number = ")
        data = re.findall(r"^[1-9]{1}[0-9]{9}$", phone)
        if data:
            print("\nUpdated Phone Number : ",phone)
        else:
            print("\nEnter Valid Phone Number")
            update_profile()
    elif option == 3:
         data = input("\nEnter your email id = ")
         result = re.findall(r"^[A-Za-z_+-.0-9]+@[A-Za-z]+\.[a-z]{1,3}$", data)    
         if result :
            print("\nUpdated Email ID : ",data)
         else:
            print("\nEnter valid Email ID")
            update_profile()
    elif option == 4:
        address = input("\nEnter your City")
        print("\nUpdated City : ",address)
    elif option == 5:
        print("\nPassword must consist of 1 capital leter,1 small letter,0-9 digit altist 1 , minimum 6 digit maximum 16 digit")
        password = input("Enter your password = ")
        result1 = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\dd!@#$%^&*()]{6,16}",password)
        if result1:
            print("!! Password Is Updated !!")
        else:
            print("Enter a valid password")
            update_profile()
    elif option ==6 :
        from _user_main import choise 
        choise()
    else:
        print("!! Enter valid option and try again !!")
        update_profile()
#new orders....
class order:
    def __init__(self,Total=0):
        self.Total = Total
        
    def Tandoori_Chicken(self,quantity_Tandoori_Chicken):
        self.quantity_Tandoori_Chicken = quantity_Tandoori_Chicken
        self.Total = self.quantity_Tandoori_Chicken * 240 + self.Total
    def Truffle_Cake(self,quantity_Truffle_Cake):
        self.quantity_Truffle_Cake = quantity_Truffle_Cake
        self.Total= self.quantity_Truffle_Cake * 900 + self.Total 
    def Vegan_Burger(self,quantity_Vegan_Burger):
        self.quantity_Vegan_Burger = quantity_Vegan_Burger
        self.Total = self.quantity_Vegan_Burger * 320 + self.Total     
    def getTotal(self):
        return self.Total


class new_order(order):
    def new_order(self):
        print("\n\nMenu")

        print("\nTandoori Chicken (4 pieces) [INR 240] \nVegan Burger (1 Piece) [INR 320] \nTruffle Cake (500gm) [INR 900]")

        while True:
            order = int(input("\n1- Tandoori Chicken 2- Vegan Burger 3- Truffle Cake \n4- Payment \n5- Main Page"))
    
            if order == 1:
                # Tanduri chicken
                quantity = int(input("Enter the quantity of Tandoori Chicken : "))
                obj.Tandoori_Chicken(quantity)
                print(f"Tanduri Chicken Quantity {quantity}")
                print(f"Payble Amount : {obj.Total}")
                data1 =(f"Tanduri Chicken {quantity} plates 280rs")
                file =  open("Order.txt","a")
                file.write(f"\nTanduri Chicken : {quantity} - 240rs plate")
                file.close()
               

            elif order == 2:
                    #  Vegam Burger
                quantity1 = int(input("Enter the quantity of Vegan Burger : "))
                obj.Vegan_Burger(quantity1)
                print(f"Vegan Burger Quantity {quantity1}")
                print(f"Payble Amount : {obj.Total}")
                dat2 =(f"\nVegan Burger {quantity1} plates 320rs")
                file =  open("Order.txt","a")
                file.write(f"\nVegan Burger : {quantity1} - 320rs plate")
                file.close()
                

    
            elif order == 3:
                   # Truffle cake
                quantity2 = int(input("Enter the quantity of Truffle Cake : "))
                obj.Truffle_Cake(quantity2)
                print(f"Truffle Cake Quantity {quantity2}")
                print(f"Payble Amount : {obj.Total}")
                data3 =(f"\nTruffle cake : {quantity2} plates 900rs")
                file =  open("Order.txt","a")
                file.write(f"\nTruffle Cake : {quantity2} - 900rs plate")
                file.close()
                
            elif order == 4:
                from _Payment import payment
                payment()

            elif order == 5:
                from _user_main import choise
                choise()
            
            else:        
                print("Not the correct option!!!!")
                break
    
        

obj = new_order()
##User Registation
import re

def registration():
        user = "Pratham"
        password2 = 1234
        option = int(input("\n1- Login \n2- Registration \n"))
        if option == 1:
            username = (input("Username : "))
            password1 = int(input("Password : "))
            if username == user and password1 ==  password2:
                print("Welcome")
            else:
                print("Invalid Username and Password")
                registration()
        elif option == 2:
            start = input("Press Enter to register")
            name = input("\nPlease Enter Your Name : ")
            phone = input(f"{name} Enter your 10 digit phone number = ")
            data = re.findall(r"^[1-9]{1}[0-9]{9}$", phone)
            if data:
                data = input(f"{name} Enter your email id = ")
                result = re.findall(r"^[A-Za-z_+-.0-9]+@[A-Za-z]+\.[a-z]{1,3}$", data)    
                if result:
                    address = input(f"{name} Enter your address : ")
                    print("Password must consist of 1 capital leter,1 small letter,0-9 digit altist 1 ,1 special character, minimum 6 digit maximum 16 digit")
                    password = input(f"{name} Enter your password = ")
                    result1 = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\dd!@#$%^&*()]{6,16}",password)
                    if result1:
                        print(f"\n {name} Welcome to the application!!!!")
                    else:
                        print("Try again and Enter a valid password")
                        registration()                        
                else:
                    print("Try again and Enter valid email id ")
                    registration()
            else:
                print("Try again and Enter valid phone number")
                registration()
        else:
            print("Try again and Enter valid option")
            registration()
       
