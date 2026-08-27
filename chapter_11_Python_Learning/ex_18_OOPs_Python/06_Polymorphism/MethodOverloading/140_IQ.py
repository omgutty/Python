# 140_IQ.py
# Topic: Real-world "overloading" - HTTP request with optional auth
#
# Only the SECOND make_http_request exists (last definition wins).
# auth=None is optional, so you can call it with just a url, or
# with url + credentials. Same method, two ways to call it.

class Browser:

    def make_http_request(self, url):
        print("Hi, Lets make the HTTP request without auth", url)   # overwritten

    def make_http_request(self, url, auth=None):                    # the real one
        print("Hi, Lets make the HTTP request with auth", url, auth)


t = Browser()
t.make_http_request("google.com","admin")   # url + auth given