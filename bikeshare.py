import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA:
        city = input("Please type a city name (chicago, new york city, washington) : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in months:
        month = input("Please type a month name or all ('january', 'february', 'march', 'april', 'may', 'june', 'all') : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in days:
        day = input("Please type a day name or all ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all') : ").lower()

    print('-'*40)
    print("Your choices are {} from cities , {} from months, {} from days.".format(city, month, day))
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
    
    # convert "Start Time" to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # add month column
    df['month'] = df['Start Time'].dt.month_name()
    # print(df.head())
    
    # add day column
    df['day_name'] = df['Start Time'].dt.day_name()
    # print(df.head())
    
    # add hour column
    df['hour'] = df['Start Time'].dt.hour
    # print(df.head())    
    
    # Load Filtered month
    if month != "all":
        df = df[df['month'] == month.title()]
        # print(df.head())
    
        
    # Load Filtered day
    if day != "all":
        df = df[df['day_name'] == day.title()]
        # print(df.head())        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # get choosen month and day
    choosen_month = df['month'].unique()[0]  if df['month'].nunique() == 1  else "all months"
    choosen_day = df['day_name'].unique()[0]  if df['day_name'].nunique() == 1  else "all days"
    
    # print("choosen month is {}".format(choosen_month))
    # print("choosen day is {}".format(choosen_day))
    
    
    # TO DO: display the most common month
    # check for variation in month column
    if choosen_month == "all months":
        print("The most common start month is '{}' in '{}s'\n".format(df['month'].mode()[0],choosen_day))
    else:
        print("**You must choose all months to see the most common month.(Your choice was {})**\n".format(choosen_month))


    # TO DO: display the most common day of week
    # check for variation in day_name column
    if choosen_day == "all days":
        print("The most common start day is '{}' in '{}'\n".format(df['day_name'].mode()[0],choosen_month))
    else:
        print("**You must choose all days to see the most common day.(Your choice was {})**\n".format(choosen_day))

    # TO DO: display the most common start hour
    print("The most common start hour is {}\n".format(df['hour'].mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is \n'{}'\n".format(df['Start Station'].mode()[0]))
    

    # TO DO: display most commonly used end station
    print("The most commonly used end station is \n'{}'\n".format(df['End Station'].mode()[0]))
    

    # TO DO: display most frequent combination of start station and end station trip
    # create new column for trip
    df['start_end_trip'] = df['Start Station'] + " ===> " + df['End Station']
    # print(df['start_end_trip'].head())
    print("The most frequent combination of start station and end station trip is \n'{}'\n".format(df['start_end_trip'].mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration_days = int(total_duration//86400)
    total_duration_hours = int((total_duration%86400)//3600)
    total_duration_minutes = int((total_duration%3600)//60)
    total_duration_seconds = round(total_duration% 60,2)
    print("Total travel time is {} seconds ({} days, {} hours, {} minutes, {} seconds)".format(total_duration, total_duration_days, total_duration_hours, total_duration_minutes, total_duration_seconds))

    # TO DO: display mean travel time
    mean_duration = round(df['Trip Duration'].mean(),2)
    mean_duration_hours = int(mean_duration//3600)
    mean_duration_minutes = int((mean_duration%3600)//60)
    mean_duration_seconds = round(mean_duration % 60,2)  
    print("Mean travel time is {} seconds ({} hours, {} minutes, {} seconds)".format(mean_duration,mean_duration_hours,mean_duration_minutes,mean_duration_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types : \n{} \n".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    # check for Gender Column
    if 'Gender' in df.columns:
        # print("gender found")
        print("The counts of user gender : \n{}\n".format(df['Gender'].value_counts()))
    else:
        print("There is no data about Gender\n")    

    # TO DO: Display earliest, most recent, and most common year of birth
    # check for Birth Year Column
    if 'Birth Year' in df.columns:
        # print("Birth Year found")
        print("The earliest year of birth : {}\n".format(int(df['Birth Year'].min())))
        print("The most recent year of birth : {}\n".format(int(df['Birth Year'].max())))
        print("The most common year of birth : {}\n".format(int(df['Birth Year'].mode())))
    else:
        print("There is no data about Birth Year\n")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def additional_questions(df):
    # What is the best day of months(which have the maximum number of trips)
    df["day_of_month"] = df['Start Time'].dt.day
    # print(df["day_of_month"].head())
    print("'{} of month' is the day which have the maximum number of trips.".format(df["day_of_month"].mode()[0]))
    
    
    # What is the best day in (which have the maximum number of trips)
    df["day_of_year"] = df['Start Time'].dt.date
    # print(df["day_of_year"].head())
    print("'{}' is the day which have the maximum number of trips ever in the selected period.".format(df["day_of_year"].mode()[0]))


def show_raw_data(df):
    df_lines = df.shape[0]
    current_row = 0
    while True:
        show_raw = input("\nDo You want to see a raw data of selected parameters ? 'y' or 'n' \n")
        if show_raw != 'y':
            break
        elif current_row >= df_lines:
            print("End of DataFrame")
            break
        else:
            print(df[current_row:current_row+5])
            current_row += 5


def main():
    while True:
        city, month, day = get_filters()
        print("\nWait Seconds ....\n")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        additional_questions(df)
        show_raw_data(df)
        
        restart = input("\nWould you like to restart? Enter 'yes' or 'y' to Restart or any thing to end.\n")
        if restart.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
	main()
