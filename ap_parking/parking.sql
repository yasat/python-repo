-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2019 at 07:22 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parking`
--

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `indno` int(10) NOT NULL,
  `no` varchar(15) NOT NULL,
  `intime` datetime NOT NULL,
  `outtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(3) NOT NULL,
  `amount` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`indno`, `no`, `intime`, `outtime`, `status`, `amount`) VALUES
(1, 'AP84-HY5433', '2019-06-13 10:47:16', '2019-06-13 10:49:17', 'out', 1),
(2, 'AP84-HY5434', '2019-06-13 10:47:54', '2019-06-13 10:50:23', 'out', 1),
(3, 'AP84-HY5433', '2019-06-13 10:49:28', '2019-06-13 10:50:03', 'out', 0),
(4, 'AP05-BH8745', '2019-06-13 11:01:22', '2019-06-13 11:09:23', 'out', 4),
(5, 'AP84-HY5433', '2019-06-13 11:08:48', '2019-06-13 11:08:48', 'in', 0),
(6, 'AP05-BH8745', '2019-06-13 11:11:54', '2019-06-13 11:11:54', 'in', 0),
(7, 'AP67-UY765', '2019-06-13 11:16:31', '2019-06-13 11:17:41', 'out', 1),
(8, 'AP07-AU7656', '2019-06-13 11:19:52', '2019-06-13 11:19:52', 'in', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
