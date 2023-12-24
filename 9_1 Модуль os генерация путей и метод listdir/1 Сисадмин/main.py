import os

relative_path = os.path.join('..','..', 'access', 'admin.bat')
print(relative_path)
abs_path = os.path.abspath(relative_path)
print(abs_path)