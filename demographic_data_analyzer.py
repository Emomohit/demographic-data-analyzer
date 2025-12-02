import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Advanced education filter
    higher_education = df[df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )]
    lower_education = df[~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )]

    # Higher education rich %
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )
    # Lower education rich %
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Min work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among minimum workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Highest earning country and %
    country_earn = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean() * 100
    )
    highest_earning_country = country_earn.idxmax()
    highest_earning_country_percentage = round(country_earn.max(), 1)

    # 8. Top occupation in India for >50K earners
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }