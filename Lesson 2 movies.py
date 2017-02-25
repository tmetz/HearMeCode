movie_titles = ["Mr. Holland\'s Opus","Back To The Future","Hidden Figures","Contact","Walk On Water"]
parental_rating = ["PG","PG","PG","PG","R"]
bechdel_rating = ["0","2","3","3","0"]
imdb_rating = ["7.3", "8.5", "7.9", "7.4", "7.4"]
genres = ["Drama","Sci-Fi","History","Sci-Fi","Drama"]

for i, movie in enumerate(movie_titles):
    print movie_titles[i] + ", " + parental_rating[i] + ", " + bechdel_rating[i] + ", " +  imdb_rating[i] + ", " + genres[i]
    
