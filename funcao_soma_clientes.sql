--Crie uma função que some todos os clientes cadastrados em uma loja durante um dia--


CREATE FUNCTION getTotalCustomers(data DATE)

RETURNS INT

BEGIN

DECLARE total INT;

SELECT COUNT(*) INTO total FROM customers WHERE data_cadastro = data;

RETURN total;

END

SELECT getTotalCustomers('2022-12-26');
