import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

class NLPModel:

    def get_model(self):
        load_dotenv()
        google_api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        return model
    

class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        first_input = """

        Hi sir, How are you!!

        1. Not a member? Register
        2. Already a member? Login
        3. Vul Kore chole aschi. Exit
    """
        
        
        user_input = input(first_input)
        if user_input == "1":
            # register
            self.__register()
        elif user_input == "2":
            # login
            self.__login()
        elif user_input == "3":
            # exit
            exit()
        else:
            print("Invalid Input")
            self.first_menu()

    def second_menu(self):
        second_menu = """
        Grate to See you!! How would you like to proceed.

        1. Sentiment Analysis
        2. Language translation
        3. Language Detection
        """
        user_input = input(second_menu)

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        else:
            print("invalid input...")
            self.second_menu()

    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            print("Email is already exits...")
        else:
            self.__database[email] = [name, password]
            print("Registrations successful. Not you can login...")
            self.first_menu()

    def __login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Success...")
                self.first_menu()
            print("Password is incorrect...")
        print("Email is not found. Register first.")
        self.first_menu()

    def __sentiment_analysis(self):
        # just write simple prompt using langchain and so on
        pass


    def __language_translations(self):
        pass


    def __language_translation(self):
        pass


    


if __name__ == "__main__":
    demo = NLPApp()
    # model = demo.get_model()
    # response = model.generate_content("Test Line")
    # print(response.text)