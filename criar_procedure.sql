CREATE PROCEDURE getTotalPurchases()

BEGIN

SELECT COUNT(*) FROM purchases;

END

CALL getTotalPurchases();
