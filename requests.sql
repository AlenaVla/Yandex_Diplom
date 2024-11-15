SELECT c.login, COUNT (*)
FROM "Couriers" AS c INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;


SELECT track,
        CASE
        WHEN "inDelivery" = true THEN 1
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
    ELSE 0 END AS status
FROM "Orders";