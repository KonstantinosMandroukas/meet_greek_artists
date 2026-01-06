-- SQL script to normalize artist names across tables

UPDATE `artist_info` SET `Name` = 'Dionisys Savvopoylos' WHERE `Name` = 'Dionisys Savopoulos';
UPDATE `artists` SET `Singers` = 'Dionisys Savvopoylos' WHERE `Singers` = 'Dionisys Savopoulos';
UPDATE `artist_info` SET `Name` = 'Viki Mosxolioy' WHERE `Name` = 'Viki Mosxoliou';
UPDATE `artists` SET `Singers` = 'Viki Mosxolioy' WHERE `Singers` = 'Viki Mosxoliou';
UPDATE `artist_info` SET `Name` = 'Giorgos Sampanis' WHERE `Name` = 'Giorgos Sabanis';
UPDATE `artists` SET `Singers` = 'Giorgos Sampanis' WHERE `Singers` = 'Giorgos Sabanis';
UPDATE `artist_info` SET `Name` = 'Lavrentis Machairitsas' WHERE `Name` = 'Lavredis Maxairitsas';
UPDATE `artists` SET `Singers` = 'Lavrentis Machairitsas' WHERE `Singers` = 'Lavredis Maxairitsas';
UPDATE `artist_info` SET `Name` = 'Maria Farandouri' WHERE `Name` = 'Maria Farantouri';
UPDATE `artists` SET `Singers` = 'Maria Farandouri' WHERE `Singers` = 'Maria Farantouri';
UPDATE `artist_info` SET `Name` = 'Giorgos Ntalaras' WHERE `Name` = 'Giorgos Dalaras';
UPDATE `artists` SET `Singers` = 'Giorgos Ntalaras' WHERE `Singers` = 'Giorgos Dalaras';
UPDATE `artist_info` SET `Name` = 'Michalis Hatzigiannis' WHERE `Name` = 'Mixalis Hatziganns';
UPDATE `artists` SET `Singers` = 'Michalis Hatzigiannis' WHERE `Singers` = 'Mixalis Hatziganns';
UPDATE `artist_info` SET `Name` = 'Lavrentis Machairitsas' WHERE `Name` = 'Lavredis Machairitsas';
UPDATE `artists` SET `Singers` = 'Lavrentis Machairitsas' WHERE `Singers` = 'Lavredis Machairitsas';
UPDATE `artist_search` SET `FirstName` = 'Dionisys', `LastName` = 'Savvopoylos' WHERE `FirstName` = 'Dionisys' AND `LastName` = 'Savopoulos';
UPDATE `artist_search` SET `FirstName` = 'Viki', `LastName` = 'Mosxolioy' WHERE `FirstName` = 'Viki' AND `LastName` = 'Mosxoliou';
UPDATE `artist_search` SET `FirstName` = 'Giorgos', `LastName` = 'Sampanis' WHERE `FirstName` = 'Giorgos' AND `LastName` = 'Sabanis';
UPDATE `artist_search` SET `FirstName` = 'Lavrentis', `LastName` = 'Machairitsas' WHERE `FirstName` = 'Lavredis' AND `LastName` = 'Maxairitsas';
UPDATE `artist_search` SET `FirstName` = 'Maria', `LastName` = 'Farandouri' WHERE `FirstName` = 'Maria' AND `LastName` = 'Farantouri';
UPDATE `artist_search` SET `FirstName` = 'Giorgos', `LastName` = 'Ntalaras' WHERE `FirstName` = 'Giorgos' AND `LastName` = 'Dalaras';
UPDATE `artist_search` SET `FirstName` = 'Michalis', `LastName` = 'Hatzigiannis' WHERE `FirstName` = 'Mixalis' AND `LastName` = 'Hatziganns';
UPDATE `artist_search` SET `FirstName` = 'Lavrentis', `LastName` = 'Machairitsas' WHERE `FirstName` = 'Lavredis' AND `LastName` = 'Machairitsas';
