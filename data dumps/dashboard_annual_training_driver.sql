-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 27, 2023 at 01:52 PM
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
-- Database: `HGGC_NEW`
--

--
-- Dumping data for table `dashboard_annual_training_driver`
--

INSERT INTO `dashboard_annual_training_driver` (`id`, `user_id`, `train1_completed_date`, `train2_completed_date`, `train3_completed_date`, `train4_completed_date`, `train5_completed_date`, `train6_completed_date`, `train7_completed_date`, `train8_completed_date`, `train9_completed_date`, `train10_completed_date`, `train11_completed_date`, `train12_completed_date`) VALUES
(1, 16, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-11', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(2, 17, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-09', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(3, 19, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-20', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(4, 20, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-13', '2023-08-06', '2023-09-01', '0000-00-00', '0000-00-00'),
(5, 21, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-16', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(6, 8, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-11', '2023-08-08', '2023-09-01', '0000-00-00', '0000-00-00'),
(7, 24, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-11', '2023-08-08', '2023-09-01', '0000-00-00', '0000-00-00'),
(8, 7, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-10', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(9, 59, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-10', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(10, 26, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-09', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(11, 27, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-11', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(12, 28, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-11', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(13, 14, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-10', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(14, 29, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-13', '2023-08-10', '2023-09-01', '0000-00-00', '0000-00-00'),
(15, 30, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-14', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(16, 33, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-07', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(17, 34, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-08', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(18, 35, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-14', '2023-08-02', '2023-09-01', '0000-00-00', '0000-00-00'),
(19, 36, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-10', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(20, 38, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-07', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(21, 37, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-08', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(22, 39, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-08', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(23, 41, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-06', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(24, 23, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-07', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(25, 43, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-14', '2023-08-02', '2023-09-01', '0000-00-00', '0000-00-00'),
(26, 44, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-10', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(27, 46, '2023-10-01', '2023-01-06', '2023-02-06', '2023-03-01', '2023-04-03', '2023-05-03', '2023-06-02', '2023-07-11', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(28, 52, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-14', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(29, 53, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-18', '2023-08-07', '2023-09-01', '0000-00-00', '0000-00-00'),
(30, 57, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-11', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(31, 56, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-17', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(32, 3, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-16', '2023-08-11', '2023-09-01', '0000-00-00', '0000-00-00'),
(33, 58, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-18', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(34, 25, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-13', '2023-08-19', '2023-09-01', '0000-00-00', '0000-00-00'),
(35, 60, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-04', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(36, 61, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-11', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(37, 66, '2023-10-01', '2023-01-09', '2023-02-01', '2023-03-07', '2023-04-08', '2023-05-13', '2023-06-03', '2023-07-12', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(38, 64, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-08', '2023-08-14', '2023-09-01', '0000-00-00', '0000-00-00'),
(39, 65, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-14', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(40, 1, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-05', '2023-08-02', '2023-09-01', '0000-00-00', '0000-00-00'),
(41, 68, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-21', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(42, 67, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-12', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(43, 69, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-20', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(44, 70, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-02', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(45, 9, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-15', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(46, 71, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-12', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(47, 72, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-12', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(48, 73, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(49, 74, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(50, 75, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(51, 76, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-10', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(52, 78, '2023-10-01', '2023-01-11', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-06', '2023-06-07', '2023-07-07', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(53, 79, '2023-10-01', '2023-01-04', '2023-02-07', '2023-03-10', '2023-04-19', '2023-05-05', '2023-06-07', '2023-07-15', '2023-08-06', '2023-09-01', '0000-00-00', '0000-00-00'),
(54, 11, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-20', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(55, 80, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-06', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(56, 81, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-03', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(57, 82, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-19', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(58, 83, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-03', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(59, 84, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(60, 85, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(61, 86, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(62, 87, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-07', '2023-09-01', '0000-00-00', '0000-00-00'),
(63, 89, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-04', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(64, 90, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-21', '2023-08-11', '2023-09-01', '0000-00-00', '0000-00-00'),
(65, 91, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(66, 92, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-15', '2023-08-06', '2023-09-01', '0000-00-00', '0000-00-00'),
(67, 93, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-06', '2023-09-01', '0000-00-00', '0000-00-00'),
(68, 94, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-14', '2023-08-08', '2023-09-01', '0000-00-00', '0000-00-00'),
(69, 10, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-10', '2023-08-08', '2023-09-01', '0000-00-00', '0000-00-00'),
(70, 95, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-05', '2023-08-02', '2023-09-01', '0000-00-00', '0000-00-00'),
(71, 96, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-07', '2023-09-01', '0000-00-00', '0000-00-00'),
(72, 97, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-10', '2023-08-09', '2023-09-01', '0000-00-00', '0000-00-00'),
(73, 99, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-07', '2023-08-13', '2023-09-01', '0000-00-00', '0000-00-00'),
(74, 98, '2023-10-01', '2023-01-07', '2023-02-03', '2023-03-03', '2023-04-06', '2023-05-02', '2023-06-08', '2023-07-13', '2023-08-05', '2023-09-01', '0000-00-00', '0000-00-00'),
(75, 45, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-10', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(76, 5, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-07', '2023-08-08', '2023-09-01', '0000-00-00', '0000-00-00'),
(77, 101, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-17', '2023-08-06', '2023-09-01', '0000-00-00', '0000-00-00'),
(78, 102, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(79, 103, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(80, 104, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(81, 107, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '2023-07-13', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(82, 108, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(83, 13, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(84, 18, '2023-10-01', '2023-01-02', '2023-02-04', '2023-03-04', '2023-04-01', '2023-05-04', '2023-06-05', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(85, 31, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(86, 32, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(87, 47, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-03', '2023-08-10', '2023-09-01', '0000-00-00', '0000-00-00'),
(88, 48, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-12', '2023-08-01', '2023-09-01', '0000-00-00', '0000-00-00'),
(89, 49, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(90, 50, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-03', '2023-08-02', '2023-09-01', '0000-00-00', '0000-00-00'),
(91, 51, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(92, 54, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-12', '2023-08-03', '2023-09-01', '0000-00-00', '0000-00-00'),
(93, 55, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00'),
(94, 105, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '2023-07-15', '2023-08-04', '2023-09-01', '0000-00-00', '0000-00-00'),
(95, 106, '2023-10-01', '2023-01-04', '2023-02-02', '2023-03-02', '2023-04-04', '2023-05-05', '2023-06-06', '0000-00-00', '0000-00-00', '2023-09-01', '0000-00-00', '0000-00-00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;