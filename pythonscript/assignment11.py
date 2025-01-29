import zipfile, urllib.request, shutil

url = 'https://www.3gpp.org/ftp//Specs/archive/29_series/29.512/29.512-f20.zip'
file_name = '29.512-f20.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()
