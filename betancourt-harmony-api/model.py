""" This random generator model handles fetching, parsing, and sorting data from the api. """
import urllib2  # Python classes and code needed to request/receive/open url info
import json  # Json needed to compile/format responses from API


class RgModel(object):
    def __init__(self):
        self._userinput = ''  # Form set by main
        self._results = {}  # Results container to be filled by setter

    @property
    def userinput(self):  # Getter for user input
        return self._userinput  # Returns private user input

    @userinput.setter  # Set user input value
    def userinput(self, g):
        gender = g.lower()  # Anything put in by user is formatted to lower case
        if gender == "male":  # Anything Male
            self._userinput = "male"  # Input is male
        elif gender == "female":  # Anything Female
            self._userinput = "female"  # Input is female
        elif gender == "either":  # If Either Gender
            self._userinput = "Either"   # Set Input for no entry
        else:  # If it's anything else
            self._userinput = "None"  # Value is none

    @property
    def results(self):  # Getter for results
        return self._results  # Returns private results

    @results.setter
    def results(self, g):  # Sets results
        gender = g  # Gender is variable sent in
        url = "http://api.randomuser.me/?gender=" + gender  # Url plus gender selection
        # Assemble request
        request = urllib2.Request(url)
        # Use urllib2 to create object to get url
        geturl = urllib2.build_opener()
        # Use url to get result - request info from API
        fromapi = geturl.open(request)

        # Parse with JSON
        api_json = json.load(fromapi)
        # Get information from JSON
        us = api_json['results'][0]['user']['username']   # Get alias username
        ng = api_json['results'][0]['user']['gender']   # Get alias gender
        e = api_json['results'][0]['user']['email']   # Get alias email
        dob = float(api_json['results'][0]['user']['dob'])  # Get alias birthday in epoch as a float
        p = api_json['results'][0]['user']['phone']   # Get alias phone
        c = api_json['results'][0]['user']['cell']   # Get alias cell phone
        t = api_json['results'][0]['user']['name']['title']  # Get alias title
        first = api_json['results'][0]['user']['name']['first']  # Get alias first name
        last = api_json['results'][0]['user']['name']['last']  # Get alias last name
        street = api_json['results'][0]['user']['location']['street']  # Get alias street
        city = api_json['results'][0]['user']['location']['city']  # Get alias city
        state = api_json['results'][0]['user']['location']['state']  # Get alias  state
        thiszip = api_json['results'][0]['user']['location']['zip']  # Get alias zip
        image = api_json['results'][0]['user']['picture']['large']  # Get alias image - large size
        # Put all elements of name into one name with capitalized first letters
        name = t.capitalize() + " " + first.capitalize() + " " + last.capitalize()
        # Put all address elements into one variable with title format on the words
        add = street.title() + "<br/> " + city.title() + ", " + state.title() + " " + thiszip

        # Put it in the container
        self._results = {'us': us, 'g': ng, 'e': e, 'dob': dob, 'p': p, 'c': c, 't': t, 'n': name, 'a': add, 'i': image}

