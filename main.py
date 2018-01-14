"""main

Main file for execution of functional programming examples
"""
from collections import namedtuple
from toolz.curried import compose, curry, filter, map, reduce

from utils.math_funcs import iseven, greater

def main():
    """Main method."""
    # create a player named tuple
    Player = namedtuple('Player', ['first', 'last', 'number', 'team', 'city'])

    # create some player named tuples
    m_j = Player(first='Michael', last='Jordan', number='23', team='Bulls', city='Chicago')
    k_b = Player(first='Kobe', last='Bryant', number='24', team='Lakers', city='Los Angeles')
    l_b = Player(first='LeBron', last='James', number='23', team='Cavaliers', city='Cleveland')
    k_p = Player(first='Kristaps', last='Porzingis', number='6', team='Knicks', city='New York')
    k_d = Player(first='Kevin', last='Durant', number='35', team='Warriors', city='Oakland')

    # store the players in tuple
    players = (m_j, k_b, l_b, k_p, k_d)

    # filter
    two_three = filter(lambda x: x.number == '23', players)
    print(tuple(two_three)) # => (Player(first='Michael', last='Jordan', number='23', team='Bulls',
                            # city='Chicago'), Player(first='LeBron', last='James', number='23',
                            # team='Cavaliers', city='Cleveland'))

    # map
    result = map(lambda x: ''.join([x.first, ' ', x.last]), players)
    print(tuple(result)) # => ('Michael Jordan', 'Kobe Bryant', 'LeBron James', 'Kristaps Porzingis', 'Kevin Durant')

    # reduce
    result = reduce(lambda x, y: x + y, [1, 2, 3], 0)
    print(result) # => 6

    # compose
    nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    c_greater = curry(greater)
    greater_zero = c_greater(y_val=0)
    result = compose(filter(greater_zero), filter(iseven))(nums)
    print(tuple(result)) # => (2, 4)

    # TODO: Add examples for groupby, drop, take, unique, curry, memoize, merge,

if __name__ == '__main__':
    main()
