class Recipe():
    def __init__(self, id, title, average_cook_time, rating):
        self.id = id
        self.title = title
        self.average_cook_time = average_cook_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.title}, {self.average_cook_time}, {self.rating})"