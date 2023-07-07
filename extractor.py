import newspaper

def extract_article_text(url):
    # Initialize newspaper article object
    article = newspaper.Article(url)

    # Download and parse the article
    article.download()
    try:
        article.parse()
    except:
        print("Unable to extract content :(")
        return '', ''

    # Extract the title and text
    title = article.title
    text = article.text

    # Return the title and text
    return title, text
