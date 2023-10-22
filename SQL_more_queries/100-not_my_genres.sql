-- List all genres not associated with show "Dexter"
SELECT DISTINCT name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE name NOT IN (
    SELECT name FROM tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = "Dexter"
)
ORDER BY name;
