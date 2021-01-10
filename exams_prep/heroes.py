def cast_spell(heroes_dict, name, mp_needed, spell_name):
    if heroes_dict[name]['MP'] >= mp_needed:
        heroes_dict[name]['MP'] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    return heroes_dict


def take_damage(heroes_dict, name, damage, attacker):
    heroes_dict[name]['HP'] -= damage
    if heroes_dict[name]['HP'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name]['HP']} HP left!")
    else:
        heroes_dict.pop(name)
        print(f"{name} has been killed by {attacker}!")
    return heroes_dict


def recharge(hero_dict, name, amount):
    if hero_dict[name]['MP']+amount <= 200:
        hero_dict[name]['MP'] += amount
        print(f"{name} recharged for {amount} MP!")
    else:
        amount = 200 - hero_dict[name]['MP']
        print(f"{name} recharged for {amount} MP!")
        hero_dict[name]['MP'] = 200
    return hero_dict


def heal(hero_dict, name, amount):
    if hero_dict[name]['HP']+amount <= 100:
        hero_dict[name]['HP'] += amount
        print(f"{name} healed for {amount} HP!")
    else:
        amount = 100 - hero_dict[name]['HP']
        print(f"{name} healed for {amount} HP!")
        hero_dict[name]['HP'] = 100
    return hero_dict


n = int(input())
heroes = {}
for _ in range(n):
    name, hit_points, mana_points = input().split()
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    heroes[name] = {'HP': hit_points, 'MP': mana_points}


commands = input()
while commands != 'End':
    commands = commands.split(' - ')
    if commands[0] == 'CastSpell':
        hero_name = commands[1]
        mp_needed = int(commands[2])
        spell_name = commands[3]
        heroes = cast_spell(heroes, hero_name, mp_needed, spell_name)
    elif commands[0] == 'TakeDamage':
        hero_name = commands[1]
        damage = int(commands[2])
        attacker = commands[3]
        heroes = take_damage(heroes, hero_name, damage, attacker)
    elif commands[0] == 'Recharge':
        hero_name = commands[1]
        amount = int(commands[2])
        heroes = recharge(heroes, hero_name, amount)
    elif commands[0] == 'Heal':
        hero_name = commands[1]
        amount = int(commands[2])
        heroes = heal(heroes, hero_name, amount)
    commands = input()

heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))
for key, value in heroes:
    print(key)
    print(f" HP: {value['HP']}")
    print(f" MP: {value['MP']}")