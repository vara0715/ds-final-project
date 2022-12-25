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
