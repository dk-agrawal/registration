class Registration:
    def __init__(self):
        self.user_name = ""
        self.pswd = ""
        self.f_name = ""
        self.m_name = ""
        self.l_name = ""
        self.father_name = ""
        self.age = 0
        self.gender = ""
        self.mobile_no = ""
        self.f_contact = ""
        self.address = ""
        self.nation = ""
        self.pincode = ""
        self.city = ""
        self.state = ""
        self.logged_in = False

    def register(self):
        self.f_name = input("Enter First name : ")
        self.m_name = input("Enter Middle name : ")
        self.l_name = input("Enter Last name : ")
        self.father_name = input("Enter your father's name : ")
        self.age = int(input("Enter your age : "))
        self.gender = input("Select your gender M/F : ")
        self.mobile_no = input("Enter contact number : ")
        self.f_contact = input("Enter Father's contact no. : ")
        self.address = input("Enter your permanent address : ")
        self.nation = input("Enter nationality : ")
        self.pincode = input("Enter your pincode : ")
        self.city = input("Enter your city : ")
        self.state = input("Enter your state : ")
        self.user_name = input("Enter username: ")
        pswd = input("Enter your password : ")
        cnf_pswd = input("Re-enter your password : ")
        if pswd == cnf_pswd:
            self.pswd = pswd
            print("Registration Successful")
        else:
            print("Password Mismatch")

    def login(self):
        u_name = input("Enter username : ")
        if u_name == self.user_name:
            pwd = input("Enter your password : ")
            if pwd == self.pswd:
                print("Login Successful..")
                self.logged_in = True
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")

    def show_profile(self):
        if self.logged_in:
            print(f"First name :\t{self.f_name}")
            print(f"Middle name :\t{self.m_name}")
            print(f"Last name :\t{self.l_name}")
            print(f"Father name :\t{self.father_name}")
            print(f"Age :\t{self.age}")
            print(f"Gender :\t{self.gender}")
            print(f"Contact Number :\t{self.mobile_no}")
            print(f"Father's Contact number :\t{self.f_contact}")
            print(f"Address :\t{self.address}")
            print(f"Nationality :\t{self.nation}")
            print(f"Pin-Code :\t{self.pincode}")
            print(f"City :\t{self.city}")
            print(f"State :\t{self.state}")
        else:
            print("Please login first to view profile")

    def update_profile(self):
        if self.logged_in:
            self.father_name = input("Enter your father's name : ")
            self.mobile_no = input("Enter contact number : ")
            print("Profile updated successfully")
        else:
            print("Please login first to update profile")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logged Out Successfully")
        else:
            print("You are not logged in")

    def sessionterminate(self):
        print("Thank You !!!")
        exit()


def main():
    reg = Registration()
    print("Welcome To Shree Shyam Commerce Point")

    while True:
        reply = input('''
Choose option:
    1. Registration
    2. Login
    3. Show Profile
    4. Update Profile
    5. Logout
    6. Session Terminate

Choose the option (1/2/3/4/5/6): ''').strip()

        if reply == '1':
            reg.register()
        elif reply == '2':
            reg.login()
        elif reply == '3':
            reg.show_profile()
        elif reply == '4':
            reg.update_profile()
        elif reply == '5':
            reg.logout()
        elif reply == '6':
            reg.sessionterminate()
        else:
            print("Please enter correct input!!")


if __name__ == "__main__":
    main()