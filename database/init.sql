CREATE DATABASE IF NOT EXISTS IXPlus;
USE IXPlus;
#
# TABLE STRUCTURE FOR: PIDSegmentMappings
#

CREATE TABLE `PIDSegmentMappings` (
  `PID` varchar(255) NOT NULL,
  `segmentID` varchar(255) NOT NULL,
  `count` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`PID`,`segmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

