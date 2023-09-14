CREATE DATABASE mock_data;

USE mock_data;

-- WordPress profiles table
CREATE TABLE wordpress_profiles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255),
  order_number VARCHAR(255),
  content TEXT,
  submitted TINYINT,
  published TINYINT,
  FOREIGN KEY (email, order_number) REFERENCES shopify_transactions(email, order_number)
);

-- Shopify transactions table
CREATE TABLE shopify_transactions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255),
  order_number VARCHAR(255),
  paid TINYINT,
  INDEX idx_shopify_transactions_email_order_number (email, order_number)
);

-- Mock data for wordpress_profiles table
INSERT INTO wordpress_profiles (email, order_number, content, submitted, published)
VALUES
  ('user1@example.com', 'ORD001', 'Profile content for user 1', 1, 1),
  ('user2@example.com', 'ORD002', 'Profile content for user 2', 1, 1),
  ('user3@example.com', 'ORD003', 'Profile content for user 3', 0, 0),
  ('user4@example.com', 'ORD004', 'Profile content for user 4', 1, 1),
  ('user5@example.com', 'ORD005', 'Profile content for user 5', 1, 0),
  ('user6@example.com', 'ORD006', 'Profile content for user 6', 1, 1),
  ('user7@example.com', 'ORD007', 'Profile content for user 7', 1, 0),
  ('user8@example.com', 'ORD008', 'Profile content for user 8', 1, 0),
  ('user9@example.com', 'ORD009', 'Profile content for user 9', 1, 1),
  ('user10@example.com', 'ORD010', 'Profile content for user 10', 0, 0);



-- Mock data for shopify_transactions table
INSERT INTO shopify_transactions (email, order_number, paid)
VALUES
  ('user1@example.com', 'ORD001', 1),
  ('user2@example.com', 'ORD002', 1),
  ('user3@example.com', 'ORD003', 0),
  ('user4@example.com', 'ORD004', 1),
  ('user5@example.com', 'ORD005', 0),
  ('user6@example.com', 'ORD006', 1),
  ('user7@example.com', 'ORD007', 0),
  ('user8@example.com', 'ORD008', 0),
  ('user9@example.com', 'ORD009', 1),
  ('user10@example.com', 'ORD010', 1);



select * from shopify_transactions;
select * from wordpress_profiles;

SELECT *
FROM shopify_transactions
WHERE email = 'user1@example.com' AND order_number = 'ORD001';

SELECT COUNT(*) AS pairing_exists
FROM shopify_transactions
WHERE email = 'user1@example.com' AND order_number = 'ORD001';

UPDATE wordpress_profiles
SET submitted = 1
WHERE id = 1;


-- Additional logic to manage profile publishing and error handling
DELIMITER $$
CREATE PROCEDURE ManageProfilePublishing(IN userEmail VARCHAR(255), IN userOrderNumber VARCHAR(255))
BEGIN
  DECLARE isOrderValid TINYINT;
  DECLARE isEmailMatching TINYINT;
  DECLARE isPaid TINYINT;
  
  -- Check if the order id exists in the shopify_transactions table
  SELECT COUNT(*) INTO isOrderValid
  FROM shopify_transactions
  WHERE order_number = userOrderNumber;
  
  IF isOrderValid = 0 THEN
    -- Order id does not exist, display an error message
    SELECT "That is not a valid order #. Please check it." AS message;
  ELSE
    -- Order id exists, check if the email matches
    SELECT COUNT(*) INTO isEmailMatching
    FROM shopify_transactions
    WHERE email = userEmail AND order_number = userOrderNumber;
    
    IF isEmailMatching = 0 THEN
      -- Email does not match, display a message
      SELECT "We have that order number, but it is not associated with that email address. Please check both." AS message;
    ELSE
      -- Both order id and email match, check if the user has paid
      SELECT paid INTO isPaid
      FROM shopify_transactions
      WHERE email = userEmail AND order_number = userOrderNumber;
      
      IF isPaid = 0 THEN
        -- User has not paid, display a message to complete the payment
        SELECT "Please complete the payment to publish the profile." AS message;
      ELSE
        -- User has paid, update the published status
        UPDATE wordpress_profiles
        SET submitted = 1, published = 1
        WHERE email = userEmail AND order_number = userOrderNumber;
        
        SELECT "Profile published successfully." AS message;
      END IF;
    END IF;
  END IF;
  
END$$
DELIMITER ;

-- Example usage of the ManageProfilePublishing procedure
CALL ManageProfilePublishing('user0@example.com', 'ORD001');


drop procedure ManageProfilePublishing;

Select * from Wordpress_profile;
drop table Wordpress_profile;

###Logic for orderNumber
SET @start_number = (SELECT IFNULL(MAX(CAST(SUBSTRING_INDEX(orderNumber, '-', -1) AS UNSIGNED)), 0) + 1 FROM Wordpress_profile WHERE orderNumber LIKE '#S-%');

SET SQL_SAFE_UPDATES = 0;

UPDATE Wordpress_profile
SET orderNumber = CONCAT('#S-', @start_number := @start_number + 1)
WHERE orderNumber = '' AND orderNumber NOT LIKE '#S-%';

SET SQL_SAFE_UPDATES = 1;


ALTER TABLE Wordpress_profile
ADD PRIMARY KEY (orderNumber(65535));

ALTER TABLE Wordpress_profile
ADD id INT AUTO_INCREMENT PRIMARY KEY;



DESCRIBE Wordpress_profile;
SELECT CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE table_schema = 'mock_data'
AND table_name = 'Wordpress_profile'
AND column_name = 'orderNumber';






