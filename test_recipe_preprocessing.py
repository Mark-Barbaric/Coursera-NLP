
import recipe_preprocessing

def test_recipe_preprocessing():
    test_recipe = [
        '1 x 1kg chicken',
        'couple cloves of garlic',
        '2tsp salt',
        '2tsp pepper',
        '1 onion',
        'pinch of basil',
        '300g carrots',
        '1 x chicken stock cube'
    ]

    output = ['chicken',
    'garlic', 'salt', 'pepper', 'onion', 'basil', 'carrots', 'chicken stock']