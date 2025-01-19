
-- ----------------------------------
CREATE SCHEMA `fest_management_system` ;
use `fest_management_system` ;

-- ----------------------------------

-- 1. Fest table:
-- Creation:
CREATE TABLE `fest` (
  `fest_ID` int NOT NULL AUTO_INCREMENT,
  `fest_name` varchar(45) NOT NULL,
  `fest_start_date` date NOT NULL,
  `fest_end_date` date NOT NULL,
  PRIMARY KEY (`fest_ID`),
  UNIQUE KEY `fest_name_UNIQUE` (`fest_name`),
  UNIQUE KEY `fest_start_date_UNIQUE` (`fest_start_date`),
  UNIQUE KEY `fest_end_date_UNIQUE` (`fest_end_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
  
-- -----------------------
-- 2. Team table:
-- Creation:
CREATE TABLE `team` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(45) NOT NULL,
  `team_lead_id` int NOT NULL,
  `fest_id` int NOT NULL,
  `event_id` int NOT NULL,
  PRIMARY KEY (`team_id`),
  UNIQUE KEY `team_name_UNIQUE` (`team_name`),
  UNIQUE KEY `team_lead_id_UNIQUE` (`team_lead_id`),
  UNIQUE KEY `fest_id_UNIQUE` (`fest_id`),
  UNIQUE KEY `event_id_UNIQUE` (`event_id`),
  CONSTRAINT `fest_id` FOREIGN KEY (`fest_id`) REFERENCES `fest` (`fest_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- -----------------------
  
  
-- 3. Event table:
-- Creation:
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(45) NOT NULL,
  `event_price` int NOT NULL,
  `event_venue_id` int NOT NULL,
  `conducting_team_id` int NOT NULL,
  `event_date` date NOT NULL,
  `event_time` time NOT NULL,
  PRIMARY KEY (`event_id`),
  UNIQUE KEY `event_name_UNIQUE` (`event_name`),
  UNIQUE KEY `event_date_UNIQUE` (`event_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


  
-- -----------------------
  
-- 4. Venue table:
-- Creation:
CREATE TABLE `venue` (
  `venue_ID` int NOT NULL AUTO_INCREMENT,
  `venue_name` varchar(45) NOT NULL,
  `capacity` int NOT NULL,
  `block` varchar(45) NOT NULL,
  `floor` int NOT NULL,
  PRIMARY KEY (`venue_ID`),
  UNIQUE KEY `venue_name_UNIQUE` (`venue_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

  
-- -----------------------
  
  
-- 5. Member table:
-- Creation:
CREATE TABLE `member` (
  `memb_id` int NOT NULL AUTO_INCREMENT,
  `memb_name` varchar(45) NOT NULL,
  `memb_phone_num` varchar(45) NOT NULL,
  `memb_srn` varchar(45) NOT NULL,
  `memb_dob` date NOT NULL,
  `team_id` int NOT NULL,
  PRIMARY KEY (`memb_id`),
  UNIQUE KEY `memb_id_UNIQUE` (`memb_id`),
  UNIQUE KEY `memb_name_UNIQUE` (`memb_name`),
  UNIQUE KEY `memb_phone_num_UNIQUE` (`memb_phone_num`),
  UNIQUE KEY `memb_srn_UNIQUE` (`memb_srn`),
  UNIQUE KEY `memb_dob_UNIQUE` (`memb_dob`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- -----------------------
   
-- 6. Participants table:
-- Creation:
CREATE TABLE `participants` (
  `part_id` int NOT NULL AUTO_INCREMENT,
  `part_name` varchar(45) NOT NULL,
  `part_phone_num` varchar(45) NOT NULL,
  `event_id` int NOT NULL,
  `part_dob` date NOT NULL,
  `part_srn` varchar(45) NOT NULL,
  PRIMARY KEY (`part_id`),
  UNIQUE KEY `part_id_UNIQUE` (`part_id`),
  KEY `event_id_idx` (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

  
-- -----------------------

-- 6. User table:
-- Creation: 
CREATE TABLE `user` (
  `user_ID` int NOT NULL AUTO_INCREMENT,
  `user_srn` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `user_role` varchar(45) NOT NULL,
  PRIMARY KEY (`user_ID`),
  UNIQUE KEY `user_srn_UNIQUE` (`user_srn`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`),
  UNIQUE KEY `password_UNIQUE` (`password`),
  UNIQUE KEY `user_role_UNIQUE` (`user_role`),
  CONSTRAINT `user_mem_ID` FOREIGN KEY (`user_ID`) REFERENCES `member` (`memb_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_part_ID` FOREIGN KEY (`user_ID`) REFERENCES `participants` (`part_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- -----------------------

---------------------------
---Trigger to prevent duplicate registrations for the same event
---------------------------
before_participant_insert--
DELIMITER //
CREATE TRIGGER `before_participant_insert` BEFORE INSERT ON `participants`
FOR EACH ROW
BEGIN
  DECLARE registration_count INT;

  -- Check if the participant is already registered for the event
  SELECT COUNT(*) INTO registration_count
  FROM `participants`
  WHERE `event_id` = NEW.`event_id` AND `part_srn` = NEW.`part_srn`;

  -- If the participant is already registered, prevent the insertion
  IF registration_count > 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot register for the same event twice.';
  END IF;
END;
//
DELIMITER ;


---------------------------
---Stored Procedure
--- To limit registrations per person to only three events
---------------------------

DELIMITER //

CREATE PROCEDURE RegisterParticipantForEvent(
    IN part_srn_param VARCHAR(45),
    IN event_id_param INT
)
BEGIN
    DECLARE event_count INT;

    -- Get the current number of events the participant is registered for
    SELECT COUNT(*) INTO event_count
    FROM participants
    WHERE part_srn = part_srn_param;

    -- Check if the participant is already registered for three events
    IF event_count < 3 THEN
        -- Register the participant for the event
        INSERT INTO participants (part_srn, event_id)
        VALUES (part_srn_param, event_id_param);

        SELECT 'Participant registered for the event.' AS Result;
    ELSE
        SELECT 'Participant cannot register for more than three events.' AS Result;
    END IF;
END //

DELIMITER ;before_participant_insertbefore_participant_insert
