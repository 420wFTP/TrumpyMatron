# TrumpyMatron
Filling out Trump Campaign surveys to mess with their voter data collection, just for kicks.

### Setup

This uses the `mechanize` and `ssl` libraries in Python3. Running is as simple as:
- Installing Python3
- Install `mechanize`:
    - `pip3 install mechanize`
- Run the script:
    - `python3 TrumpyMatron.py`
    
Once form submission is enabled you will need to edit the appropriate fields in the code. Feel free to change this.

### NOTES:
- I have successfully gotten Python to conenct to the webpage and open, bypassing `robots.txt`
- This script does not yet submit the form, it just prints the webpage form information as parsed by `mechanize`
- If feeling lazy but still want to run the survey submission loop, the survey can be submitted with just the text fields filled out. So you _could_ enable that and make the campaign chug empty responses... but where's the fun in that? This also probably means that this whole thing is an excercise in futility, but hey, have fun with it.
    
### TODO:
- Add form-filling/submitting functionality (too time crunched to get it working rn)
- Add random email IDs
- Add random ZIP code fills

? ANTIFA ? ଘ(੭*ˊᵕˋ)੭* ̀ˋ ? ANTIFA ?

