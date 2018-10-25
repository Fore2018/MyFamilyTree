<?php
if (!defined('puyuetian'))
    exit('403');

if ($_G['USER']['ID'] == 1 && !$_G['TABLE']['CLAN']) {
    $query = <<<EOF
    CREATE TABLE `{$_G['MYSQL']['PREFIX']}clan` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `clanname` TEXT,
        `cradle` TEXT,
        `locked` TINYINT(1),
        `introduction` TEXT,
        PRIMARY KEY (`id`)
    ) ENGINE = MyISAM CHARSET = utf8
EOF;
    mysql_query($query);
}
