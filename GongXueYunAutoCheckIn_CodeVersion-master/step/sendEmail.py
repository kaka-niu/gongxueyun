import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from manager.ConfigManager import ConfigManager


def send_email(title, content):
    to_emails = ConfigManager.get("smtp", "to")

    for to_email in to_emails:
        # 设置 MIMEText 对象
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = Header(title, 'utf-8')
        from_header = Header(ConfigManager.get("smtp", "from"), 'utf-8')
        message['From'] = formataddr((from_header.encode(), ConfigManager.get("smtp", "username")))
        message['To'] = to_email

        # 连接到 SMTP 服务器
        with smtplib.SMTP_SSL(ConfigManager.get("smtp", "host"), ConfigManager.get("smtp", "port")) as server:
            # 登录到邮箱账户
            server.login(ConfigManager.get("smtp", "username"), ConfigManager.get("smtp", "password"))
            # 发送邮件
            server.sendmail(ConfigManager.get("smtp", "username"), to_email, message.as_string())
