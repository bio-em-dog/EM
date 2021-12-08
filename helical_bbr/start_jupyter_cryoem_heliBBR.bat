chcp 65001
call %USERPROFILE%\anaconda3\Scripts\activate.bat cryoem_heliBBR
python %USERPROFILE%\anaconda3\envs\cryoem_heliBBR\Scripts\jupyter-notebook-script.py C:\Code\EM\helical_bbr\
:: --port 48665 --ip 192.168.1.107
pause & exit