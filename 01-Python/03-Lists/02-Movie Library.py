"""
Create a list of dictionaries where each dictionary represents a 
movie (title, year, genre). Write functions to:
•Find a movie by title.
•Check if a movie is before a certain year.
•Print all movies of a specific genre. (Use if statements and list indexing)
"""
def find_by_name(movie_list,name):
    for movie in movie_list:
        if movie["name"] == name:
            return movie 
    
    return None

def check_before_year(movie, year):
    if movie["year"] < year:
        return True
    else:
        return False
        

def print_by_genre(movie_list, genre):
    for movie in movie_list:
        if movie["genre"] == genre:
            print(movie)

movie_list = [
            {
                "name":"The Shawshank Redemption",
                "year":1994,
                "genre": "Drama"
            },
            {
                "name":"The Godfather",
                "year":1972,
                "genre":"Drama"
            },
            {
                "name":"The Dark Knight",
                "year":2008,
                "genre":"crime"
            }]


movie = find_by_name(movie_list,"The Dark Knight")
print(movie)
print("the movie was made before 2012") if check_before_year(movie,2012) == True else print("the movie was made after 2012") 
print_by_genre(movie_list, "Drama")