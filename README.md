# 📊 Demographic Data Analyzer

A Python data analysis project that extracts insights from the 1994 Census database. It calculates key demographic metrics such as average ages, education distribution, salary correlations, and top-earning statistics across different countries and occupations.

This project is part of the **Data Analysis with Python** curriculum from [freeCodeCamp](https://www.freecodecamp.org/).

## 💡 What it Calculates
The `demographic_data_analyzer.py` script uses Pandas to answer the following specific questions about the dataset (`adult.data.csv`):

1. **Race Representation:** Counts how many people of each race are represented in the dataset.
2. **Average Age:** Calculates the average age of all men in the dataset.
3. **Education Percentage:** Calculates the percentage of the dataset that holds a Bachelor's degree.
4. **Education and Salary:** Determines what percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K.
5. **No Advanced Education and Salary:** Determines what percentage of people *without* advanced education make more than 50K.
6. **Minimum Work Hours:** Finds the absolute minimum number of hours anyone works per week.
7. **Minimum Hours vs Salary:** Calculates the percentage of people working those minimum hours who still make more than 50K.
8. **Highest Earning Country:** Identifies the country with the highest percentage of people making >50K and calculates that percentage.
9. **Top Occupation in India:** Identifies the most popular occupation for those making >50K in India.

## 🛠️ Technologies Used
- **Python 3**
- **Pandas:** The core library used for data manipulation, grouping, and series calculations.

## 🚀 How to Run
1. Ensure you have Pandas installed:
   ```bash
   pip install pandas
   ```
2. Run the main script to print all the demographic data points to the console:
   ```bash
   python main.py
   ```
3. To run the automated unit tests:
   ```bash
   python test_module.py
   ```
