import shutil
# shutil клевая вещь, без шуток:D
try:
    folder_from = 'my_cool_project'
    folder_where = 'my_cool_project/templates'
    shutil.copytree(folder_from, folder_where)
except Exception as e:
    print(f'global error: {e}')
