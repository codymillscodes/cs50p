e = input('File name: ').lower().strip()
index = e.find('.', -6)
ext = e[index:]
if ext == '.gif':
    print('image/gif')
elif ext == '.jpg' or ext == '.jpeg':
    print('image/jpeg')
elif ext == '.png':
    print('image/png')
elif ext == '.pdf':
    print('application/pdf')
elif ext == '.txt':
    print('text/plain')
elif ext == '.zip':
    print('application/zip')
else:
    print('application/octet-stream')