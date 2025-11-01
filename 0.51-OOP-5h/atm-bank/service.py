class AtmMachine:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()


    def menu(self):
        system_options = f"""
            Hi, How can i help you!!

            1. Press 1 to Create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anythings to exit
        """
        user_choice = input(system_options)

        if user_choice == '1':
            self.create_pin()

        elif user_choice == '2':
            self.change_pin()

        elif user_choice == '3':
            self.check_balance()

        elif user_choice == '4':
            self.withdraw()

        elif user_choice == '5':
            self.go_back()
        else:
            print("*"*40)
            print("You enter invalid input. Try again...")
            print("*"*40)
            self.menu()

    # -------------------------------------------------
    def create_pin(self):
        user_input = input("Enter your new pin: ")
        self.pin = user_input

        user_balance = int(input("Enter First balance..."))
        self.balance = user_balance

        print("Pin setup Successfully Done.")
        self.menu()


    # --------------------------------------------------
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        print(old_pin, self.pin)

        if old_pin == self.pin:
            new_pin = input("Enter a new pin: ")
            self.pin = new_pin
            print("New pin setup successfully Done...")
            self.menu()
        else:
            print("Your pin is not matching with old pin...")
            self.menu()

    # -----------------------------------------------------

    def check_balance(self):
        print(f"Your current balance is {self.balance}")
        self.menu()


    def withdraw(self):
        request_amount = int(input("Enter you Request Amount: "))
        if request_amount > self.balance:
            print("Salra gorib tor taka nai...")
            self.menu()
        if request_amount <= self.balance:
            self.balance -= request_amount
            print(f"Withdraw Successful and the amount is: {request_amount}")
            self.menu()

    def go_back(self):
        exit()



if __name__ =="__main__":
    my_bank = AtmMachine()