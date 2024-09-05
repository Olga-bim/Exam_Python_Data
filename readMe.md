# Diamonds Data Analysis

## Description

This project performs data analysis on diamond data. The data is initially stored in a CSV file, which is then converted into a JSON format. The program provides various analyses including finding the highest diamond price, counting diamonds with specific cuts, and calculating the average carat weight and price for different diamond types.

## Installation

1. Ensure you have Python 3.6 or higher installed.
2. Clone this repository or download it as a ZIP file.
3. Navigate to the project directory via the command line:
   ```bash
   cd <path to the project>
4. Install any required dependencies (if applicable):

    pip install -r requirements.txt

## Usage
Ensure you have a diamonds.csv file in the project directory. This file should contain the diamond data.
Run the script:

    python app.py
    Functions
    The script includes the following functions:

max_price(diamonds): Returns the highest diamond price.
average_price(diamonds): Returns the average price of diamonds.
count_ideal_diamonds(diamonds): Returns the number of diamonds with the 'Ideal' cut.
get_unique_colors(diamonds): Returns the number of unique colors and a list of these colors.
average_carat_by_cut(diamonds, cut_type): Returns the average carat weight for diamonds of a specified cut type.
average_carat_by_all_cuts(diamonds): Returns the average carat weight for each type of cut.
average_price_by_color(diamonds): Returns the average price for each diamond color.

## Example Output
    1. Highest diamond price is: 15000.0
    2. Average price of a diamond is: 4500.0
    3. Number of Ideal diamonds: 123
    4.1 Different colors: 5
    4.2 Colors list: ['G', 'H', 'E', 'F', 'D']
    5. Average carat of Premium diamonds: 1.2
    6. Average carat for each cut type: {'Fair': 0.7, 'Good': 0.8, 'Ideal': 1.0, 'Premium': 1.2'}
    7. Average price for each color type: {'D': 10000.0, 'E': 8000.0, 'F': 6000.0, 'G': 5000.0, 'H': 4000.0}

## License
This project is licensed under the MIT License - see the LICENSE file for details.

    Feel free to adjust the descriptions and example outputs based on your actual data and results.
