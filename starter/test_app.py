import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Singer, Choir, ChoirEnrollment
from settings import TEST_DB_NAME, TEST_DB_USER, TEST_DB_PASSWORD, SINGER_TOKEN, DIRECTOR_TOKEN


class ChoirTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(TEST_DB_USER, TEST_DB_PASSWORD, 'localhost:5432', TEST_DB_NAME)
        setup_db(self.app, self.database_path)

        self.headers_director = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + DIRECTOR_TOKEN
        }

        self.headers_singer = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + SINGER_TOKEN
        }

        self.new_singer = {
            'name': 'Liz Lemon',
            'phone': '423-521-9581',
            'voice_part': 'soprano',
            'not_available': 'Tuesday'
        }

        self.new_singer2 = {
            'name': 'Jack Donaghy',
            'phone': '398-889-9554',
            'voice_part': 'tenor',
            'not_available': 'Tuesday'
        }

        self.new_singer3 = {
            'name': 'Tracy Jordan',
            'phone': '683-811-9521',
            'voice_part': 'baritone',
            'not_available': 'Tuesday'
        }

        self.new_choir = {
            'name': 'Somerset',
            'practice_time': 'Monday 7 pm'
        }


        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()


    def tearDown(self):
        pass


    def test_get_paginated_singers(self):
        res= self.client.get('/singers', headers=self.headers_director)
        data = json.loads(res.data)
        # print('data: {}'.format(data))
        # print('res: {}'.format(res))
        # print(res.status_code)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['singers'])
        self.assertTrue(data['total singers'])


    # there is no page 100, status code should be 404
    def test_404_get_paginated_singers_beyong_valid_page(self):
        res = self.client.get('/singers?page=100', headers=self.headers_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_get_singer_by_id(self):
        res = self.client.get('/singers/2', headers=self.headers_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['singer'])

    def test_404_get_singer_by_id(self):
        res = self.client.get('singers/200', headers=self.headers_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # def test_delete_a_singer(self):
    #     res = self.client.delete('/singers/16', headers=self.headers_director)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['deleted singer'])


    # delete a singer who does not exist
    # def test_404_delete_a_singer(self):
    #     res = self.client.delete('singers/16', headers=self.headers_director)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')


    # def test_add_a_singer(self):
    #     res = self.client.post('/singers', headers=self.headers_singer, json=self.new_singer)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['singer added'])


    # def test_409_add_a_singer(self):
    #     res = self.client.post('/singers', headers=self.headers_singer, json=self.new_singer)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 409)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "schedule conflict")


    # def test_409_add_an_incorrect_voice_part(self):
    #     res = self.client.post('/singers', headers=self.headers_singer, json=self.new_singer3)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "unprocessable_entity")


    def test_singers_voice_part(self):
        res =self.client.get('/singers/alto', headers=self.headers_singer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total'])


    def test_422_singers_voice_part(self):
        res = self.client.get('/singers/baritone', headers=self.headers_singer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable_entity")


    # update singer information, ie, change not_available to Friday
    def test_singers_update(self):
        res = self.client.patch('/singers/17', headers=self.headers_singer, json={"not_available": "Monday"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['singer'])


    def test_404_singer_update(self):
        res = self.client.patch('/singers/30', headers=self.headers_singer, json={"not_available": "Friday"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")


    def test_get_choirs(self):
        res = self.client.get('/choirs', headers=self.headers_singer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['choirs'])



    # def test_add_choir(self):
    #     res = self.client.post('/choirs', headers=self.headers_director, json=self.new_choir)
    #     data = json.loads(res.data)
    #
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue((data['choir added']))


    def test_add_choir(self):
        res = self.client.post('/choirs', headers=self.headers_singer, json=self.new_choir)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], "unauthorized")
        self.assertEqual(data['description'], "you are unauthorized")



if __name__ == '__main__':
    unittest.main()
