import os, json

class json_manager:
    def __init__(self, Pfad, Topic):
        self.path = Pfad
        self.topic = Topic
        self.setup()

    def open_json(self):
        with open(self.path, 'r') as file:
            self.data = json.load(file)

    def setup(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                json.dump({self.topic: {}}, file)
        else:
            with open(self.path, 'r') as file:
                self.data = json.load(file)
            if self.topic not in self.data:
                self.data[self.topic] = {}
                with open(self.path, 'w') as file:
                    json.dump(self.data, file)

    def add_element(self, first, second):
        self.open_json()
        self.data[self.topic][first] = second

        with open(self.path, 'w') as file:
            json.dump(self.data, file)

    def get_value(self, first):
        self.open_json()
        return self.data[self.topic][first]

    def get_all_keys(self):
        self.open_json()
        return list(self.data[self.topic].keys())
    def remove_element(self, element):
        self.open_json()
        if element in self.data[self.topic]:
            del self.data[self.topic][element]
            with open(self.path, 'w') as file:
                json.dump(self.data, file)

    def remove_all(self):
        self.open_json()
        self.data[self.topic] = {}
        with open(self.path, 'w') as file:
            json.dump(self.data, file)


if __name__ == '__main__':
    app = json_manager('data.json', 'Letters')
    app.add_element('1', 'A')
