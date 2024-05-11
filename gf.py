import os
path = r'C:\Users\user\Desktop\Иовлев Марк\11.05.24\fdf'
projectname = 'fdf'
folders = \
['input' ,
'output' ,
'scenes' ,
'assets']

fullPath = os. path. join (path, projectname)
os. mkdir(fullPath)