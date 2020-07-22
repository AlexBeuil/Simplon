use sakila;

## 1 - Afficher les 10 locations les plus longues 
##		(nom/prenom client, film, video club, durée)

select customer.last_name, customer.first_name, film.title, customer.store_id, datediff(return_date, rental_date) FROM customer
join rental on customer.customer_id = rental.customer_id
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id 
order by datediff(return_date, rental_date)
desc limit 10;  

## 2 - Afficher les 10 meilleurs clients actifs par montant dépensé 
##		(nom/prenom client, montant dépensé)

select customer.last_name, customer.first_name, sum(payment.amount) from customer
join payment on customer.customer_id = payment.customer_id
group by customer.last_name, customer.first_name 
order by sum(payment.amount)
desc limit 10;

## 3 - Afficher la durée moyenne de location par film triée de maniére descendante

select film.title, avg(film.rental_duration) from film
group by film.title 
order by avg(film.rental_duration) desc limit 10;

## 4 - Afficher tous les films n'ayant jamais été empruntés

select film.title, rental_date
from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
where rental_date is null;

## 5 - Afficher le nombre d'employés (staff) par video club

select count(staff.staff_id), address.district 
from staff 
join address on staff.address_id = address.address_id
group by address.district;

## 6 - Afficher les 10 villes avec le plus de video club

select city.city, count(staff.store_id)
from city
join address 
join staff 
ON city.city_id = address.city_id AND address.address_id = staff.address_id
group by city.city order by count(staff.store_id);  

## 7 - Afficher les films les plus long dans lequel joue Johnny Lollobrigida

select film.title, length 
from film 
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where first_name = 'Johnny' and last_name = 'Lollobrigida'
order by length desc limit 1;

## 8 - Afficher le temps moyen de location du film 'Academy dinosaur'

select film.title, avg(film.rental_duration)
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.rental_id
where film.title = 'Academy dinosaur'
order by avg(film.rental_duration)

## 9 - Afficher les films avec plus de deux exemplaires en invenatire 
##		(store id, titre du film, nombre d'exemplaires)

SELECT inventory.store_id, film.title, COUNT(inventory.film_id) 
FROM film
JOIN inventory ON film.film_id = inventory.film_id 
GROUP BY inventory.store_id, film.title HAVING COUNT(inventory.film_id) > 2;

## 10 - Lister les films contenant 'din' dans le titre

SELECT film.title FROM film
WHERE film.title like "%din%";

## 11 - Lister les 5 films les plus empruntés 

SELECT film.title, COUNT(rental.rental_date) FROM film
JOIN inventory ON film.film_id = inventory.film_id 
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title order by COUNT(rental.rental_date) desc limit 5;

## 12 - Lister les films sortis en 2003, 2005 et 2006

SELECT film.title, film.release_year FROM film
WHERE release_year = '2003' or '2005' or '2006';

## 13 - Afficher les films ayant été empruntés mais n'ayant pas encore été restitués, 
##		triés par date d'emprunt. Afficher seulement les 10 premiers. 

SELECT film.title, rental.rental_date, rental.return_date FROM rental 
JOIN inventory on rental.inventory_id = inventory.inventory_id 
JOIN film on inventory.film_id = film.film_id 
WHERE rental.return_date is null order by rental.rental_date limit 10;

## 14 - Afficher les films d'action durant plus de 2h

SELECT film.title, category.name, film.length from film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on category.category_id = film_category.category_id
WHERE film.length > 120 AND category.name = 'Action' ORDER BY film.length desc;

## 15 - Afficher tous les utilisateurs ayant emprunté des films avec la mention NC-17

SELECT film.title, customer.first_name, customer.last_name, film.rating FROM film 
JOIN inventory on film.film_id = inventory.film_id 
JOIN rental on inventory.inventory_id = rental.inventory_id 
JOIN customer on rental.customer_id = customer.customer_id 
WHERE film.rating = 'NC-17';

## 16 - Afficher les films d'animation dont la langue originale est l'anglais

SELECT film.title, category.name, language.name FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on category.category_id = film_category.category_id
JOIN language on language.language_id = film.language_id 
WHERE category.name = 'Animation' AND language.name = 'English';

## 17 - Afficher les films dans lesquels une actrice nommée Jennifer a joué 
##		(bonus: en même temps qu'un acteur nommé Johnny)

SELECT john_film.title FROM 
(SELECT film.film_id FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id 
WHERE actor.first_name = 'Jennifer') as jen_film
JOIN 
(SELECT film.film_id, film.title FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Johnny') as john_film
USiNG(film_id);  

## 18 - Quelles sont les 3 catégories les plus empruntées ? 

SELECT category.name, count(category.name) FROM category 
JOIN film_category USING(category_id) 
JOIN film USING(film_id)
GROUP BY category.name ORDER BY COUNT(category.name) desc LIMIT 3; 

## 19 - Quelles sont les 10 villes ou on a fait le plus de location ?

SELECT city.city, count(rental.rental_date) FROM city 
JOIN address USING(city_id)
JOIN customer USING(address_id)
JOIN rental USING(customer_id)
GROUP BY city.city ORDER BY count(rental.rental_date) desc LIMIT 10;

## 20 - Lister les acteurs ayant joué dans au moins 1 film

SELECT actor.first_name, actor.last_name, COUNT(film.title)
FROM film 
JOIN film_actor USING(film_id)
JOIN actor USING(actor_id)
GROUP BY actor.first_name, actor.last_name HAVING count(film.title) >= 1 ORDER BY count(film.title) asc;

