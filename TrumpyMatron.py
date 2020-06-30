import mechanize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

### inspect form, comment out to run loop only
br = mechanize.Browser()
br.set_handle_robots(False)
### added line to get around robots.txt 403 Error
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_equiv(False)
br.open("https://www.donaldjtrump.com/landing/2020-trump-vs-dem-poll")
for form in br.forms():
    print(form)

### TODO - fix to work with RadioControl buttons
### Built this from a script I had to unsub from an email, assumed wrong form type. Pulled field names via quick inspection in Chrome...
### Can you tell I'm not a web dev yet? And I mean that as in I don't ever plan to be one. And it shows.
    
##### submit survey via inf loop
##this_survey = "garbage"
##x = 0
##while this_survey == "garbage":
##    br = mechanize.Browser()
##    br.set_handle_robots(False)
##    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
##    br.set_handle_equiv(False)
##    br.open("https://www.donaldjtrump.com/landing/2020-trump-vs-dem-poll")v
##    br.select_form(nr=0)
##    br.form['fields[340-1]'] = '$0' # love MS-13
##    br.form['fields[341-1]'] = '$0' # am corrupt
##    br.form['fields[342-1]'] = '$0' # am RADical [shaka]
##    br.form['fields[343-1]'] = '$0' # am liar
##    br.form['fields[344-1]'] = '$0' # will eat the rich
##    br.form['fields[345-1]'] = '$0' # am sleazy for sure
##    br.form['fields[346-1]'] = '$0' # am liar
##    br.form['fields[347-1]'] = '$0' # am sleepy
##    br.form['fields[348-1]'] = '$0' # have big brain
##    br.form['fields[411-1]'] = '$0' # the RAD one has my vote
##    br.form['fields[350]'] = "Big"
##    br.form['fields[351]'] = "Chungus"
##    br.form['fields[352]'] = 'trumplover69@gmail.com' ### TODO: Add random string as '+[string]@domain.com'
##    br.form['fields[353]'] = '20500' ### TODO: Randomize zip code - pull from .csv of valid US zip codes
##    req = br.submit()
##    x = x + 1
##    print("licked, stamped, and SENT survey #", x) ### comment out to silence verbose output
