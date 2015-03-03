-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2015 年 03 月 03 日 10:42
-- 服务器版本: 5.5.23
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_liuhb`
--

-- --------------------------------------------------------

--
-- 表的结构 `menu`
--

CREATE TABLE IF NOT EXISTS `menu` (
  `nid` int(10) NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `make_time` int(11) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `comment` text,
  `category_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11 ;

--
-- 转存表中的数据 `menu`
--

INSERT INTO `menu` (`nid`, `dish_name`, `price`, `make_time`, `image`, `comment`, `category_id`) VALUES
(1, 'salsa', 15, 10, 'salsa.jpg', NULL, 135),
(2, '蒸饺', 20, 10, 'dumpling.JPG', NULL, 133),
(3, '永和大王', 25, 20, 'yonghe.JPG', NULL, 1223),
(4, '兰州拉面', 15, 10, 'lamian.JPG', NULL, 133),
(5, '清蒸鱼', 48, 30, 'fish.jpg', NULL, 5),
(6, '武夷茶', 35, 10, 'wuyicha.jpg', NULL, 1029),
(7, '乐美芝蛋糕', 10, 0, 'lemeizhi.jpg', NULL, 41),
(8, '卡麦珑披萨', 15, 10, 'pisa.jpg', NULL, 137),
(9, '汇隆海鲜', 138, 40, 'haixian.jpg', NULL, 5),
(10, '馄饨', 11, 10, 'huntun.jpg', NULL, 133);

-- --------------------------------------------------------

--
-- 表的结构 `menu_sort`
--

CREATE TABLE IF NOT EXISTS `menu_sort` (
  `uid` int(10) NOT NULL AUTO_INCREMENT,
  `category` varchar(20) NOT NULL,
  `info` text,
  `category_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- 转存表中的数据 `menu_sort`
--

INSERT INTO `menu_sort` (`uid`, `category`, `info`, `category_id`) VALUES
(1, '全部', NULL, 1),
(2, '快餐', NULL, 2),
(3, '中餐', NULL, 4),
(4, '西餐', NULL, 8),
(5, '料理', NULL, 16),
(6, '糕点', NULL, 32),
(7, '汤类', NULL, 64),
(8, '面食', NULL, 128),
(9, '饮品', NULL, 1024);

-- --------------------------------------------------------

--
-- 表的结构 `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `session_id` varchar(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `uid` int(5) NOT NULL AUTO_INCREMENT,
  `user` varchar(20) NOT NULL,
  `passwd` varchar(10) NOT NULL,
  `nick_name` varchar(20) DEFAULT NULL,
  `extend` text,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`uid`, `user`, `passwd`, `nick_name`, `extend`) VALUES
(1, 'root', '9e85481845', '', NULL),
(2, 'test', '832627b4f6', 'nick_test', NULL),
(3, 'sith', 'f76670ceba', 'sith_y', NULL);
