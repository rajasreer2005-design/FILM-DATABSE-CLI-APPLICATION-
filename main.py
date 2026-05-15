from api import search_movie, get_movie_details

def main():
    print("\n🎬 Film Database CLI Application")
    print("1. Search Movie")
    print("2. Get Movie Details")
    print("3. Exit")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "1":
            title = input("Enter movie name: ")
            results = search_movie(title)
            for movie in results:
                print(f"- {movie['Title']} ({movie['Year']})")

        elif choice == "2":
            imdb_id = input("Enter IMDb ID: ")
            details = get_movie_details(imdb_id)
            if details:
                print("\n🎬 Movie Details")
                print(f"Title: {details['Title']}")
                print(f"Year: {details['Year']}")
                print(f"Genre: {details['Genre']}")
                print(f"IMDB Rating: {details['imdbRating']}")
                print(f"Plot: {details['Plot']}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()