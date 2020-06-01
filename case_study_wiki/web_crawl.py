def continue_crawl(search_history, target_url):
    '''
    This is to find lists of urls leading to target_url

    search_history: list of searches
    target_url: target
    '''
    if search_history[-1] == target_url:
        print('Target found!')
        return False

    elif len(search_history) > 25:
        print('Target not found after 25 trial')
        return False

    elif search_history[-1] in search_history[:-1]:
        print('You are stocked in a loop')
        return False

    else:
        True

