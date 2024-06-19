-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_out_info`
--

DROP TABLE IF EXISTS `patient_out_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_out_info` (
  `Patients_Out_ID` varchar(30) NOT NULL,
  `Patients_First_Name` varchar(30) DEFAULT NULL,
  `Surgery_Number` int DEFAULT NULL,
  `Bill_Number` int DEFAULT NULL,
  `Dead_Or_Alive` varchar(6) DEFAULT NULL,
  `Total_Cost` int DEFAULT NULL,
  PRIMARY KEY (`Patients_Out_ID`),
  KEY `Surgery_Number` (`Surgery_Number`),
  KEY `Bill_Number` (`Bill_Number`),
  CONSTRAINT `patient_out_info_ibfk_1` FOREIGN KEY (`Surgery_Number`) REFERENCES `patient_in_info` (`Surgery_Number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `patient_out_info_ibfk_2` FOREIGN KEY (`Bill_Number`) REFERENCES `billing_info` (`Bill_Number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_out_info`
--

LOCK TABLES `patient_out_info` WRITE;
/*!40000 ALTER TABLE `patient_out_info` DISABLE KEYS */;
INSERT INTO `patient_out_info` VALUES ('415627_AE','davitya',123456,234567,'alive',645),('66662_GY','vidya',878299,999330,'alive',3049);
/*!40000 ALTER TABLE `patient_out_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 18:43:31
