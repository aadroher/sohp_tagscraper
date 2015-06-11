from flask import Flask, render_template
from tag_scraper import TagScraper

app = Flask(__name__)

# Global config
so_url = "http://stackoverflow.com/"

@app.route('/', methods=['GET'])
def tag_stats():
    tag_scraper = TagScraper(url=so_url)
    tags = tag_scraper.get_tags(tag_scraper.html_doc)
    tag_freqs = tag_scraper.get_tag_freqs()

    return render_template('tag_stats.html', tag_freqs=tag_freqs,
                                            # tags=tags,
                                            so_url=so_url,
                                            req_time=tag_scraper.req_time)
if __name__ == '__main__':
    app.run(debug=True)
