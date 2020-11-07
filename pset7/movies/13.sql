SELECT distinct name FROM people
JOIN stars 
ON people.id = stars.person_id
WHERE stars.movie_id IN
(SELECT distinct movie_id FROM stars
JOIN people 
ON people.id = stars.person_id
WHERE people.name = 'Kevin Bacon' 
AND people.birth = 1958) 
AND name != 'Kevin Bacon';