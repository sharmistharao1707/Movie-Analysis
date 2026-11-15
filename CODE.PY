import pandas as pd
import matplotlib.pyplot as plt
import csv


with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie_ID", "Movie_Name", "Genre", "Rating", "Year"])
    writer.writerow([1, "Inception", "Sci-Fi", 8.8, 2010])
    writer.writerow([2, "Titanic", "Romance", 7.8, 1997])
    writer.writerow([3, "Avengers", "Action", 8.0, 2012])
    writer.writerow([4, "Interstellar", "Sci-Fi", 8.6, 2014])


df = pd.read_csv("movies.csv")


while True:
    print("\n====== MOVIE RATING AND ANALYSIS ======")
    print("1. Display DataFrame")
    print("2. Display Rows and Columns")
    print("3. Add New Movie")
    print("4. Delete Movie")
    print("5. Line Graph")
    print("6. Bar Graph")
    print("7. Histogram")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(df)

    elif choice == 2:
        print("Number of Rows:", df.shape[0])
        print("Number of Columns:", df.shape[1])

    elif choice == 3:
        mid = int(input("Movie ID: "))
        name = input("Movie Name: ")
        genre = input("Genre: ")
        rating = float(input("Rating: "))
        year = int(input("Release Year: "))

        df.loc[len(df)] = [mid, name, genre, rating, year]
        df.to_csv("movies.csv", index=False)
        print("Movie added successfully")

    elif choice == 4:
        mid = int(input("Enter Movie ID to delete: "))
        df = df[df["Movie_ID"] != mid]
        df.to_csv("movies.csv", index=False)
        print("Movie deleted successfully")

    elif choice == 5:
        plt.plot(df["Movie_Name"], df["Rating"])
        plt.xlabel("Movie Name")
        plt.ylabel("Rating")
        plt.title("Movie Ratings - Line Graph")
        plt.show()

    elif choice == 6:
        plt.bar(df["Movie_Name"], df["Rating"])
        plt.xlabel("Movie Name")
        plt.ylabel("Rating")
        plt.title("Movie Ratings - Bar Graph")
        plt.show()

    elif choice == 7:
        plt.hist(df["Rating"], bins=5)
        plt.xlabel("Rating")
        plt.ylabel("Frequency")
        plt.title("Rating Distribution")
        plt.show()

    elif choice == 8:
        print("Program exited successfully")
        break

    else:
        print("Invalid choice")
