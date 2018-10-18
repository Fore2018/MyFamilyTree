<?php
if (!defined('puyuetian')) {
    exit('403');
}

// 去除标题连字符
$_G['SET']['EMBED_HEADMARKS'] .= <<<EOF
<script>
    document.title = document.title.replace(/\s-$/, "");
</script>
EOF;

// 修改网站名
$_G['SET']['WEBNAME'] = $_G['SET']['APP_QUELAAG_FURYSWORD_WEBNAME'];
$_G['SET']['WEBTITLE'] = $_G['SET']['APP_QUELAAG_FURYSWORD_WEBTITLE'];

// 添加切换版式选项
$_G['SET']['FOOTERHTMLCODE'] .= <<<EOF
<a href="https://www.linkfire.org/">电脑版</a>
<a href="https://m.linkfire.org/">手机版</a>
<a target="_blank" href="mailto:admin@linkfire.org">联系站长</a>
EOF;

// 修改一些样式
$_G['SET']['EMBED_HEAD'] .= <<<EOF
<style type="text/css">
.readcontent {text-align: justify;}
p {text-align: justify;}
pre {overflow: auto; white-space: pre !important; width: 100% !important; word-wrap: break-word;}
.fly-footer a{padding:0 6px; font-weight: 400; color: #737573;}
</style>
EOF;
