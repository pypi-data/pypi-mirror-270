from hanoikovoidcdau import data
from hanoikovoidcdau.standardize import find_closest_match


input_street = "Cầu Tun"
closest_match = find_closest_match(input_street, data)
print(f"Input: {input_street}")
print(f"Closest match: {closest_match}")
