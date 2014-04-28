import re
import urllib


# Take a url and return the corresponding web page data.
#
# @param [string] url The URL of a web-page
# @return [string] page The web-page as a string
def getPage(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


# Take a web page's content and return a list of urls that are linked
# to by that page.
#
# @param [string] content Content of a web page as a string
# @return [list] links A list of the links in the web page
def getAllLinks(content):
    links = []
    while True:     # go forever
        url, endpos = getNextTarget(content)
        if url:     # if url is not empty
            links.append(url)
            content = content[endpos:]    # Keep reducing the web page
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
# We check if the keyword has been used, then check if url is already there.
# TODO: have a counter for each url
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
            if not url in entry[1]:  # if url isn't already in list, add it
                entry[1].append(url)
            return   # don't keep looking after we find the index

    # not found, add new keyword to index
    index.append([keyword, [url]])


# Add the content of a web page to our index
#
# @param [list] index An index of keywords and associated URLs
# @param [string] url
# @param [string] content Web page content as a string
def addPageToIndex(index, url, content):
    # Clean up the content
    # pattern = "<\S*>|(>|http|href|www|\d)\S* ?"
    pattern = "<\S*>|>|http|href|www|\d|_\S*"
    content2 = re.sub(pattern, '', content)

    # split content into a list of keywords
    keywords = re.split(r"\W", content2)

    # check for '' list items and remove -> this is slow
    # while keywords.count('') != 0:
    #     keywords.remove('')
    # # Clean up option to get rid of short keywords. This doesn't work.
    # for word in keywords:
    #     if len(word) < 3:
    #         keywords.remove(word)

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
    # We do two lists so we finish an entire depth level before moving to the next.
    next_depth = []     # list of URLs of pages in the next depth level
    depth = 0           # we begin at depth level 0, the seed page

    while to_crawl and depth <= max_depth:
        url = to_crawl.pop()
        if url not in crawled:  # Check if we have already crawled this page
            content = getPage(url)  # Get the content from the page as a string
            addPageToIndex(index, url, content)  # Add content of page to index

            new_links = getAllLinks(content)  # Crawl the page
            union(next_depth, new_links)  # Add new links to to_crawl list
            crawled.append(url)     # Add page URL to crawled list

        if not to_crawl:     # if to_crawl is empty, move to next depth
            to_crawl, next_depth = next_depth, []   # fill to_crawl and empty next_depth
            depth += 1

    return index

# Kick things off with a seed page.
index = crawlWeb("http://www.huffingtonpost.com/ryan-holiday/spartan-system_b_1556462.html", 0)

print len(index)
for element in index:
    print element
