import webapp2
import dbwrap
import posts
from handler import Handler


#class Root(Handler):
    #def get(self):
        #self.redirect('/blog/')


class Contents(Handler):
    def get(self):
        post_list = dbwrap.post_list
        self.render("contents.html", blog_posts=post_list)


class PostHandler(Handler):
    def get(self, post_name):
        if not post_name:
            self.redirect('/')

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


class About(Handler):
    def get(self):
        self.render('about.html')


class Contact(Handler):
    def get(self):
        self.render('contact.html')


class RSS(Handler):
    def get(self):
        self.render('rss.xml', posts=dbwrap.post_list)


app = webapp2.WSGIApplication([
    ('/', Contents),
    ('/post/([^/]+)', PostHandler),
    ('/feed/', RSS),
    #('/about/', About),
    #('/contact/', Contact),
], debug=True)
