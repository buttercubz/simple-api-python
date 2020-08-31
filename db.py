class DB:
    def __init__(self):
        print(" * database is connected <<")
        self.items = [
            {"$_id": 0, "name": "laptop", "price": 800, "stock": 10},
            {"$_id": 1, "name": "tv", "price": 400, "stock": 5},
            {"$_id": 2, "name": "pc", "price": 1200, "stock": 25},
        ]

    def __lenDB(self):
        return len(self.items)

    def Get(self, id):
        for item in self.items:
            if item['$_id'] == id:
                return item
        return None

    def add(self, item, update=False):
        toAdd = item
        if item["$_id"] >= self.__lenDB():
            toAdd["$_id"] = self.__lenDB()
        if update:
            self.items.insert(toAdd["$_id"], toAdd)
        else:
            self.items.append(toAdd)
        return toAdd

    def get_all(self):
        return self.items

    def remove(self, id):
        item = self.Get(id)

        if item != None:
            self.items.remove(item)
            return item
        else:
            return None

    def update(self, id, data):
        for item in self.items:
            if item['$_id'] == id:
                data['$_id'] = id
                self.remove(id)
                return self.add(data, True)
            else:
                return None
