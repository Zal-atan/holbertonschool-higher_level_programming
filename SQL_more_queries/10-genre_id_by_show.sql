-- Lists all shows contained in hbtn_0d_tvshows which have atleast one genre linked
-- SELECT tv_shows.title, tv_show_genres.genre_id
-- FROM tv_shows, tv_show_genres
-- WHERE tv_shows.id = tv_show_genres.show_id
-- ORDER BY  tv_shows.title, tv_show_genres.genre_id;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
