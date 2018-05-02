from bs4 import BeautifulSoup
html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p id="start" class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")


tag = soup.find("p")
print("1. Find P tag\n"+str(tag)+"\n")

tag2 = soup.findAll("p")[1].prettify()
print("2. Find P tag and pretty print\n"+str(tag2))

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
tag3 = soup.findAll(has_class_but_no_id)
print("3. Find tags that have classes but no id\n"+str(tag3))