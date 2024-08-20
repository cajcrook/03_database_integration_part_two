from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository #all, a list of all recipes is returned
"""
def test_all_recipes_are_returned(db_connection):
    db_connection.seed("seeds/recipe_directory_table.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.all()
    assert recipe == [
        Recipe(1, "Pizza", 10, 5),
        Recipe(2, "Pasta", 8, 4),
        Recipe(3, "Fajitas", 20, 3),
        Recipe(4, "Broth", 60, 1),
        Recipe(5, "Sausage Sandwich", 15, 2)
        ]

"""
When we call RecipeRepository #find, we recice a single recipe based on our search criteria(rating)
"""
def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipe_directory_table.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(3)
    assert recipe == Recipe(3, "Fajitas", 20, 3)

