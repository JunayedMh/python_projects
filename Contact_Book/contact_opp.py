class Contact:
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email
        
class ContactBook:
    def __init__(self):
        self.contact_list = []

    def find_contact(self, n):
        for contact_name in self.contact_list:
            if contact_name['name'].lower() == n.lower():
                return contact_name
            else:
                return None
    
    def valid_phone(self,phn):
        return phn.isdigit() and len(phn) == 11
    
    def valid_email(self,eml):
        return "@" in eml and "." in eml
    
    def add(self):
        name = input("Contact name: ")
        if self.find_contact(name):
            print("Contact already exist.")
        else:
            phone = input("Enter phone: ")
            if not self.valid_phone(phone):
                print("Invalid phone number")
                return
            else:
                email = input("Enter email: ")
                if not self.valid_email(email):
                    print("Invalid email.")
                    return
                else:
                    self.contact_list.append({"name":name, "phone":phone, 'email':email})
                    print(f"{name} added to the contact.")
    
    def view_all(self):
        for contact in self.contact_list:
            print(f" {contact["name"]:<10}: {contact["phone"]:}")
    
    def search(self):
        cont = self.find_contact(input("Search: "))
        print(cont if cont else "Not found")

    def delete(self):
        cont = self.find_contact(input("Delete: "))
        if cont:
            self.contact_list.remove(cont)
            print(f"{cont} deleted")
        else:
            print(f"{cont} not found.")

    
    def update(self):
        cont = self.find_contact(input("Name to update: "))
        if not cont:
            print("Not found.")
        else:
            cont_up = input("Update (name/email/phone): ").lower()
            if cont_up == "phone":
                valid = input("New phone number: ")
                if self.valid_email(valid):
                    cont["phone"] = valid
                else:
                    print("Invalid.")
            elif cont_up == "name":
                new_name = input("Enter new name: ").strip()
                if self.find_contact(new_name):
                    print("Alread Exist.")
                else:
                    cont["name"] = new_name
                    print(f"Name updated to {new_name}")
            elif cont_up == "email":
                valid = input("New email: ")
                if self.valid_email(valid):
                    cont["email"] = valid
                else:
                    print("Invalid.")
            
    def run(self):
        while True:
            print("\n1.Add 2.View 3.Search 4.Delete 5.Update 6.Exit")
            choice = input("Choose option: ")
            if choice == "1": self.add()
            elif choice == "2": self.view_all()
            elif choice == "3": self.search()
            elif choice == "4": self.delete()
            elif choice == "5": self.update()
            elif choice == "6": break
            else:
                again = input("Back to the contact book? Y/N: ")
                again = again.strip().lower()

                if again == "n":
                        break
        
ContactBook().run()
        