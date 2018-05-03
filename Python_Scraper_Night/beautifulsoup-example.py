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

#simple tag lookup
tag = soup.find("p")
print("1. Find P tag\n"+str(tag)+"\n")

#get all tags of a type, make it pretty
tag2 = soup.findAll(["p","title"])
print("2a. Find all P and title tags\n"+str(tag2)+"\n")
print("2b. Pretty print one of these\n"+str(tag2[2].prettify())+"\n")

#traverse up
tag3 = soup.find("a").parent
print("3. Find A tag's parent\n"+str(tag3)+"\n")

#traverse down and sideways
tag4 = soup.p.next_sibling.next_sibling
print("4. Find sibling\n"+str(tag4)+"\n")

#setup a function, pass it into beautful soup
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
tag5 = soup.findAll(has_class_but_no_id)
print("5. Find tags that have classes but no id\n"+str(tag5))