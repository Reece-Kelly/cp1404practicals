import wikipedia

page_title = input("Page title: ")
while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        page_title = input("Page title: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        page_title = input("Page title: ")
