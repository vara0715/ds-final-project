pin = 965645
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
