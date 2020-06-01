def continue_crawl(search_history, target_url, max_steps=25):
    '''
    This is to find lists of urls leading to target_url

    search_history: list of searches
    target_url: target
    '''
    if search_history[-1] == target_url:
        print('Target found!')
        return False

    elif len(search_history) > max_steps:
        print('Target not found after %f trial', %len(max_steps))
        return False

    elif search_history[-1] in search_history[:-1]:
        print('You are stocked in a loop')
        return False

    else:
        True

import time

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return 

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link





