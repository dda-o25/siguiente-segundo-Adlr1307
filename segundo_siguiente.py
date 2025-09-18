h = int(input("Pon las horas (0-23): "))
m = int(input("Pon los minutos: "))
s = int(input("Pon los segundos (puedes dejarlo en 0): "))
s = s+1
    


if s >= 60:
    s = 0
    m += 1


if m >= 60 :
    m = 0
    h += 1

if h > 23:
    h = 0

print(f"\rSon las {h:02d}:{m:02d}:{s:02d}", end="", flush=True)
print()
