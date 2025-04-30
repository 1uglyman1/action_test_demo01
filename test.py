import subprocess
import os

try:
    # 克隆 GitHub 仓库
    result = subprocess.run(["git", "clone", "https://github.com/shmilylty/OneForAll.git"], capture_output=True, text=True, check=True)
    print("仓库克隆成功")
except subprocess.CalledProcessError as e:
    print(f"克隆仓库时出错: {e.stderr}")

# 根据操作系统选择合适的命令查看目录内容
if os.name == "nt":  # Windows 系统
    command = "dir"
else:  # Linux 或 macOS 系统
    command = "ls"

try:
    # 第一次查看目录内容
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    print("第一次查看目录内容:")
    print(result.stdout)
    # 第二次查看目录内容
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    print("第二次查看目录内容:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"执行查看目录命令时出错: {e.stderr}")
    
