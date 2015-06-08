import movie
import fresh_tomatoes

#Creating instances of my movie class with a list of my favorite movies.
alien = movie.Movie("Alien",
                    ("http://ia.media-imdb.com/images/M/MV5BMTU1ODQ4NjQyOV5BMl5BanBnXk"
                     "FtZTgwOTQ3NDU2MTE@._V1_SX214_AL_.jpg"),
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

inception = movie.Movie("Inception",
                        ("http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5Ban"
                         "BnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg"),
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

pierrot_le_fou = movie.Movie("Pierrot Le Fou",
                             ("http://ia.media-imdb.com/images/M/MV5BMTIwODgyNDU3N15BM"
                              "l5BanBnXkFtZTcwMDIyMjU1MQ@@._V1_SY317_CR5,0,214,317_AL_"
                              ".jpg"),
                             "https://www.youtube.com/watch?v=E81T4FUIz-I")

diabolique = movie.Movie("Diabolique",
                         ("http://ia.media-imdb.com/images/M/MV5BMTcwNzc5MjI5Nl5BMl5Ba"
                          "nBnXkFtZTYwNjIwMzc5._V1_SY317_CR5,0,214,317_AL_.jpg"),
                         "https://www.youtube.com/watch?v=BzbGtjtfZwA")

annie_hall = movie.Movie("Annie Hall",
                         ("http://ia.media-imdb.com/images/M/MV5BMTU1NDM2MjkwM15BMl5Ba"
                          "nBnXkFtZTcwODU3OTYwNA@@._V1_SX214_AL_.jpg"),
                         "https://www.youtube.com/watch?v=OqVgCfZX-yE")

star_wars = movie.Movie("Star Wars",
                        ("http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5Ban"
                         "BnXkFtZTcwMzEyMTIyMw@@._V1_SX214_AL_.jpg"),
                        "https://www.youtube.com/watch?v=9gvqpFbRKtQ")

getaway = movie.Movie("Getaway",
                      ("http://ia.media-imdb.com/images/M/MV5BOTEwNDUyNjUyNV5BMl5BanBn"
                       "XkFtZTYwMzAxOTI5._V1_SY317_CR10,0,214,317_AL_.jpg"),
                      "https://www.youtube.com/watch?v=9FhkOy1inT8")

italian_job = movie.Movie("The Italian Job",
                          ("http://ia.media-imdb.com/images/M/MV5BNTI1ODYwNzg3Nl5BMl5B"
                           "anBnXkFtZTcwMDYzMjk3OA@@._V1_SX214_AL_.jpg"),
                          "https://www.youtube.com/watch?v=FEltJsIwSvE")

throne_of_blood = movie.Movie("Throne of Blood",
                              ("http://ia.media-imdb.com/images/M/MV5BMTM1MTk2NDIzOV5B"
                               "Ml5BanBnXkFtZTcwMTA5ODQxMQ@@._V1_SY317_CR5,0,214,317_A"
                               "L_.jpg"),
                              "https://www.youtube.com/watch?v=PoYzsDVyFRU")

#Putthing the movies in a list to pass on to the script that creates our page.
movie_list = [alien, inception, pierrot_le_fou, diabolique, annie_hall, star_wars,
              getaway, italian_job, throne_of_blood]


def main():
    #Creates the movies web page.
    fresh_tomatoes.open_movies_page(movie_list)

if __name__ == "__main__":
    main()
