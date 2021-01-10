number_of_snowballs = int(input())
max_snowball = 0
for snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_snow / snowball_time) ** snowball_quality
    if max_snowball < result:
        max_snowball = result
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
print(f'{max_snowball_snow} : {max_snowball_time} = {max_snowball:.0f} ({max_snowball_quality})')



