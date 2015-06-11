from flask import Flask, render_template
from tag_scraper import TagScraper

app = Flask(__name__)

# Global config
so_url = "http://stackoverflow.com/"

@app.route('/', methods=['GET'])
def tag_stats():
    tag_scraper = TagScraper(url=so_url)
    tag_stats = tag_scraper.get_tag_stats()
    return render_template('tag_stats.html', tag_stats=tag_stats)

if __name__ == '__main__':
    app.run(debug=True)
