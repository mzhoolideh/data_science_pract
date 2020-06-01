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