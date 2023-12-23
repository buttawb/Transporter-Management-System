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
-- Table structure for table `dashboard_vehiclemaker`
--

CREATE TABLE `dashboard_vehiclemaker` (
  `VMid` int(11) NOT NULL,
  `VMNAME` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dashboard_vehiclemaker`
--

INSERT INTO `dashboard_vehiclemaker` (`VMid`, `VMNAME`) VALUES
(1, 'DAEWOO'),
(2, 'FAW'),
(3, 'NISSAN'),
(4, 'ISUZU'),
(9, 'Unknown'),
(100, 'Unknown Maker');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dashboard_vehiclemaker`
--
ALTER TABLE `dashboard_vehiclemaker`
  ADD PRIMARY KEY (`VMid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dashboard_vehiclemaker`
--
ALTER TABLE `dashboard_vehiclemaker`
  MODIFY `VMid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
