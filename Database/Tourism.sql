-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2022 at 06:51 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trs`
--
CREATE DATABASE IF NOT EXISTS `trs` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `trs`;

-- --------------------------------------------------------

--
-- Table structure for table `customer_query`
--

CREATE TABLE `customer_query` (
  `customer_name` varchar(20) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_number` varchar(11) NOT NULL,
  `customer_message` varchar(100) NOT NULL,
  `employee_reply` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_query`
--

INSERT INTO `customer_query` (`customer_name`, `customer_email`, `customer_number`, `customer_message`, `employee_reply`) VALUES
('SANKET', 'sanket@gmail.com', '7774096101', 'Hello Rohit', ''),
('sachin', 'sk@gmail.com', '7774096122', 'hello', '');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_booking`
--

CREATE TABLE `hotel_booking` (
  `customer_name` varchar(40) NOT NULL,
  `customer_email` varchar(40) NOT NULL,
  `customer_number` varchar(11) NOT NULL,
  `room_booked` varchar(3) NOT NULL,
  `no_of_people` varchar(3) NOT NULL,
  `hotel_checkin` date NOT NULL,
  `hotel_checkout` int(11) NOT NULL,
  `date_booked` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_booking`
--

INSERT INTO `hotel_booking` (`customer_name`, `customer_email`, `customer_number`, `room_booked`, `no_of_people`, `hotel_checkin`, `hotel_checkout`, `date_booked`) VALUES
('[value-1]', '[value-2]', '[value-3]', '[va', '[va', '0000-00-00', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tourism_plan`
--

CREATE TABLE `tourism_plan` (
  `plan_id` int(20) NOT NULL,
  `plan_name` varchar(40) DEFAULT NULL,
  `plan_state` varchar(30) DEFAULT NULL,
  `plan_details` varchar(200) DEFAULT NULL,
  `plan_duration` varchar(20) DEFAULT NULL,
  `plan_amount` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tourism_plan`
--

INSERT INTO `tourism_plan` (`plan_id`, `plan_name`, `plan_state`, `plan_details`, `plan_duration`, `plan_amount`) VALUES
(101, 'Ganja', 'Maharashtra', 'Pune 2 Days\nMumbai 3 Days\nNagpur 2 Days		', '8 Days', 12000);

-- --------------------------------------------------------

--
-- Table structure for table `tour_registration`
--

CREATE TABLE `tour_registration` (
  `customer_name` varchar(30) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_phone` varchar(12) NOT NULL,
  `customer_address` varchar(100) NOT NULL,
  `customer_gender` varchar(8) NOT NULL,
  `customer_country` varchar(20) NOT NULL,
  `customer_state` varchar(20) NOT NULL,
  `customer_passport` varchar(10) NOT NULL,
  `customer_selected_package` varchar(16) NOT NULL,
  `trip_startdate` date NOT NULL,
  `trip_enddate` date NOT NULL,
  `trip_amt` float NOT NULL,
  `customer_payment` float NOT NULL,
  `trip_status` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tour_registration`
--

INSERT INTO `tour_registration` (`customer_name`, `customer_email`, `customer_phone`, `customer_address`, `customer_gender`, `customer_country`, `customer_state`, `customer_passport`, `customer_selected_package`, `trip_startdate`, `trip_enddate`, `trip_amt`, `customer_payment`, `trip_status`) VALUES
('value-1', 'value-2', 'value-3', '[value-4]', '[value-5', '[value-6]', '[value-7]', '[value-81]', '[value-9]', '0000-00-00', '0000-00-00', 0, 0, '[value-14]'),
('[value-1]', '[value-2]', '[value-3]', '[value-4]', '[value-5', '[value-6]', '[value-7]', '[value-8]', '[value-9]', '0000-00-00', '0000-00-00', 0, 0, '[value-14]');

-- --------------------------------------------------------

--
-- Table structure for table `trs_customer_login`
--

CREATE TABLE `trs_customer_login` (
  `customer_userid` varchar(40) NOT NULL,
  `customer_userpw` varchar(20) NOT NULL,
  `customer_email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trs_customer_login`
--

INSERT INTO `trs_customer_login` (`customer_userid`, `customer_userpw`, `customer_email`) VALUES
('surajgiri974', 'A', 'surajgiri974@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `trs_employee`
--

CREATE TABLE `trs_employee` (
  `emp_id` varchar(20) NOT NULL,
  `emp_name` varchar(50) NOT NULL,
  `emp_address` varchar(100) NOT NULL,
  `emp_dob` date NOT NULL,
  `emp_mobno` bigint(11) NOT NULL,
  `emp_sal` float NOT NULL,
  `emp_saltax` float NOT NULL,
  `emp_netsal` float NOT NULL,
  `emp_type` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `trs_login`
--

CREATE TABLE `trs_login` (
  `trs_id` varchar(20) NOT NULL,
  `trs_pw` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trs_login`
--

INSERT INTO `trs_login` (`trs_id`, `trs_pw`) VALUES
('suraj@gmail.com', 'suraj');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_registration`
--

CREATE TABLE `vehicle_registration` (
  `customer_name` varchar(50) NOT NULL,
  `customer_license` varchar(16) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_phone` varchar(11) NOT NULL,
  `customer_pickup` date NOT NULL,
  `customer_drop` date NOT NULL,
  `vehicle_type` varchar(20) NOT NULL,
  `city` varchar(15) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_registration`
--

INSERT INTO `vehicle_registration` (`customer_name`, `customer_license`, `customer_email`, `customer_phone`, `customer_pickup`, `customer_drop`, `vehicle_type`, `city`, `amount`) VALUES
('Suraj Giri', 'MH12202022187318', 'surajgiri@gmail.com', '8308149964', '2022-08-24', '2022-08-31', 'Two Wheeler', 'Pune', 640),
('[value-1]', '[value-2]', '[value-3]', '[value-4]', '0000-00-00', '0000-00-00', '[value-7]', '[value-8]', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_query`
--
ALTER TABLE `customer_query`
  ADD PRIMARY KEY (`customer_number`);

--
-- Indexes for table `tourism_plan`
--
ALTER TABLE `tourism_plan`
  ADD PRIMARY KEY (`plan_id`);

--
-- Indexes for table `tour_registration`
--
ALTER TABLE `tour_registration`
  ADD PRIMARY KEY (`customer_passport`);

--
-- Indexes for table `trs_customer_login`
--
ALTER TABLE `trs_customer_login`
  ADD PRIMARY KEY (`customer_userid`);

--
-- Indexes for table `trs_employee`
--
ALTER TABLE `trs_employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `trs_login`
--
ALTER TABLE `trs_login`
  ADD PRIMARY KEY (`trs_id`);

--
-- Indexes for table `vehicle_registration`
--
ALTER TABLE `vehicle_registration`
  ADD PRIMARY KEY (`customer_license`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
