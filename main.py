# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from py_compile import _get_default_invalidation_mode


speler1 = 'Ruud Gullit'
speler2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = speler1 + ' ' + str(goal_0) + ', ' + speler2 + ' '+ str(goal_1)
print(scorers)

report = f'{speler1} scored in the {goal_0}nd minute\n{speler2} scored in the {goal_1}th minute'

print(report)

player = 'Ronald Koeman'

first_name = player[:player.find(" ")]

print(first_name)

last_name = player[player.find(" ")+1:]

last_name_len = len(last_name)

print(last_name_len)

name_short = first_name[:1]+'. '+last_name

print(name_short)

chant1 = (first_name+'! ')*len(first_name)
chant = chant1[:len(chant1)-1]

print(chant)

good_chant = chant[:-1] != ' '

print(good_chant)