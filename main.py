import random

színek = ["piros","zöld","kék","fekete","fehér", "sárga", "narancssárga", "rózsaszín", "lila"]
random_színek = random.sample(színek, 4)

print(f"\nŰdv a Színözön játékban!")
print(f"A játék lényege, hogy van 4db szín amit ki kell találnod!")
print(f"A játékban található színek: piros, zöld, kék, fekete, fehér, sárga, narancssárga, rózsaszín és lila.")
print(f"\nHa eltalálsz egy színt akkor a játék ki írja azt, hogy: A(z) xy színt Megtaláltad, Gratulálok. ")
print(f"Ha pedig olyan színt írsz bele ami nincs benne akkor a ki írja azt, hogy: ílyen szín nincs benne/Bíztos színt írtál be?")
print(f"És ha mindegyik szín megvan akkor ki írja azt, hogy: Nincs több szín mindet meg találtad!")
print(f" ")

while len(random_színek) > 0:
  színekk = input("Adj meg egy színt (vagy 'q' kilépésez):")

  if színekk == 'q':
    break

  if színekk in random_színek:
    random_színek.remove(színekk)
    print("A(z)",színekk,"színt Megtaláltad, Gratulálok")
  else:
    print("ílyen szín nincs benne/Bíztos színt írtál be?")

if len(random_színek) == 0:
  print("Nincs több szín mindet meg találtad!")