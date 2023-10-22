-- List all shows and their ratings in descending order
SELECT tv_shows.title, sum(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC
