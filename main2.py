import pandas as pd
import os
import csv
from datetime import datetime
import time
import json

class Register:
    def __init__ (self, name,):
        self.name = name

    def reg(self):
        file_exists = os.path.isfile('user_data.csv')
        with open('user_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['user_name'])  # Write header if file does not exist
            writer.writerow([self.name])
        print(f"User '{self.name}' registered successfully.")

    
class Login(Register):
    def __init__(self, name):
        super(). __init__(name)

    def log(self):
        try:
            with open('user_data.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['user_name'] == self.name:
                        print(f"Welcome back, {self.name}!")
                        return True
                print("User not found. Registering new user.")
                self.reg()
                return False
        except FileNotFoundError:
            print("No user data found. Creating new file and registering user.")
            self.reg()
            return False
        
class Details:
    def __init__(self, day,month,year):
        self.day = day
        self.month =month
        self.year =year

    def display_info(self):
        print(f"your birthday is {self.day},{self.month},{self.year}")
    
    def age(self):
        calculate_age = lambda year: datetime.now().year - year
        age = calculate_age(self.year)
        return age

class GettingToKnowYou:
    def __init__(self, name):
        self.name = name
        self.movies_watched = 0
        self.max_movies = 5
        self.movie_ratings = {}  # Dictionary to store movie ratings
        self.seen_movies = set()  # Set to track movies already seen

    def rate(self):
        data = pd.read_csv("new_movie_data.csv")
        
        while self.movies_watched < self.max_movies:
            movie_row = data.sample().iloc[0]
            movie = movie_row['title']
            genre = movie_row['genres']  # Adjust column name to match your CSV
            avg_rating = movie_row['vote_average']  # Adjust column name to match your CSV

            if movie in self.seen_movies:
                continue  # Skip movies that have already been rated
            
            self.seen_movies.add(movie)
            
            print(f"Have you ever watched this: {movie}")
            answer = input("Enter 'yes' or 'no': ").strip().lower()
            
            if answer == "yes":
                rating = input("How did you find it? Can you rate it from 1-10: ").strip()
                
                # Ensure the rating is a valid number
                try:
                    rating = int(rating)
                    if 1 <= rating <= 10:
                        self.movie_ratings[movie] = {
                            'user_rating': rating,
                            'genre': genre,
                            'average_rating': avg_rating
                        }
                        print(f"Your rating: {rating}")
                    else:
                        print("Rating should be between 1 and 10.")
                        continue  # Skip the increment of movies_watched if rating is invalid
                except ValueError:
                    print("Please enter a valid number for rating.")
                    continue  # Skip the increment of movies_watched if input is invalid
                
                self.movies_watched += 1
                print(f"Movies watched = {self.movies_watched}")
            elif answer == "no":
                print("Okay, let's try another movie.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        self.save_ratings()

    def save_ratings(self):
        user_data = {
            'movies': self.movie_ratings
        }
        
        # Save as JSON
        json_filename = f'{self.name}_movie_data.json'
        with open(json_filename, 'w') as json_file:
            json.dump(user_data, json_file, indent=4)
        
        # Save as CSV
        csv_filename = f'{self.name}_movie_data.csv'
        user_data_flat = [{
            'movie': movie,
            'user_rating': details['user_rating'],
            'genre': details['genre'],
            'average_rating': details['average_rating']
        } for movie, details in self.movie_ratings.items()]
        user_data_df = pd.DataFrame(user_data_flat)
        user_data_df.to_csv(csv_filename, index=False)
        
        print(f"\nUser movie data saved to '{json_filename}' and '{csv_filename}'")
            

def main():
    name = input("enter your name: ").lower()
    loginobj = Login(name)
    loginobj.log()
    month = int(input("Enter your birth month (as a number): "))
    day = int(input("Enter your birth day (as a number): "))
    year = int(input("enter your year of birth"))
    gender = input("Enter your gender").lower()
    

    details_obj = Details(month,day,year)
    if (gender == "male" or gender== "female"):
        print(gender)
    else:
        print("unknown gender")
    time.sleep(1)
    details_obj.display_info()
    time.sleep(2)
    age = details_obj.age()
    print(f"You are {age} years old.")
    time.sleep(2)
    known = GettingToKnowYou(name)
    known.rate()


# data science
    
if __name__ == "__main__":
    main()