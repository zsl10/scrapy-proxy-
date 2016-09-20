CREATE TABLE `dy_proxy` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `ip` varchar(15) NOT NULL COMMENT '服务器ip地址',
  `port` char(4) NOT NULL COMMENT '端口',
  `http_type` varchar(5) DEFAULT NULL COMMENT 'http类型',
  `position` varchar(40) NOT NULL COMMENT '服务器所在地址',
  `speed` double(4,3) NOT NULL COMMENT '速度',
  `connect_time` double(4,3) NOT NULL COMMENT '连接时间',
  `check_time` varchar(40) DEFAULT NULL COMMENT '验证时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
