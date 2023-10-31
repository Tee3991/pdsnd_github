import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington' : "C:/Users/USER/Downloads/washington.csv" }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter|
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)

    city = None
    while city not in CITY_DATA:
        city = input("Enter the name of the city to analyze (Chicago, New York City, Washington): ").lower()

        if city not in CITY_DATA:
            print('Invalid city. Please try again.')

    month = None
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Enter the name of the month to filter by (January, February, March, April, May, June, or 'all' to apply no month filter): ").lower()

        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Invalid month. Please try again.')

    day = None
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Enter the day of the week to filter by (all, Monday, Tuesday, ..., Sunday): ').lower()

        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Invalid day. Please try again.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    
    # Filter the data by month if applicable
    if month != 'all':
        # Convert the 'Start Time' column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # Extract the month from the 'Start Time' column
        df['month'] = df['Start Time'].dt.month
        # Filter the DataFrame by the selected month
        df = df[df['month'] == month]

    # Filter the data by day if applicable
    if day != 'all':
        # Convert the 'Start Time' column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # Extract the day of the week from the 'Start Time' column
        df['day_of_week'] = df['Start Time'].dt.day_name()
        # Filter the DataFrame by the selected day
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Extract the month from the 'Start Time' column
    df['month'] = pd.to_datetime(df['Start Time']).dt.month

    # Find the most common month if the column has values
    if len(df['month']) > 0:
        common_month = df['month'].mode()[0]
        month_names = ['January', 'February', 'March', 'April', 'May', 'June']
        common_month_name = month_names[common_month - 1]
        print('The most common month for bikeshare travel is:', common_month_name)
    else:
        print('No data available for the month.')

    # Extract the day from the 'Start Time' column
    df['day'] = pd.to_datetime(df['Start Time']).dt.day

    # Find the most common day if the column has values
    if len(df['day']) > 0:
       common_day = df['day'].mode()[0]
       if common_day >= 1 and common_day <= len(day_names):
          common_day_name = day_names[common_day - 1]
          print('The most common day for bikeshare travel is:', common_day_name)
       else:
            print('Invalid day value.')
    else:
         print('No data available for the day.')
    # Extract the hour from the 'Start Time' column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # Find the most common hour if the column has values
    if len(df['hour']) > 0:
        common_hour = df['hour'].mode()[0]
        print('The most common hour for bikeshare travel is:', common_hour)
    else:
        print('No data available for the hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
       
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

# Calculate the duration of each trip
    df['Duration'] = df['End Time'] - df['Start Time']

# Sum up the durations to get the total travel time
    total_travel_time = df['Duration'].sum()

    print("The total travel time is:", total_travel_time)
       
    mean_travel_time = df['Duration'].mean()
    print('the mean travel time is: ',mean_travel_time)

  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_type_counts)
       
    gender_count =df['Gender'].value_counts()
    print('counts of gender : ',gender_count)
       
# Get the earliest year of birth
    earliest_year = df['Birth Year'].min()

# Get the most recent year of birth
    most_recent_year = df['Birth Year'].max()

# Get the most common year of birth
    most_common_year = df['Birth Year'].mode()[0]

    print("Earliest year of birth:", earliest_year)
    print("Most recent year of birth:", most_recent_year)
    print("Most common year of birth:", most_common_year)
       
       

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ")
    if view_data.lower() == "yes":
        print(df.head(5))  # Display the first 5 rows of the DataFrame
        i = 5
        while True:
            view_more = input("Would you like to view 5 more rows? Enter yes or no: ")
            if view_more.lower() == "yes":
                print(df[i:i+5])  # Display the next 5 rows of the DataFrame
                i += 5
            else:
                break
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data('washington', 'may', 'all')
        data_shape = df.shape[0]
        print("The shape of the loaded data is:", data_shape)
        time_stats(df)
        chicago
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
