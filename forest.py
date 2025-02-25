# forest.py
import dungeoncrawler

def explore(player):
    print("Witamy w lesie!")
    print(player)
    choice = input("Czy chcesz wrócić do poprzedniej lokalizacji? (tak/t or nie/n): ").strip().lower()
    if choice in ["tak", "t"]:
        dungeoncrawler.main()
    else:
        print("Kontynuujesz eksplorację lasu.")