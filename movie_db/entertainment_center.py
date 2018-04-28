import fresh_tomatoes
import media


toy_story = media.Movie( "Toy Story" , 
                          "A story of a boy and his toys that come to life" ,
                          "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg" ,
                          "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar" ,
                     "A marine on an alien planet" ,
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io" )

#print( avatar.storyline )
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock" ,
                             "Using rock music to learn" ,
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille" ,
                          "A rat is a chef in Paris" ,
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "http://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg" ,
                                "https://www.youtube.com/watch?v=dtiklALGz20")

hunger_games = media.Movie("Hunger Games" ,
                           "A really real reality show",
                           "https://en.wikipedia.org/wiki/The_Hunger_Games_(film)#/media/File:HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8" )

movies = [ toy_story , avatar , school_of_rock , ratatouille , midnight_in_paris , hunger_games ]
fresh_tomatoes.open_movies_page( movies )
