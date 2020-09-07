from requests_html import HTML, HTMLSession
import csv


def info_scraping(r):
    # starting an html session and getting the link where to get the session

    # in the HTML div tag under class article, we have the information
    # check the HTML tag
    articles = r.html.find('article')

    for article in articles:

        headline = article.find('.entry-title-link', first=True).text

        summary = article.find('.entry-content p', first=True).text

        try:
            vid_src = article.find('iframe', first=True).attrs['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]

            yt_link = f"https://youtube.com/watch?v={vid_id}"

        except:
            yt_link = None

        print()
        yield headline, summary, yt_link


def csv_file(r):
    # creating a csv file
    csv_file = open('cms.scrape.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

    for headline, summary, yt_link in info_scraping(r):
        # writing the data into the csv file
        csv_writer.writerow([headline, summary, yt_link])

    # closing the csv file
    csv_file.close()


def java_script_tags():
    with open('test_file.html') as html_file:
        source = html_file.read()
        html = HTML(html=source)
        html.render()

    match = html.find('#footer', first=True)
    print(match.html)


def all_links(r):
    # get all the links in the page
    for link in r.html.absolute_links:
        print(link)


session = HTMLSession()
r = session.get('https://coreyms.com/')
