SELECT country, count(id) FROM artist GROUP by country;

SELECT genre_name, count(id) FROM genre GROUP by genre_name;

SELECT artist.name, sell.selling FROM sell inner join artist ON artist.id = sell.artist_id order by sell.selling;