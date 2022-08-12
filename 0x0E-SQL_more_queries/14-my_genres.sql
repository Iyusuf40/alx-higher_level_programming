-- test
-- query
SELECT name FROM tv_genres
INNER JOIN tv_show_genres AS tv_sg
ON tv_genres.id IN (
SELECT tv_show_genres.genre_id FROM tv_show_genres
INNER JOIN tv_shows
ON tv_show_genres.show_id = (
SELECT tv_shows.id FROM tv_shows
WHERE tv_shows.title = "Dexter"))
GROUP BY name
ORDER BY name; 
