import requests


res = requests.get("https://hivescans.com")
print(res.text)


pic = requests.get("https://hivescans.com/wp-content/uploads/1673965364-6555-i348071.png")

# install pic in directory
with open('comic.png', 'wb') as f:
    f.write(pic.content)

# if true, then if less then 400, then true, if more than false from status code
print(pic.ok)

# if 200, success, if 300, redirects, if 400, client errors, if 500, server error
print(pic.status_code)
#


