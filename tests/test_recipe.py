from lib.recipe import Recipe

'''
Test recipe is constructed correctly
'''
def test_recipe_constructs_correctly():
    recipe = Recipe("id", "title of recipe", 50, 5)
    assert recipe.id == "id"
    assert recipe.title == "title of recipe"
    assert recipe.average_cook_time == 50
    assert recipe.rating == 5

'''
Test that recipe is formatted to a string
'''
def test_recipe_in_string_format():
    recipe = Recipe("id", "title", "average_cook_time", "rating")
    assert str(recipe) == "Recipe(id, title, average_cook_time, rating)"

"""
Compare two recipes and ensure they're equal
"""
def test_two_recipes_are_equal():
    recipe1 = Recipe("id", "Title", "Average cook time", "Rating")
    recipe2 = Recipe("id", "Title", "Average cook time", "Rating")
    assert recipe1 == recipe2
