-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 23, 2023 at 08:25 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HGGC`
--

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_vehicleowner`
--

CREATE TABLE `dashboard_vehicleowner` (
  `VO_id` int(11) NOT NULL,
  `VO_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dashboard_vehicleowner`
--

INSERT INTO `dashboard_vehicleowner` (`VO_id`, `VO_name`) VALUES
(1, 'BANK OF PUNJAB'),
(2, 'BILAL TRADERS'),
(3, 'ORIX LEASING '),
(4, 'BANK AL HABIB SWL'),
(5, 'HAJI GUL ENT'),
(6, 'STANDERD CHARTED'),
(7, 'SITARA P/S'),
(8, 'BANK AL HABIB'),
(9, 'ALLIED BANK SWL'),
(10, 'BURJ BANK'),
(11, 'ALLIED BANK SWL'),
(12, 'BANK AL HABIB KARACHI'),
(13, 'HABIB BANK KARACHI'),
(14, 'MEEZAN BANK'),
(15, 'Salman'),
(100, 'Unknown Owner');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dashboard_vehicleowner`
--
ALTER TABLE `dashboard_vehicleowner`
  ADD PRIMARY KEY (`VO_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dashboard_vehicleowner`
--
ALTER TABLE `dashboard_vehicleowner`
  MODIFY `VO_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
