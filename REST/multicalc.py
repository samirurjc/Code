#!/usr/bin/python

#
# Multiple calculator: add, subs, mult, div

# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# October 2009
#

import webappmulti
import urlparse
import simplecalc

def decorateHTML (text):

    return ("<html><body>" + text + "</body></html>")

# classes stores correspondence between operation types (as strings)
# and classes implementing the calculators for them
classes = {'add': simplecalc.add,
           'sub': simplecalc.sub,
           'mul': simplecalc.mul,
           'div': simplecalc.div}

# resources stores the resources serviced by this service,
# including the create object servicing '/' and the 
# calculator objects servicing each calculator resource
# 
resources = {}

class create (webappmulti.app):
    """Creates a new calculator (adds, substracts, multiplies or divides)

    Services:
       . POST /?type=type_of_calculator

    type_of_calculator in ('add', 'sub', 'mul', 'div')
    """

    def parse (self, request, rest):

        verb = request.split(' ',1)[0]
        return (verb, rest)

    def process (self, (verb, rest)):

        if verb == "POST":
            params = urlparse.parse_qs(rest[1:])
            print params
            try:
                oper = params['type'][0]
                resources['/' + str(self.calcno)] = classes[oper]()
                self.calcno += 1
                success = True
            except:
                success = False
                (error, message) = ("400 Bad Request",
                                    simplecalc.decorateHTML("400 Bad Request: Error in creation of calculator"))
        else:
            success = False
            (error, message) = ("405 Method Not Allowed",
                                "405 Method Not Allowed: HTTP method " + verb + " not supported")
        if success:
            return ("200 OK", simplecalc.decorateHTML(str(resources)))
        else:
            return (error, simplecalc.decorateHTML(message))


    def __init__ (self):
        self.calcno = 0
        
if __name__ == "__main__":
    createObj = create()
    resources['/'] = createObj
    multiCalc = webappmulti.webApp ("localhost", 1234, resources)
