word = input("vnesi besedo:").lower()
if word == word[::-1]:
    print("beseda je palindrom.")
else:
    print("Beseda ni palindrom")
