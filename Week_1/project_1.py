# Favorite Movie List
print("What are your three favourite movies?")

first_movie = input("First movie: ")
second_movie = input("Second movie: ")
third_movie = input("Third movie: ")
movies = [first_movie, second_movie, third_movie]

print("Your favourite movies are:")
for movie in movies:
    print("-", movie)
print("You entered", len(movies), "movies.")
