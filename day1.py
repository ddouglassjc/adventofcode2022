import os

raw_data_filename = "day1.txt"
raw_data = os.path.join(os.path.dirname(__file__), raw_data_filename)
big_chungus, current_elf = 0, 0
all_elfs = []
with open(raw_data) as file:
    for line in file:
        strip_it = line.strip()
        if strip_it.isdigit():
            current_elf += int(strip_it)
        else:
            all_elfs.append(current_elf)
            if current_elf > big_chungus: 
                big_chungus = current_elf
            current_elf = 0 
all_elfs.sort()
print(sum(all_elfs[-3:])) #part 2 answer


print(f"Big chungus is the snack plug with {big_chungus} kcals.") #part 1 answer