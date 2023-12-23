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
-- Table structure for table `dashboard_company`
--

CREATE TABLE `dashboard_company` (
  `cid` int(11) NOT NULL,
  `cabb` varchar(10) NOT NULL,
  `cname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dashboard_company`
--

INSERT INTO `dashboard_company` (`cid`, `cabb`, `cname`) VALUES
(1, 'TPPL', 'Total Parco Pakistan Limited'),
(2, 'TPPL MHK', 'Total Parco Pakistan Limited MHK'),
(3, 'TPPL MCH', 'Total Parco Pakistan Limited MCH');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dashboard_company`
--
ALTER TABLE `dashboard_company`
  ADD PRIMARY KEY (`cid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dashboard_company`
--
ALTER TABLE `dashboard_company`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
