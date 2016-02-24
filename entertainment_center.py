import media
import fresh_tomatoes

#for i-robot
avatar = media.Movie("Avatar",
					 "Science-Fiction",
					 "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
					 "https://www.youtube.com/watch?v=cX0R3mXaod8")
irobot = media.Movie("I_Robot",
					 "Science-Fiction",
					 "https://fanart.tv/fanart/movies/2048/movieposter/i-robot-52175b0ad5313.jpg",
					 "https://www.youtube.com/watch?v=rL6RRIOZyCM")
gforce = media.Movie("G-Force",
					 "Science-Fiction",
					 "http://cdn.traileraddict.com/content/walt-disney-pictures/gforce-2.jpg",
					 "https://www.youtube.com/watch?v=VAMUfDvAQeo")
life_of_pi = media.Movie("Life Of Pi",
					 "Science-Fiction",
					 "http://cdn.traileraddict.com/content/20th-century-fox/life_of_pi-4.jpg",
					 "https://www.youtube.com/watch?v=j9Hjrs6WQ8M")
ratatouille = media.Movie("Ratatouille",
					 "Science-Fiction",
					 "https://www.movieposter.com/posters/archive/main/50/MPW-25274",
					 "https://www.youtube.com/watch?v=bKedSHDpkvI")
frozen = media.Movie("Frozen",
					 "Science-Fiction",
					 "http://vignette2.wikia.nocookie.net/disney/images/2/27/Frozen_-_Poster.jpg/revision/latest?cb=20141122215852",
					 "https://www.youtube.com/watch?v=FLzfXQSPBOg")
belaseshe = media.Movie("Belaseshe",
					 "Values Of Relationship",
					 "http://f23.wapka-files.com/download/1/7/7/1304460_177888ae00010456cd171f75.jpg/b4ce0625ef11a2f754ab/Belaseshe%2B(2015)%2Bbengali%2Bmovie%2Bposter.jpg",
					 "https://www.youtube.com/watch?v=X0zUrtioA2g")
highway = media.Movie("Highway",
					 "Indian Bangla",
					 "https://s-media-cache-ak0.pinimg.com/236x/7f/b6/e7/7fb6e7eb7ac3d13315de18c3f2ca7498.jpg",
					 "https://www.youtube.com/watch?v=lWrN_bBbXQc")
hridmajharay = media.Movie("Hridmajharay",
					 "Indian Bangla",
					 "http://arounds.us/wp-content/uploads/2015/08/Hrid-Majharey-2014.jpg",
					 "https://www.youtube.com/watch?v=ve0MqOP_DKo")
aklaakash = media.Movie("Aklaakash",
					 "Indian Bangla",
					 "https://upload.wikimedia.org/wikipedia/en/1/15/Ekla_Akash_poster.jpg",
					 "https://www.youtube.com/watch?v=2wG7m8P88tM")
sudhu_tomary_jonno = media.Movie("Sudhu Tomary Jonno",
					 "Indian Bangla",
					 "http://2.bp.blogspot.com/-k944wXFERFw/VfRK8bh1pAI/AAAAAAAALgU/1sE6321XMAM/s1600/shudhu-tomari-jonno-bengali-movie-first-look.jpg",
					 "https://www.youtube.com/watch?v=UHxKE9Qaa6o")
ebersobor = media.Movie("Eber Sobor",
					 "Indian Bangla",
					 "https://upload.wikimedia.org/wikipedia/en/6/66/Ebar_Shabor_poster.jpg",
					 "https://www.youtube.com/watch?v=lg-umWenbbM")
bomkeesh_fire_elo = media.Movie("Byomkesh Phire Elo(2014)",
					 "Indian Bangla",
					 "https://upload.wikimedia.org/wikipedia/en/b/b1/Byomkesh_Phire_Elo_poster.jpg",
					 "https://www.youtube.com/watch?v=6I9986kdFUs")
royel_bengle_tigher = media.Movie("The Royal Bengal Tiger 2014",
					 "Indian Bangla",
					 "https://pbs.twimg.com/media/Bewt1y5CQAAhb6A.jpg",
					 "https://www.youtube.com/watch?v=qbiZUc7nh_I")
movies = [avatar,irobot,gforce,life_of_pi,frozen,ratatouille,belaseshe,highway,hridmajharay,aklaakash,sudhu_tomary_jonno,ebersobor,bomkeesh_fire_elo,royel_bengle_tigher]
fresh_tomatoes.open_movies_page(movies)
