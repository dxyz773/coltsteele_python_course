from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special extra-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# Select always yields a "list"
d = soup.select("[data-example]")
d2 = soup.find_all(attrs={"data-example": "yes"})
text_special = soup.select(".special")

# print(soup.find(id="first"))
# print(soup.find_all(class_="special"))
# for i, x in enumerate(text_special):
#     print(f"{i}: {x.get_text()}")
#     print(x.attrs)

h3_attr = soup.find("h3")["data-example"]


body_el = soup.body.contents
div1 = body_el[1]
ol = div1.next_sibling.next_sibling


div2 = soup.find(id="first").find_next_sibling()
# print(div2)

h3_el = soup.find("h3")
h3_el_parent = h3_el.find_parent()
print(h3_el_parent)
