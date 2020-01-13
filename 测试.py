from bs4 import BeautifulSoup as bs

a = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="renderer" content="webkit">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="keywords" content="内乡宝天曼峡谷漂流景区开漂公告,内乡县政府,内乡县人民政府">
	<meta name="description" content="内乡县位于河南省西南部，南阳盆地西缘。东接镇平，南连邓州，西邻淅川、西峡，北依嵩县、南召。地形呈南北条状，南北长85公里，东西宽54公里，总面积2465平 方公里，耕地面积76万亩。全县辖16个乡镇289个行政村和8个居民委员会，3840个村民小组，总人口63万人。">
	<title>内乡宝天曼峡谷漂流景区开漂公告-内乡县人民政府</title>
	<link rel="stylesheet" type="text/css" href="http://static.neixiangxian.gov.cn/css/reset.css"/>
	<link rel="stylesheet" type="text/css" href="http://static.neixiangxian.gov.cn/css/detail.css"/>
	<script src="http://static.neixiangxian.gov.cn/js/jquery.min.js" type="text/javascript" charset="utf-8"></script>
	<style>
		#my-video{
			height: auto !important;
		}
		.my-player .my-video-dimensions{
			height: auto !important;
		}
	</style>
</head>
<body>
<!--header开始-->
<script src="http://static.neixiangxian.gov.cn/js/top.js"></script>
<!--header开始-->
<div class="wrapper">
	<div class="width1000 containBox">
		<P class="detailTitle">首页  > 公示公告</P>
		<div class="conBox clearfix">
			<h1 class="title">内乡宝天曼峡谷漂流景区开漂公告</h1>
			<p class="detailTxt">
				<a href="/">内乡政府门户网站&nbsp www.neixiangxian.gov.cn</a>
				&nbsp&nbsp<span>2018-04-19 17:32:17</span>&nbsp&nbsp
				<span>来源：内乡县政府网站</span>
			</p>
			<div class="contentBox">
				<p class="MsoNormal" style="text-indent:32.1500pt;mso-char-indent-count:2.0000;"><img src="http://file.neixiangxian.gov.cn/attached/20180419/20180419173149_594.jpg" alt="8E6ABF5A@A5E2F63D" style="max-width:100%;"></p><p class="MsoNormal" style="text-indent:32.1500pt;mso-char-indent-count:2.0000;"><b><span style="font-family: 宋体; font-size: 16pt;"><font face="宋体">内乡宝天曼峡谷漂流兹定于</font>2018<font face="宋体">年</font><font face="Calibri">5</font><font face="宋体">月</font><font face="Calibri">1</font><font face="宋体">日正式对外开漂运营，热诚欢迎社会各界新老朋友前来激情漂流，体验大自然赋予的鬼斧神工，也给您炎热夏季开一个好兆头。给您一天时间，让你重返快乐童年！</font></span></b></p><p class="MsoNormal" style="text-indent:32.1500pt;mso-char-indent-count:2.0000;"><b><span style="font-family: 宋体; font-size: 16pt;"><font face="宋体">详情请咨询：</font>13733127888 &nbsp;&nbsp;&nbsp;0377<font face="宋体">—</font><font face="Calibri">65157888</font></span></b></p><p class="MsoNormal" style="text-indent:32.1500pt;mso-char-indent-count:2.0000;"><b style="text-indent: 16.05pt;"><span style="font-family: 宋体; font-size: 16pt;">特此公告！</span></b></p><p class="MsoNormal"><b><span style="font-family: 宋体; font-size: 16pt;">&nbsp;</span></b></p><p class="MsoNormal"><b><span style="font-family: 宋体; font-size: 16pt;">&nbsp;</span></b></p><p class="MsoNormal" align="right" style="text-align:right;"><b><span style="font-family: 宋体; font-size: 16pt;">内乡宝天曼峡谷漂流有限公司</span></b><b><span style="font-family: 宋体; font-size: 16pt;"><o:p></o:p></span></b></p><p class="MsoNormal" align="right" style="margin-right:16.0000pt;text-align:right;"><b><span style="font-family: 宋体; font-size: 16pt;">二〇一八年四月十九日</span></b><b><span style="font-family: 宋体; font-size: 16pt;"><o:p></o:p></span></b></p><p><br></p> 
			</div>
			<P class="zrEditor">责任编辑：管理员</P>
			<div class="clearfix sharebox fr">
				<span class="fl">分享：</span>
				<div class="bdsharebuttonbox fl">
					<a href="#" class="bds_more" data-cmd="more"></a>
					<a href="#" target='_blank' class="bds_qzone bdkj" data-cmd="qzone" title="分享到QQ空间"></a>
					<a href="#" target='_blank' class="bds_weixin bdwx" data-cmd="weixin" title="分享到微信"></a>
					<a href="#" target='_blank' class="bds_tsina bdwb" data-cmd="tsina" title="分享到新浪微博"></a>
					<a href="#" target='_blank' class="bds_sqq bdqq" data-cmd="sqq" title="分享到QQ好友"></a>
				</div>
				<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://static.neixiangxian.gov.cn/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
			</div>
		</div>
	</div>
</div>
<!--footer开始-->
<script src="http://static.neixiangxian.gov.cn/js/footer.js"></script>
<!--footer结束-->
<script src="http://static.neixiangxian.gov.cn/js/common.js"></script>
<script src="http://static.neixiangxian.gov.cn/static/api/js/share.js?v=89860593.js?cdnversion=417672"></script>
</body>
</html>
'''

soup = bs(a, 'lxml')
b = soup.select('span:nth-of-type(2)')
print(b)