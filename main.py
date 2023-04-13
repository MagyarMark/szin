színek = ["piros","zöld","kék","fekete"]

print(f"\nŰdv a Színözön játékban!")
print(f"A játék lényege, hogy van 4db szín amit ki kell találnod!")
print(f"\nHa eltalálsz egy színt akkor a játék ki írja azt, hogy: A(z) xy színt Megtaláltad, Gratulálok. ")
print(f"Ha pedig olyan színt írsz bele ami nincs benne akkor a ki írja azt, hogy: ílyen szín nincs benne/Bíztos színt írtál be?")
print(f"És ha mindegyik szín megvan akkor ki írja azt, hogy: Nincs több szín mindet meg találtad!")
print(f" ")

while len(színek) > 0:
  színekk = input("Adj meg egy színt (vagy 'q' kilépésez):")

  if színekk == 'q':
    break

  if színekk in színek:
    színek.remove(színekk)
    print("A(z)",színekk,"színt Megtaláltad, Gratulálok")
  else:
    print("ílyen szín nincs benne/Bíztos színt írtál be?")

if len(színek) == 0:
  print("Nincs több szín mindet meg találtad!")