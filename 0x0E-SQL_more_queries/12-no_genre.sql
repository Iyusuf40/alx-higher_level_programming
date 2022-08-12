-- test
-- query
SELECT tv_shows.title title, tv_show_genres.genre_id genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = NULL
ORDER BY title, genre_id;
