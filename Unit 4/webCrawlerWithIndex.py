

# A function that takes a url and returns the corresponding web-page as a string.
#
# @param [string] url The URL of a web-page
# @return [string] page The web-page as a string
def getPage(url):
    try:
        import urllib
        # print urllib.urlopen(url).read()
        return urllib.urlopen(url).read()
    except:
        return ""


# A function that takes in a web page as a string, and returns a list
#  containing all the urls that are linked to by that page
#
# @param [string] page A web page as a string
# @return [list] links A list of the links in the web page
def getAllLinks(page):
    links = []
    while True:     # go forever
        url, endpos = getNextTarget(page)
        if url:     # if url is not empty
            links.append(url)
            page = page[endpos:]    # Keep reducing the web page
        else:
            break
    return links


# A function that takes in the content of a web page as a string,
# finds the first url, and returns that url and the ending position
# of the url.
#
# @param [string] content Content of a web page
# @return [string] url The first link found
# @return [string] end_quote The index position of the end of the link found
def getNextTarget(content):
    start_link = content.find(' href="http')
    if start_link == -1:    # If we don't find a link tag in page
        return None, 0
    start_quote = content.find('"', start_link)
    end_quote = content.find('"', start_quote + 1)
    url = content[start_quote+1: end_quote]
    return url, end_quote


# A function that takes as inputs two lists and modifies the first list to be
# a set union of the two lists.
#
# @param [list] list1
# @param [list] list2
# We don't return anything b/c lists are passed by reference. We modify list1.
def union(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item)

# Associate a url with a keyword in the index.
#
# @param [list] index An list where each element contains two elements -
#   1. the keyword
#   2. A list of urls associated with the keyword
# @param [string] keyword
# @param [string] url
# @return [list] index Updated list (by reference)
def addToIndex(index, keyword, url):
    # If keyword is already in the index, add the url to the list of
    # urls associated with that keyword
    for entry in index:   # Iterate over the index looking for keyword
        if entry[0] == keyword:
            entry[1].append(url)  # If we find the keyword, append the url
            return   # don't keep looking after we find the index

    # If the keyword is not in the index, add the entry to the index:
    # [keyword, [url]]
    index.append([keyword, [url]])

# Add the content of a web page to our index
#
# @param [list] index An index of keywords and associated URLs
# @param [string] url
# @param [string] content Web page content as a string
def addPageToIndex(index, url, content):
    # Clean up the content by removing prior and trailing punctuation

    # turn content into a list of words
    keywords = content.split()

    # for each keyword, call addToIndex
    for keyword in keywords:
        addToIndex(index, keyword, url)


# A function that takes a url as a seed-page, and returns a list of all urls
# that can be reached by following the links on the seed-page.
#
# @param [string] seed Seed page URL
# @param [int] max_depth Max depth we will crawl
# @return [list] crawled List of all urls that can be reached by following
#   links starting from the seed page.
def crawlWeb(seed, max_depth):
    to_crawl = [seed]   # list of URLs of pages left to crawl in current depth level
    crawled = []        # list of URLs of pages we have crawled
    index = []

    while to_crawl:
        url = to_crawl.pop()
        if url not in crawled:  # Check if we have already crawled this page
            content = getPage(url)  # Get the content from the page as a string
            addPageToIndex(index, url, content)  # Add content of page to index
            new_links = getAllLinks(content)  # Crawl the page
            union(to_crawl, new_links)  # Add new links to to_crawl list
            crawled.append(url)     # Add page URL to crawled list

    return index

# Kick things off with a seed page.
print crawlWeb("http://xkcd.com/353", 1)
