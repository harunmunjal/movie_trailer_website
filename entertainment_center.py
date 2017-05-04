import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

imitation_game = media.Movie("The Imitation Game",
                             "British mathematician Alan Turing builds a machine, which is a prototype of the modern computer, to decipher German codes.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU",
                        "https://www.youtube.com/watch?v=S5CjKEFb-sM")

three_idiots = media.Movie("3 Idiots",
                           "In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")
theory_of_everything = media.Movie("Theory Of Everything",
                           "A look at the life of renowned scientist Stephen Hawking and his love affair with Jane. He was diagnosed with the motor neuron disease but that didn't stop him from becoming a brilliant mind.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSgW7hpezP5xtikV7WqwwqFm37kqMeJeFEGpYcO30CDcchn9g8m",
                        "https://www.youtube.com/watch?v=Salz7uGp72c")
znmd = media.Movie("Zindagi Na Milegi Dobara",
                   "Friends Kabir, Imran and Arjun take a vacation in Spain before Kabir's marriage. The trip turns into an opportunity to mend fences, heal wounds, fall in love with life and combat their worst fears.",
                   "https://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
                   "https://www.youtube.com/watch?v=FJrpcDgC3zU")

movies = [toy_story, avatar, imitation_game, three_idiots, theory_of_everything, znmd]
fresh_tomatoes.open_movies_page(movies)
#print(avatar.storyline)
#avatar.show_trailer()
