from classes.person import Person
import os

def clear():
      os.system('cls && pause')

def handle_input():
      while True:
            print("""
                        Insert the operation you want to perform:\n
                              1 : Add a person\n
                              2 : Remove a person\n
                              3 : Exit
                        """)
            ask = input(int())
            match int(ask):
                  case 1:
                        data = input("Insert the name and the surname of the person separated by a comma: ")
                        split_data = data.split(', ')
                        if len(split_data) == 2:
                              Person(split_data[0], split_data[1])
                              Person.get_file()
                              clear()
                        else:
                              print('Wrong format! The information must be in this way: "Name, Surname".')
                              clear()
                  case 2:
                        num = input("Insert the id of the person you want to delete: ")
                        if num > Person.get_total():
                              print("This id doesn't exist.")
                              clear()
                        elif not num.isdigit():
                              print("Wrong format! Please insert a number!")
                              clear()
                        else:
                              Person.remove_person(int(num))
                              Person.get_file()
                              clear()
                  case 3:
                        return
                  case _:
                        print("Unknown command! Try again.")
                        clear()
      Person.get_file()

if __name__ == "__main__":
      handle_input()