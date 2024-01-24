from requests import get

file_name = input("file name: ")
url = input("url: ")

res = get(url)
with open(file_name, 'w') as file:
    file.write(res.text)
print('done')