import csv
import json
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Open the CSV file and convert it to JSON
with open('diamonds.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

with open('diamonds.json', 'w', encoding='utf-8') as json_file:
    json.dump(rows, json_file, ensure_ascii=False, indent=4)


# General function for reading data from a JSON file
def load_diamonds():
    with open('diamonds.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

# 1. What is the highest diamond price?
def max_price(diamonds):
    return max(float(diamond['price']) for diamond in diamonds)

# 2. What is the average price of a diamond?
def average_price(diamonds):
    return sum(float(diamond['price']) for diamond in diamonds) / len(diamonds)

# 3. How many Ideal diamonds are there?
def count_ideal_diamonds(diamonds):
    return sum(1 for diamond in diamonds if diamond['cut'] == 'Ideal')

# 4. How many different colors do diamonds have? which ones?
def get_unique_colors(diamonds):
    colors = {diamond['color'] for diamond in diamonds}
    return len(colors), list(colors)

# 5. What is the median carat of Premium type diamonds?
def average_carat_by_cut(diamonds, cut_type):
    filtered = [diamond for diamond in diamonds if diamond['cut'] == cut_type]
    if filtered:
        return sum(float(diamond['carat']) for diamond in filtered) / len(filtered)
    return 0

#  6. Create an average carat for each cut type.
def average_carat_by_all_cuts(diamonds):
    cuts = {}
    for diamond in diamonds:
        cuts.setdefault(diamond['cut'], []).append(float(diamond['carat']))

    return {cut: sum(carat_list) / len(carat_list) for cut, carat_list in cuts.items()}

# 7. Create an average price for each type of turtle
def average_price_by_color(diamonds):
    colors = {}
    for diamond in diamonds:
        colors.setdefault(diamond['color'], []).append(float(diamond['price']))

    return {color: sum(price_list) / len(price_list) for color, price_list in colors.items()}


def main():
    diamonds = load_diamonds()

    print(f"1. Highest diamond price is: {max_price(diamonds)}")
    print(f"2. Average price of a diamond is: {average_price(diamonds)}")
    print(f"3. Number of Ideal diamonds: {count_ideal_diamonds(diamonds)}")

    colors_count, colors_list = get_unique_colors(diamonds)
    print(f"4.1 Different colors: {colors_count}")
    print(f"4.2 Colors list: {colors_list}")

    print(f"5. Average carat of Premium diamonds: {average_carat_by_cut(diamonds, 'Premium')}")
    print(f"6. Average carat for each cut type: {average_carat_by_all_cuts(diamonds)}")
    print(f"7. Average price for each color type: {average_price_by_color(diamonds)}")


if __name__ == "__main__":
    main()
