--  creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET items.quantity = items.quantity - NEW.number
    WHERE items.name = NEW.item_name;
END$$

DELIMITER ;
