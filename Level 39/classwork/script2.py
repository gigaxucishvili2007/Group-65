"""2. While loop-ით გადაუყევით ლისტს რომელშიც იქნება მოთავსებული სტრინგები (ასოები), თქვენი დავალებაა, რომ ეს სტრინგები საბოლოოდ ერთი მთლიანი სტრინგის სახით გამოიტანოთ."""

full_letter = ["I" , "am" , "Giga" , "Khutsishvili"]
txt = ""
index = 0
while index < len(full_letter):
    txt += full_letter[index]
    index += 1
print(txt)