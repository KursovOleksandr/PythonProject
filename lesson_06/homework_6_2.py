target_str = ""
cycle_flag = True

while cycle_flag:
    target_str = input("Введіть текст\n")
    for char in target_str:
        if char.__eq__("h"):
            cycle_flag = False
            break