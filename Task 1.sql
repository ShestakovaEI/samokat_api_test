SELECT "courierId",
	COUNT(*)
FROM "Orders"
WHERE "inDelivery"=true
GROUP BY "courierId";