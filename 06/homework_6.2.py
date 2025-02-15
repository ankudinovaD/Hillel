input_seconds = int(input('Input your seconds: '))

dict_name = {0: 'днів', 1: 'день', 2: 'дні', 3: 'дні', 4: 'дні', 5: 'днів',
             6: 'днів', 7: 'днів', 8: 'днів', 9: 'днів', 11: 'днів',
             12: 'днів', 13: 'днів', 14: 'днів'}

days, mod = divmod(input_seconds, 86400)
hours, mod = divmod(mod, 3600)
minutes, seconds = divmod(mod, 60)

day_word = ''
for key, value in dict_name.items():
    if days % 100 == key or days % 10 == key:
        day_word = value


hours, minutes, seconds = str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")
