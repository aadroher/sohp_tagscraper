from flask import Flask, render_template
from page import Page

app = Flask(__name__)

# Global config
so_url = "http://stackoverflow.com/"

@app.route('/', methods=['GET'])
def tag_stats():
    page = Page(url=so_url)
    # tags = parser.get_tags(parser._dom)
    tag_freqs = page.tag_freqs()
    top_questions = page.top_questions()

    return render_template('stats.html', tag_freqs=tag_freqs,
                                         top_questions=top_questions,
                                         so_url=so_url,
                                         req_time=page.req_time)
if __name__ == '__main__':
    app.run(debug=True)
