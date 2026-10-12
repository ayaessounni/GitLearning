i = 0
while i < 9:
    i += 1
    if i == 3:
        print("End the current loop.")
        continue
    if i == 5:
        print("End the current big loop.")
        break
    print(i)