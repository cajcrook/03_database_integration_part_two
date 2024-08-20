from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["title"], row["average_cook_time"], row["rating"])
            recipes.append(item)
        return recipes
    
    def find(self, rating):
        rows = self._connection.execute('SELECT * FROM recipes WHERE rating = %s', [rating])
        row = rows[0]
        return Recipe(row["id"], row["title"], row["average_cook_time"], row["rating"])