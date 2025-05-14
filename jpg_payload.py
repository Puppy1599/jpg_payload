import subprocess
import os
import sys
import shutil

# 获取临时执行路径
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# 拼接 PHP 路径
php_path = os.path.join(base_path, "php-8.4.7-nts-Win32-vs17-x64", "php.exe")
php_script = os.path.join(base_path, "jpg_payload.php")

# 获取命令行参数
args = sys.argv[1:]

# 构建命令并执行
subprocess.call([php_path, php_script] + args)