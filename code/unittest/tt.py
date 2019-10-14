最方便的就是使用pip安装 
pip install uncompyle

uncompyle6 --help 查看帮助 
uncompyle6 models.pyc > models.py 将models.pyc反编译成py文件 
uncompile -o . *.pyc 将当前文件夹中所有的pyc文件反编译成后缀名为.pyc_dis的源文件
