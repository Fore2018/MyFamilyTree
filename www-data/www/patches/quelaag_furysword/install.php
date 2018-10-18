<?php
if (!defined('puyuetian'))
    exit('403');

if ($_G['USER']['ID'] == 1 && !$_G['TABLE']['APP_PUYUETIAN_APPDEMO_TABLE']) {
    mysql_query("CREATE TABLE `{$_G['MYSQL']['PREFIX']}app_puyuetian_appdemo_table` (`id` int(11) NOT NULL AUTO_INCREMENT, `data` text, PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT CHARSET=utf8");
}


exit();
