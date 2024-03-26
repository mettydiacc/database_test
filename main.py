from functions.input import handle_input
from classes.person import Person

def load_people():
	with open('people.txt', 'r') as file:
		values = file.readline().strip().split(",")
		data = {"id": values[0], "name": values[1], "surname": values[2]}
		Person.person_list.append(data)

def main() -> None:
	load_people()
	handle_input()
	

if __name__ == "__main__":
	main()