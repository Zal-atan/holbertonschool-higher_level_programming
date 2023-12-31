-- List all genres and number of shows of that type of genre, in descending order of number of shows per genre
-- order of number of shows per genre
SELECT tv_genres.name AS genre, count(*) AS number_of_shows
    FROM tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
