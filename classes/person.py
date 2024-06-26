class Person():
      ids = 0
      person_list = []

      def __new__(cls, *args, **kwargs) -> 'Person':
            new_person = super().__new__(cls)
            new_person.ids = cls.ids
            cls.person_list.append({
                  'id': cls.ids,
                  'name': f"{args[0]}",
                  'surname': f"{args[1]}",
            })
            cls.ids += 1
            return new_person
      
      def __del__(cls, instance):
            cls.person_list.pop(instance.ids)
            for i, person in enumerate(cls.person_list):
                  person['id'] = i
            cls.ids = len(cls.person_list)

      def __init__(self,
            name: str,
            surname: str
      ) -> None:
            self.name = name
            self.surname = surname
            self.id = Person.ids

      def get_value(self, value: str) -> str | int:
            match value:
                  case "name":
                        return self.name
                  case "surname":
                        return self.surname
                  case "id":
                        return self.ids
                  case _:
                        return "Not found"

      @classmethod
      def get_total(self) -> int:
            values = 0
            for value in self.person_list:
                  values += 1
            return values

      @classmethod
      def search(self, value: str | int) -> dict | None:
            key = "id" if isinstance(value, int) else "name"
            result = next((person for person in self.person_list if person[key] == value), None)
            if result: return f"{key} found: {result}"
            else: return f"{key} not found"

      @classmethod
      def get_values(self, type: str) -> str | None:
            return [{k: d.get(k) for k in ['id', f'{type}'] if k in d} for d in self.person_list]
      
      @classmethod
      def get_file(self) -> None:
            with open('people.txt', 'a')  as file:
                file.write('\n'.join([str(i) for i in self.person_list]))
                file.close()