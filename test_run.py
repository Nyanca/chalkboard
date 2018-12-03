import os
import unittest
import run
import json
from run import app, index, user
from flask import Flask, url_for

class example_test(unittest.TestCase):
    # test that unittest is set up correctly
    def test_working(self):
        x = 2
        y = 2
        self.assertEqual((x,y), (2,2), 'Failed')
    
class TestPageLoad(unittest.TestCase):
    '''
    a test suite for run.py
    '''
    @classmethod
    def setUpClass(cls): 
        #called immediately before a test
        print("setUpClass - TestFlaskRoutes")

    @classmethod
    def tearDownClass(cls):
        #called after each test runs in this class
        print("tearDownClass - TestFlaskRoutes")
        
    def test_index_route(self):
    # test home page renders expected route 200
        tester = app.test_client(self)  
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_index_route 200/SUCCESS")
        
    def test_index_page_load(self):
    # test home page loads correctly
        tester = app.test_client(self)  
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Chalkboard' in response.data)
        print("test_index_page_load-- SUCCESS")
    
    def test_user_route(self):
    # test game page renders expected route 200
        tester = app.test_client(self)  
        response = tester.get('/<username>', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print("test_user_route 200/SUCCESS")
    
    def test_user_page_load(self):
    # test game page loads correctly
        tester = app.test_client(self)  
        response = tester.get('/<username>', content_type='html/text')
        self.assertTrue(b'Chalkboard' in response.data)
        print("test_user_page_load-- SUCCESS")

class TestReadAppend(unittest.TestCase):
    ''' 
    A test suite for testing file read and append operations
    '''
    
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

    @classmethod
    def tearDownClass(cls):
        os.remove("data/test_users.txt")
        os.remove("data/test_data.json")
        print("tearDownClass - TestReadAppend")
    
    def test_player_in_file(self):
        with open("data/test_users.txt", "r") as append_user:
            data = append_user.read()
        self.assertIn("user1", data)
        self.assertIn("user2", data)
        self.assertIn("user3", data)
        self.assertNotIn("anotheruser", data)
        print("test_player_in_file-- PASS")
    
    def test_data_in_file(self):
        with open("data/test_data.json", "r") as test_data:
            data = test_data.read()
        self.assertIn("riddle", data)
        self.assertIn("answer", data)
        print("test_data_in_file-- PASS")
        
    def test_key_matches_value(self):
        data = {'riddle':'a riddle question', 'answer':'a riddle answer'}
        json_str = json.dumps(data)  
        response = json.loads(json_str)
        answer = response['answer']
        riddle = response['riddle']
        self.assertEqual(answer, 'a riddle answer')
        self.assertEqual(riddle, 'a riddle question')
        print("test_key_matches_value-- PASS")

# class testCounters(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls): 
#         print("setUpClass - TestCounters")

#     @classmethod
#     def tearDownClass(cls):
#         print("tearDownClass - TestCounters")
    
#     def test_score_incrementation(self):
#         print('test_score_incrementation-- PASS')
        
if __name__ == "__main__":
    unittest.main()