import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('city: ')
    city = city.lower()
    while city not in ['chicago', 'new york', 'washington']:
        city = input('city:')
        if city in ['chicago', 'new york', 'washington']:
            break
    
    # get user input for month (all, january, february, ... , june)
    month = input('month: ')
    month = month.lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        month = input('month: ')
        if month in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            break
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('day: ')
    day = day.lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturnday', 'sunday','all']:
        day = input('day: ')
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturnday', 'sunday','all']:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    t = pd.to_datetime(df['Start Time'])
    m = pd.Series(data=['january', 'february', 'march', 'april', 'may', 'june'],index=[1,2,3,4,5,6])
    d = pd.Series(data=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturnday', 'sunday'],index=[1,2,3,4,5,6,0])
    df['month']=[m[i.month] for i in t]
    df['dayofweek']=[d[i.dayofweek] for i in t]
    if month == 'all':
        df = df
    else:
        df = df[df['month']==month]
    if day == 'all':
        df = df
    else:
        df = df[df['dayofweek']==day]
 
     return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'].mode().to_string(index = False))

    # display the most common day of week
    print(df['dayofweek'].mode().to_string(index = False))

    # display the most common start hour
    t = pd.to_datetime(df['Start Time'])
    df['hour']=[i.hour for i in t]
    print(df['hour'].mode().to_string(index = False))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode().to_string(index = False))

    # display most commonly used end station
    print(df['End Station'].mode().to_string(index = False))

    # display most frequent combination of start station and end station trip
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    print(df['journey'].mode().to_string(index = False))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df['Trip Duration'].sum())

    # display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df[df['User Type']=='SubScriber']['Gender'].count())
    print(df[df['User Type']=='Customer']['Gender'].count())
    # Display counts of gender
    print(df[df['Gender']=='Male']['Gender'].count())
    print(df[df['Gender']=='Female']['Gender'].count())

    # Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min())
    print(df['Birth Year'].max())
    print(df['Birth Year'].mode().to_string(index = False))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
