SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


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

INSERT INTO `menu` (`nid`, `dish_name`, `price`, `make_time`, `image`, `comment`, `category_id`) VALUES
(1, 'salsa', 15, 10, 'salsa.jpg', NULL, 1),
(2, '蒸饺', 20, 0, 'dumpling.JPG', NULL, 1),
(3, '永和大王', 25, 30, 'yonghe.JPG', NULL, 1),
(4, '兰州拉面', 15, 10, 'lamian.JPG', NULL, 1),
(5, '清蒸鱼', 48, 30, 'fish.jpg', NULL, 1),
(6, '武夷茶', 35, 15, 'wuyicha.jpg', NULL, 1),
(7, '乐美芝蛋糕', 10, 0, 'lemeizhi.jpg', NULL, 1),
(8, '卡麦珑披萨', 15, 20, 'pisa.jpg', NULL, 1),
(9, '汇隆海鲜', 138, 40, 'haixian.jpg', NULL, 1),
(10, '馄饨', 11, 10, 'huntun.jpg', NULL, 1);

CREATE TABLE IF NOT EXISTS `menu_sort` (
  `uid` int(10) NOT NULL AUTO_INCREMENT,
  `category` varchar(20) NOT NULL,
  `info` text,
  `category_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

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

CREATE TABLE IF NOT EXISTS `user` (
  `uid` int(5) NOT NULL AUTO_INCREMENT,
  `user` varchar(20) NOT NULL,
  `passwd` varchar(10) NOT NULL,
  `nick_name` varchar(20) DEFAULT NULL,
  `extend` text,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

