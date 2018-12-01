
## RIDDLE-ME-THIS multi-player game app

This project has been developed as part of CI Dublin's coding bootcamp for software developers following modules in HTML, CSS, User Centric Frontend Dev, Javascript Fundamentals, Interactive Frontend Dev, Python Fundamentals and Practical Python. 

This is multi-player game application written in Python, and using the Flask framework. The purpose of this app is to allow multiple players to compete for the highest ranking score on the leaderboard by solving riddles. 

This project is called Chalkboard, and is themed around a school-learning environment. 

## UX
This game is designed with desktop first approach as I imagine it beging used in a learning environment where mobile phones are not common. In order to give this project the look and feel of a game environment (without more advanced game-mbuilding skills), I gave it a clear theme which is depicted throughout. 

I decided that an easy-to-use game application should have a simpe layout, and be able to present core information in a readable way. 

I therefore decided to center the game around a chalkboard image, and provide users with riddles written on the board. The player's score, name, and guess result are also documented consistently on the board's bottom left hand corner. Meanwhile, all buttons used throughout are consistently circular and glowing.  

## FEATURES

# features implemented

    1) Users can access the game by providing a username which is logged in a txt file. 
    2) Upon supplying a username, user's must guess the answer to a series of riddles. If they guess incorrectly, they are returned to the same riddle and informed that they supplied the wrong answer. If they guess correctly they are returned to the next riddle and their score is incremented by one. 
    3) After reaching the end of the game, they are returned to the game over page, where they are shown a leaderboard with top 5 highest scores. 
    4) Users can then choose to 'play again' if they are feeling competitive.

# features-to-be-implemented

    1) The riddle questions are stored in a json file. The game displays all riddles in this file. With more time I would work on a feature that shuffles the order of the riddles, so that each instance of the game is different. I would then add more riddles than the 6 provided to make the most of this feature.
    2) I would create an if statement with flash messages to provide motivational statements at particular scores e.g score == 3, 'not bad', score == 5 'you're pretty good at this'

# TECH USED
This project features my first use of Python https://www.python.org/

HTML & CSS are also used for layout and design.

Bootstrap Grid System offers responsive layout for design. https://getbootstrap.com/ 

Font Awesome provides lovely icons https://fontawesome.com/

The framework used is the popular micro framework Flask http://flask.pocoo.org/docs/1.0/

# TESTING 

# Manual Testing: 

Here's an example scenario used in the manual testing phase of this project: 

    1) Test that the username form appends username to the file players.txt & passes name to game page:
        i) input username on index page 
        ii) continue to game page
        iii) check that username is displayed on the game page
        iv) open the txt file to check that the name has been appended
    2) Test responsivity across devices using Chameleon plug in and Emmet Re:View
        i) check different break points for screen widths
        ii) note problem areas

While the game is largely responsive, the riddles need to be repositioned by scrolling each time, as they load lower down on the page than intended, and are structured as flex elements due to the background image styles. As mentioned, this game is really built for rendering on medium to large screen sizes. 

Iphone 5 and lower screen dimensions will not get the optimal style of this game which is an issue that needs to be addressed.  

# Unittest testing: 

The testing framework used in this project is the standard library unittest. 

No installation needed, simply: 

    import unittest
    import run

An example of a sample testcase used to check that the unittest is up and running: 

    class example_test(unittest.TestCase):
    # test that unittest is set up correctly
    def test_working(self):
        x = 2
        y = 2
        self.assertEqual((x,y), (2,2), 'Failed')

To run the test file from the command line: 

    python3 -m unittest test_run.py
    
Using this framework, I executed tests to ensure that all routes and pages were loading as expected. Which they did. 

I then set up a class to test write and append features as such: 

        @classmethod
        def setUpClass(cls): 
        # set up mock txt file for testing run.py's player_list
        with open("data/test_users.txt", "a") as append_user:
            append_user.write("user1" + "\n")  
            append_user.write("user2" + "\n")
            append_user.write("user3" + "\n")

        # set up mock json file to mimic run.py's riddle_list
        with open("data/test_data.json", "w") as test_data:
            data = "[{'riddle':'a riddle question', 'answer':'a riddle answer'}]"
            test_data.write(data)
        
        print("setUpClass - TestFileReadAppend")

From here, I was able to test write and append operations aswell as to test the data going into and being retrieved from the json file. The tests provided the expected results for the features tested. More extensive testing is however required, but for now, I'm a novice tester with much more to learn! 

# Deployment 

# Credits 
# content
Riddles taken from https://riddlesbrainteasers.com 

# media 
All images used in this project are open souce and available for commercial usage. 

# acknowledgements 
Thanks to CI Dublin 
