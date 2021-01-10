class Weapon:
    bullets = 0

    def __init__(self, amount_of_bullets):
        Weapon.bullets = amount_of_bullets

    def shoot(self):
        if Weapon.bullets > 0:
            Weapon.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f'Remaining bullets: {Weapon.bullets}'


weapon = Weapon(0)

print(repr(weapon))
