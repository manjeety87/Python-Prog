def checkRating(rating):
    if 0 <= rating <= 10:
        return True
    else:
        print("Error: Please give ratings between 0 to 10.")
    return False

class Movie:
	def __init__(self, title, director, release_year, rating):
		self.__title = title
		self.__director = director
		self.__release_year = release_year
		self.__rating = rating
	def get_title(self):
		return self.__title
	def get_director(self):
		return self.__director
	def set_title(self, title):
		self.__title = title
        
	def set_director(self, director):
		self.__director = director
	def get_rating(self):  
		return self.__rating
	def set_rating(self, rating): # OPTIMIZE: the checkRating function rating is not working
		self.__rating = rating
		# if checkRating(rating): 
		# 	self.__rating = rating
		# 	return True
		# else:
		# 	print("Invalid rating")

		# return False
	
    #Add methods for getting and setting the release year
movie1 = Movie("The Matrix", "Lana Wachowski", 1999, 8.7)
movie2 = Movie("Avengers", "Joss Whedon", 2012, 8.0)


# print(movie2.get_title())
# print(movie2.set_title("The Avengers"))
# print(movie2.get_title())
# print(movie2.get_director())
# print(movie2.set_director("Stanley"))
# print(movie2.get_director())
# print(movie2.get_rating())
# print(movie2.set_rating(8.0))
# print(movie2.get_release_year())
# print(movie2.set_release_year(1999))



class MovieCollection:
    def __init__(self):
        self.movies = {}
		
    def add_movie(self, movie):
        if movie.get_title() in self.movies:
            print(f"'{movie.get_title()}' already exists in the movie collection.")
        else:
            self.movies[movie.get_title()] = movie
    
    def get_movie(self, title):
        if title in self.movies:
            return self.movies[title]
        else:
            print(f"'{title}' does not exist in the movie collection.")

    def list_movies(self):
        #Replace pass with your code
        pass
	

def main():
	#Replace pass with your code
	pass
	
main()

