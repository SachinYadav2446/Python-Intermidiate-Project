contact_list=[]


while True:
    print("Contact book Menu")
    print("1) Add Contact")
    print("2) View Contact")
    print("3) Search Contact")
    print("4) Update Contact")
    print("5) Delete Contact")
    print("6) Exit")

    user_choice=int(input("Choose your operation from Contact Book : "))

    if user_choice==1:
        contact_name=input("Enter Name of Contact : ")
        contact_phone=int(input("Enter Phone number of Contact : "))
        contact_email=input("Enter Email of Contact : ")
        contact_details={
            'name':contact_name,
            'phone':contact_phone,
            'email':contact_email
        }
        contact_list.append(contact_details)

    elif user_choice==2:
        if len(contact_list)>0:
            for index,contact in enumerate(contact_list,start=1):
                print(f"{index}:{contact['name']}-{contact['phone']}-{contact['email']}")
        else:
            print("Contact List is empty . Add some contacts first")     

    elif user_choice==3:
        print("Search Methods")
        print("1) By Name")
        print("2) By Phone Number")
        print("3) By Email")

        user_choice_search_method=int(input("Choose Method to Search your contact : "))

        found=False

        if user_choice_search_method==1:
            user_search_name=input("Enter Name of Contact to search : ")

            for index,contact in enumerate(contact_list,start=1):
                if user_search_name==contact['name']:
                    print(f"{index}:{contact['name']}-{contact['phone']}-{contact['email']}")
                    found=True
                    break

            if found==False:
                print("Contact with this name does not exist")


        elif user_choice_search_method==2:
            user_search_phone=int(input("Enter phone number of contact to search : "))

            for index,contact in enumerate(contact_list,start=1):
                if user_search_phone==contact['phone']:
                    print(f"{index}:{contact['name']}-{contact['phone']}-{contact['email']}")
                    found=True
                    break

            if found==False:
                print("Contact with this phone number does not exist")


        elif user_choice_search_method==3:
            user_search_email=input("Enter email of contact to search : ")

            for index,contact in enumerate(contact_list,start=1):
                if user_search_email==contact['email']:
                    print(f"{index}:{contact['name']}-{contact['phone']}-{contact['email']}")
                    found=True
                    break

            if found==False:
                print("Contact with this email does not exist")

        else:
            print("Choose option again")


    elif user_choice==4:

        if len(contact_list)>0:

            print("Update menu of Contact list is below")

            for index,contact in enumerate(contact_list,start=1):
                print(f"{index}:{contact['name']}-{contact['phone']}-{contact['email']}")

            contact_update_number=int(input("Enter which contact to update : "))

            if 1<=contact_update_number<=len(contact_list):

                print("1) Name of Contact")
                print("2) Phone number of Contact")
                print("3) Email of Contact")

                user_choice_update=int(input("Choose to update : "))

                if user_choice_update==1:
                    updated_name=input("Update name : ")
                    contact_list[contact_update_number-1]['name']=updated_name
                    print("Contact updated successfully")

                elif user_choice_update==2:
                    updated_number=int(input("Update number : "))
                    contact_list[contact_update_number-1]['phone']=updated_number
                    print("Contact updated successfully")

                elif user_choice_update==3:
                    updated_email=input("Update email : ")
                    contact_list[contact_update_number-1]['email']=updated_email
                    print("Contact updated successfully")

                else:
                    print("Choose option again")

            else:
                print("Invalid contact number")

        else:
            print("Contact List is empty . Add some contacts first")


    elif user_choice==5:

        if len(contact_list)==0:
            print("Contact List is empty . Add some contacts first")

        else:

            print("Choose Way to delete : ")
            print("1) By Entering Name")
            print("2) By Entering Phone number")
            print("3) By Entering Email")

            user_delete_choice=int(input("Enter Way to delete : "))
            found=False

            if user_delete_choice==1:
                user_delete_name=input("Enter name to delete contact : ")

                for index,contact in enumerate(contact_list):
                    if contact['name']==user_delete_name:
                        contact_list.pop(index)
                        found=True
                        print("Contact deleted successfully")
                        break


            elif user_delete_choice==2:
                user_delete_phone=int(input("Enter phone number to delete contact : "))

                for index,contact in enumerate(contact_list):
                    if contact['phone']==user_delete_phone:
                        contact_list.pop(index)
                        found=True
                        print("Contact deleted successfully")
                        break


            elif user_delete_choice==3:
                user_delete_email=input("Enter email to delete contact : ")

                for index,contact in enumerate(contact_list):
                    if contact['email']==user_delete_email:
                        contact_list.pop(index)
                        found=True
                        print("Contact deleted successfully")
                        break


            else:
                print("Choose option again")

            if found==False:
                print("Contact not found.")


    elif user_choice==6:
        user_exit_choice=input("Are you sure you wanna exit (Y/N): ")

        if user_exit_choice=='Y':
            print("Exited Program")
            break  

        else:
            print("Not Exited Program")

    else:
        print("Choose option among menu of Contact List")