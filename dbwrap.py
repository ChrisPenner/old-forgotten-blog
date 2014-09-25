from google.appengine.api import memcache


post_dict = {}
post_list = []


def put(name, post):
    post_dict[name] = post
    post_list.append(post)
    sort_post_list()


def get(key, namespace=None):
    return memcache.get(key, namespace=namespace)


def get_post(name):
    return post_dict.get(name)


def sort_post_list():
    def get_time_tuple(post):
        return post.sort_date
    post_list.sort(key=get_time_tuple, reverse=True)
