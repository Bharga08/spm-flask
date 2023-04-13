-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ecom_orders`
--

DROP TABLE IF EXISTS `ecom_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ecom_orders` (
  `ordid` int NOT NULL AUTO_INCREMENT,
  `product` tinytext,
  `cname` varchar(20) DEFAULT NULL,
  `quqntity` tinyint DEFAULT NULL,
  `total` int DEFAULT NULL,
  `dop` date DEFAULT NULL,
  `country` char(20) DEFAULT NULL,
  PRIMARY KEY (`ordid`)
) ENGINE=InnoDB AUTO_INCREMENT=2157450 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ecom_orders`
--

LOCK TABLES `ecom_orders` WRITE;
/*!40000 ALTER TABLE `ecom_orders` DISABLE KEYS */;
INSERT INTO `ecom_orders` VALUES (2157445,'pens','ranjith',10,100,'2019-02-09','US'),(2157446,'laptop','maheshbabu',1,49999,'2020-01-23','IN'),(2157447,'table','kajal',1,1399,'2020-01-23','IN'),(2157448,'speaker','ram',2,1099,'2019-09-10','NETHERLANDS'),(2157449,'pens','raji',5,200,'2016-08-29','US');
/*!40000 ALTER TABLE `ecom_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python`
--

DROP TABLE IF EXISTS `python`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `python` (
  `stdid` int NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT NULL,
  `course` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`stdid`)
) ENGINE=InnoDB AUTO_INCREMENT=206536 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `python`
--

LOCK TABLES `python` WRITE;
/*!40000 ALTER TABLE `python` DISABLE KEYS */;
INSERT INTO `python` VALUES (1,'bhagi','BSC'),(2,'pandu','BBA'),(3,'mastii','BCA'),(4,'sai','BCOM'),(206532,'bhagi','BSC'),(206533,'pandu','BBA'),(206534,'mastii','BCA'),(206535,'sai','BCOM');
/*!40000 ALTER TABLE `python` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-02  0:14:45
