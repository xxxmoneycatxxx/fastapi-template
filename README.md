```bash
# 构建虚拟环境，在当前目录运行以下命令（需要python3.3或以上版本）
# 常用参数： 
# --clear  重建已有虚拟环境
# windows
python -m evnv ./venv
# mac | linux
python3 -m venv ./venv

# 激活虚拟环境
# windows
./venv/Scripts/activate.bat
# mac | linux
source bin/activate

# 包管理
# 生成 requirements.txt
pip freeze > requirements.txt
# 安装 requirments.txt
pip install -r requirements.txt


```