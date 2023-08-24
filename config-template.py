class Config:
	def __init__(self):
		self.domain = "" # 部署CodeRunner-Plugin的域名或ip,要求协议完整eg.https://example.com or http://example.com
		self.proxydomain = "" # CodeRunner-Plugin 的代理服务器域名或ip，由于vercel域名或ip可能被墙，代码或图片在国内无法下载，若不需要代理则与self.domain内容相同
		self.dbname = "Cluster0" # mongodb数据库名称,在mongodb官网注册后会赠送一个免费数据库
		self.CORS = False # 是否开启CORS，开启则需要Referer与self.domain或self.proxydomain相同才能访问
		self.api_url = "" # 短域名api服务器地址
		#这里提供一个测试的地址，不保证稳定性与速度
# api_url : http://7dk1cvezn.mghost.site/api.php
# accesskey : aB3$gH8*jK6#mN1@pQ4&rT7%wZ0^cF5(iJ9)lO2!uV6*yB0#dG3&hJ8(kM1@oP4&rS7%vY0^zC5
