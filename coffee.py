""" Instructions for coffee machine
    1. Make and serve me, you and Gibbs a cup of coffee (add coffee, add hot water, stir)
    2. Change how the mix is stirred
    3. A better way to make coffee with less repitition
    4. Make you coffee with milk and sugar (add sugar, add milk)
    5. Make Gibbs coffee with milk, sugar and something else (add sugar, add milk, ...)
    6. Refactor
"""

def make_coffee(*options):
    """ Makes coffee 
        Args:
            options: 0 or more extra ingredients
    """

    # Get ingredients
    ingredients = ['coffee', 'hot water']
    if options:
        for option in options:
            ingredients.append(option)

    # Do the steps    
    print('Started making coffee...\nGetting cup')
    print('Adding {}'.format(', '.join(ingredients)))
    print('Stir the mix for 5 seconds\nFinished making coffee...')

    if options:
        coffee = 'Tasty coffee with {}'.format(', '.join(options))
    else:
        coffee = 'Tasty coffee'

    return coffee
    


def serve_coffee(coffee, person):
    """ Serves coffee to a specified person """
    print("---Here's your {} {}, Enjoy!! ---\n".format(coffee, person))

# Make my coffee
my_coffee = make_coffee()
serve_coffee(my_coffee, 'Evans')


# Make Gibbs' coffee
gibbs_coffee = make_coffee('sugar', 'milk', 'cream')
serve_coffee(gibbs_coffee, 'Gibbs')


# Make Janet's coffee
janet_coffee = make_coffee('milk', 'sugar')
serve_coffee(janet_coffee, 'Janet')