""" This model handles fetching, parsing, and sorting data from the api. """
import urllib2  # Python classes and code needed to request/recieve/open url info
import json
import time  # Will translate epoch format for dob into something readable


class AltView(object):
    def __init__(self):
        self._userinput = ''  # Form set by main
        self._results = ''

    @property
    def userinput(self):  # Getter for user input
        return self._userinput  # Returns private user input

    @userinput.setter  # Set user input value
    def userinput(self, g):
        gender = g.lower()  # Anything put in by user is formatted to lower case
        if gender == "male" or gender == "m" or gender == 'man' or gender == 'boy':  # Anything Male
            self._userinput = "male"  # Input is male
        elif gender == "female" or gender == 'f' or gender == 'woman' or gender == 'girl':  # Anything Female
            self._userinput = "female"  # Input is female
        else:  # Anything else
            self._userinput = " "   # Leave it blank for random results

    @property
    def results(self):  # Getter for results
        return self._results

    @results.setter
    def results(self, g):
        gender = g
        url = "http://api.randomuser.me/?gender=" + gender
        print url
        # Assemble request
        request = urllib2.Request(url)
        # Use urllib2 to create object to get url
        geturl = urllib2.build_opener()
        # Use url to get result - request info from API
        fromapi = geturl.open(request)

        # Parse with JSON
        api_json = json.load(fromapi)
        # Get information from JSON
        u = api_json['results'][0]['user']['username']   # Get alias username
        ng = api_json['results'][0]['user']['gender']   # Get alias gender
        e = api_json['results'][0]['user']['email']   # Get alias email
        dob = float(api_json['results'][0]['user']['dob'])  # Get alias birthday in epoch as a float
        p = api_json['results'][0]['user']['phone']   # Get alias phone
        c = api_json['results'][0]['user']['cell']   # Get alias cell phone
        title = api_json['results'][0]['user']['name']['title']  # Get alias title
        first = api_json['results'][0]['user']['name']['first']  # Get alias first name
        last = api_json['results'][0]['user']['name']['last']  # Get alias last name
        street = api_json['results'][0]['user']['location']['street']  # Get alias street
        city = api_json['results'][0]['user']['location']['city']  # Get alias city
        state = api_json['results'][0]['user']['location']['state']  # Get alias  state
        zip = api_json['results'][0]['user']['location']['zip']  # Get alias zip
        image = api_json['results'][0]['user']['picture']['medium']  # Get alias image - medium size

        # Formatting and simplifying
        username = "Username: " + u + "<br/>"  # Add label and break
        new_gender = "Gender: " + ng.capitalize() + "<br/>"  # Add label, capitalize, and break
        email = "Email: " + e + "<br/>"  # Add label and break
        dob = time.strftime('%B %d %Y', time.localtime(dob))  # DOB now is in local readable time
        bday = "Birthday: " + dob + "<br/>"  # Add label and break
        phone = "Phone Number: " + p + "<br/>"  # Add label and break
        cell = "Mobile Number: " + c + "<br/>"  # Add label and break
        image_ready = '<img src="' + image + '" alt="Your Pretty Picture" /><br/>'  # format image

        # Put all elements of name into one name with capitalized first letters
        name = "Name: " + title.capitalize() + " " + first.capitalize() + " " + last.capitalize() + "<br/>"
        # Put all address elements into one variable with title format on the words
        address = street.title() + " " + city.title() + ", " + state.title() + " " + zip

        # Return results
        self._results = image_ready + name + new_gender + username + bday + email + phone + cell + address
