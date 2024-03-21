-- creates a stored procedure ComputeAverageScore that computes the average score for a student
DROP PROCEDURE IF EXISTS  ComputeAverageScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    INSERT INTO average_scores (user_id, average_score)
    VALUES (p_user_id, avg_score)
    ON DUPLICATE KEY UPDATE average_score = avg_score;

END$$

DELIMITER ;
