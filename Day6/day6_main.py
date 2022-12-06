distinct_characters = 14

signal = open("input.txt", "r").readline()
for index in range(0, len(signal) - distinct_characters - 1):
    marker = list(signal[index:index+distinct_characters])
    count_dict = {i: marker.count(i) for i in marker}
    if len(count_dict) == distinct_characters:
        print(f"marker end at {index+distinct_characters}")
        break
