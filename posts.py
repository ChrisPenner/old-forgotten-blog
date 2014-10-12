import dbwrap

from lib import markdown2
from lib import parsedatetime
import datetime
import os


class Post(object):
    def __init__(self, title='', name='', content='', date='', author='',
                 tags=set(), categories=set(), **kwargs
                 ):
        date, sort_date, pub_date = parse_date(date)
        self.date = date
        self.sort_date = sort_date
        self.pub_date = pub_date
        self.title = title
        self.name = name
        self.author = author
        self.content = content
        self.link = "http://www.chrispenner.ca/post/" + name
        self.tags = tags
        self.categories = categories


def init():
    md = markdown2.Markdown()
    dir_path = 'content/posts'
    file_list = [f for f in os.listdir(dir_path) if not f.startswith('.')]
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path) as f:
            # read title, author, and date from file before converting markdown.
            line = ''
            post_info = {}
            while not line.startswith('\n'):
                line = f.readline()
                if line.lower().startswith('title'):
                    post_info['title'] = line.replace('title:', '').strip()

                elif line.lower().startswith('date'):
                    post_info['date'] = line.replace('date:', '').strip()

                elif line.lower().startswith('author'):
                    post_info['author'] = line.replace('author:', '').strip()

                elif line.lower().startswith('categories'):
                    line_contents = line.lower().replace('categories:', '').strip()
                    categories = line_contents.split(' ')
                    categories = map(str.strip, categories)
                    categories = filter(lambda x: '' != x, categories)
                    post_info['categories'] = set(categories)

                elif line.lower().startswith('tags'):
                    line_contents = line.lower().replace('tags:', '').strip()
                    tags = line_contents.split(' ')
                    tags = map(str.strip, tags)
                    tags = filter(lambda x: '' != x, tags)
                    post_info['tags'] = set(tags)

            s = f.read()
            content = md.convert(s)
            # split file name on . take the file name, lowercase
            post_info['name'] = file_name.rpartition('.')[0].lower()
            post_info['content'] = content

            # add all retrieved content to post
            post = Post(**post_info)
            add_post(post)


def add_post(post):
    dbwrap.put(post.name, post)


def get_adj_posts(post_name):
    post_names = [p.name for p in dbwrap.post_list]
    if post_name in post_names:
        index = post_names.index(post_name)
        if index + 1 < len(post_names):
            next_post = post_names[index + 1]
        else:
            next_post = None

        if index - 1 >= 0:
            prev_post = post_names[index - 1]
        else:
            prev_post = None
        return (prev_post, next_post)
    else:
        return (None, None)


def parse_date(date):
    months = {1: 'Jan',
              2: 'Feb',
              3: 'Mar',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'Aug',
              9: 'Sept',
              10: 'Oct',
              11: 'Nov',
              12: 'Dec',
              }
    pdt = parsedatetime.Calendar()
    sort_date, t = pdt.parse(date)
    year = str(sort_date[0])
    month = months[sort_date[1]]
    day = str(sort_date[2])

    date_obj = datetime.date(sort_date[0], sort_date[1], sort_date[2])
    pub_date = date_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")

    if day[-1] == '1':
        suffix = 'st'
    elif day[-1] == '2':
        suffix = 'nd'
    elif day[-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'

    date = "%(month)s %(day)s%(suffix)s %(year)s" % {
        'month': month,
        'day': day,
        'suffix': suffix,
        'year': year,
        }

    return date, sort_date, pub_date


init()
