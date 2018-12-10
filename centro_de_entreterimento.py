import filme
import fresh_tomatoes

a_origem = filme.Filme("A ORIGEM", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=HiixbtN-O24")
toy_story = filme.Filme("TOY STORY", "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
no_limite_do_amanha = filme.Filme("NO LIMITE DO AMANHA", "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg", "https://www.youtube.com/watch?v=EA6EWWwDbtY")
os_vingadores = filme.Filme("OS VINGADORES", "https://upload.wikimedia.org/wikipedia/pt/9/90/Avengers_Infinity_War.jpg","https://www.youtube.com/watch?v=t_ULBP6V9bg")
animais_fantasticos = filme.Filme("ANIMAIS FANTASTICOS E ONDE HABITAM","https://upload.wikimedia.org/wikipedia/pt/c/c7/Capa_de_Animais_Fant%C3%A1sticos_e_Onde_Habitam.jpg", "https://www.youtube.com/watch?v=HRdIQ5oLHG4")
django = filme.Filme("DJANGO", "https://upload.wikimedia.org/wikipedia/pt/8/8b/Django_Unchained_Poster.jpg", "https://www.youtube.com/watch?v=tivv135aGbc")
x_man = filme.Filme("X-MAN","https://upload.wikimedia.org/wikipedia/en/a/a2/X-Men_-_The_Official_Game_Coverart.png", "https://www.youtube.com/watch?v=nbNcULQFojc")
as_branquelas = filme.Filme("AS BRANQUELAS", "https://upload.wikimedia.org/wikipedia/pt/d/de/White_chicks.jpeg", "https://www.youtube.com/watch?v=y5nr345eBQ0")

filmes = [no_limite_do_amanha, os_vingadores, a_origem, animais_fantasticos, django, toy_story, x_man, as_branquelas]
fresh_tomatoes.open_movies_page(filmes)