from classes.person import Person
from pprint import pprint

def main() -> None:
	_luca: Person = Person("Luca", "Moroso")
	_mett: Person = Person("Mett", "Diacc")
	_mett: Person = Person("Matt", "Diacc")
	pprint(Person.person_list)
	print(Person.search(1))
	print(Person.get_total())
	pprint(Person.get_values('name'))

if __name__ == "__main__":
	main()