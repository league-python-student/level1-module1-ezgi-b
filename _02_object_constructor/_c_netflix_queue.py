class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    last_airbender = Movie("The Last Airbender", 0)
    tangled = Movie("Tangled", 5)
    toy_story = Movie("Toy Story", 3)
    httyd = Movie("How to Train Your Dragon", 5)
    chronicle = Movie("Chronicle", 4)
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    print(Movie.get_ticket_price(last_airbender))
    # TODO 3) Instantiate a NetflixQueue object.
    queue = NetflixQueue()
    # TODO 4) Add your movies to the Netflix queue.
    queue.add_movie(last_airbender)
    queue.add_movie(tangled)
    queue.add_movie(toy_story)
    queue.add_movie(httyd)
    queue.add_movie(chronicle)
    # TODO 5) Print all the movies in your queue.
    queue.print_movies()
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    print("The best movie is " + queue.get_best_movie().title)
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."
    print("The second best movie is " + queue.get_movie(1).title)

