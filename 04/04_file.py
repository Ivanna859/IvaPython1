# 04_file.py

# Zeptáme se uživatele na hodnotu
value = input("Zadejte hodnotu, kterou chcete uložit do souboru: ")

# Otevřeme soubor 04_file.txt v režimu přidávání ('a') a zapíšeme hodnotu
with open("04_file.txt", mode="a", encoding="utf-8") as file:
    file.write(value + "\n")

print("Hodnota byla úspěšně uložena do souboru 04_file.txt.")
