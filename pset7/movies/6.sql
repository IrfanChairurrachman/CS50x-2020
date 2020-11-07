select avg(ratings.rating) as 'Average Rating' 
from movies 
join ratings 
on movies.id = ratings.movie_id 
where movies.year = 2012;