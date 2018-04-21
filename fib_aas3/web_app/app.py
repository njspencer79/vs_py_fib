import fib_num
import web
import json



max_fib = 30000   # change this number to adjust max results allowed

# we redirect all requests to our generators
# we ignore favicor.ico - creating a 404 not 400 error
urls = (
    '/favicon.ico', None,
    '/(.*)', 'index'
)

app = web.application(urls, globals(), True).wsgifunc()


class index:
    def GET(self, num_it):

        if not num_it:
            num_it = 0

        # convert to an int or set to zero
        try:
            num_it = int(num_it)
        except:
            num_it = 0

        # excced the max_fib and you get a message and 400 HTTP status
        if num_it > max_fib:
            web.ctx.status = '400 Bad Request'
            return '400 Bad Request - Max Fib numbers is ' + str(max_fib)

        list_fibs = fib_num.fib_generator(num_it)

        # if your list is 2 long and 2nd result is a 400
        # then something went wrong.  HTTP error 4 and
        # we pass the message to page
        if len(list_fibs) == 2 and list_fibs[1] == 400:
            web.ctx.status = '400 Bad Request'
            return '400 Bad Request - ' + list_fibs[0]

        # if we get here we should be ok convert to JSON
        out_json = json.dumps(list_fibs)
        return out_json




if __name__ == "__main__":
    app = web.application(urls, globals())

    app.run()
