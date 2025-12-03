SELECT flight_id, * 
FROM flights 
WHERE status = 'On Time';

SELECT * 
FROM bookings 
WHERE total_amount > 1000000;

SELECT * 
FROM aircrafts_data;

SELECT flight_id 
FROM flights 
WHERE aircraft_code = '733';

SELECT * 
FROM tickets 
WHERE passenger_name LIKE 'IRINA %';

SELECT city, COUNT(*) as num_airports
FROM airports_data
GROUP BY city
HAVING COUNT(*) > 1;

SELECT ad.model, COUNT(*) as num_flights
FROM flights f
JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
GROUP BY ad.model;

SELECT book_ref, COUNT(*) as num_tickets
FROM tickets
GROUP BY book_ref
HAVING COUNT(*) > 1;

SELECT flight_id, scheduled_departure, actual_departure
FROM flights 
WHERE actual_departure IS NOT NULL 
AND (actual_departure - scheduled_departure) > INTERVAL '1 hour';