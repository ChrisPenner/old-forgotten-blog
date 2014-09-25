import webapp2

import posts
import dbwrap
from handler import Handler


class Contents(Handler):
    def get(self):
        post_list = dbwrap.post_list
        self.render("contents.html", blog_posts=post_list)


class PostHandler(Handler):
    def get(self, post_name):
        if not post_name:
            self.redirect('/blog/')

        post_name = post_name.lower()
        post_dict = dbwrap.post_dict
        if post_name in post_dict:
            post = dbwrap.get_post(post_name)
            prev_post, next_post = posts.get_adj_posts(post_name)
            self.render('post.html',
                        post=post,
                        prev_post=prev_post,
                        next_post=next_post,
                        )
        else:
            self.redirect('/')


app = webapp2.WSGIApplication([
    ('/blog/', Contents),
    ('/blog/([^/]+)', PostHandler),
], debug=True)
