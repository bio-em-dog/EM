# 目录
-AutoHT
    - pyinstaller
      - (pipenv的执行目录)
      - pipfile
    - dec
    - inc
    - dec.py
    - inc.py

# 流程
anaconda
写代码
pyvenv
pyinstaller





## pipenv
https://zhuanlan.zhihu.com/p/57674343


```
cd <path to pyinstaller folder>
#建立虚拟环境
pipenv --python 3.7.11 # 一定要在project dir中执行
# pipenv新建的虚拟环境统一放在`%USERPROFILE%\.virtualenvs`, 在特定目录下运行pipenv shell时,pipenv会自动在虚拟环境目录下搜索以当前目录名称开头的虚拟环境目录.
#进入虚拟环境
pipenv shell
#安装模块
pip install <.py里面用到的模块>


pip install pyperclip
pip install pyautogui==0.9.50
pip install opencv-python

pipenv graph #显示安装的环境
#打包的模块也要安装
pip install pyinstaller
#开始打包
pyinstaller -Fw E:\test\url_crawler.py
```

## pyinstaller

http://c.biancheng.net/view/2690.html


```cmd
:: pipenv prompt
pipenv shell  :: in pyinstaller folder
pyinstaller -D -i "..\icon\dec.ico" "..\dec.py"
pyinstaller -D -i "..\icon\inc.ico" "..\inc.py"
```

-D 单文件夹
-F 单文件
-w 隐藏consel
--icon

## icon
win10 256 128 64 32 16
https://www.reddit.com/r/learnpython/comments/fks3oc/autoscaling_ico_with_pyinstaller/

生成各个大小合一的icon才能在生成后正常显示

注意缩略图有缓存，可以ctrl拖拽一个副本看看，或者删除`%localappdata%/Iconcache.db`

`Imagemagick`命令：  
`convert dec_waifu2x_art_scale_tta_1.png  -define icon:auto-resize=256,64,48,32,16 my_icon.ico`



### 
cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)