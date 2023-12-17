title_article = input()
content_article = input()

print(f"<h1>  \n"
      f"   {title_article}\n"
      f"</h1>")

print(f"<article> \n"
      f"    {content_article}\n"
      f"</article>")

while True:
    command = input()
    if command == "end of comments":
        break
    print(f"<div>\n"
          f"    {command}\n"
          f"</div>")



