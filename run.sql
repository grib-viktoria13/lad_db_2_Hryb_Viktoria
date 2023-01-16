CALL get_artists('UNITED STATES');

SELECT get_artist('UNITED STATES');

INSERT INTO artist(id, name, country, tcu, years) VALUES (10, 'Ed Sheeran', 'United Kingdom', 246.7, 2011);

--DELETE FROM artist where id = 10;

select * from artist order by id;