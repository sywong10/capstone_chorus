from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setup_db, db, Singer, Choir, ChoirEnrollment
# from models import setup_db, db



def create_app(test_config=None):
    app = Flask(__name__)
    migrate = Migrate(app, db)

    setup_db(app)
    CORS(app, resources={r"/*": {"origins": "*"}})


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE')
        return response


    @app.route('/')
    def index():
        return 'hello'


    @app.route('/singers', methods=['GET'])
    def get_singers():

      singers = Singer.query.all()

      return jsonify({
            'success': True,
            'singers': [s.long() for s in singers]
        }), 200


    @app.route('/singers', methods=['POST'])
    def add_singers():
        body = request.get_json()

        new_name = body.get('name', None)
        new_phone = body.get('phone', None)
        new_voice_part = body.get('voice_part', None)
        new_not_available = body.get('not_available', None)

        try:
            singer = Singer(name=new_name, phone=new_phone, voice_part=new_voice_part, not_available=new_not_available)
            singer.insert()

            return jsonify({
              'success': True,
              'singers': 'singer added'
            }), 200

        except Exception as e:
            print(e)
            abort(404)


    # @app.route('/singers/<int:id>/voice_type', methods=['GET'])
    # def get_singer_type(id):
    #
    #     try:
    #         singers = Singer.query.filter(Singer.id==id).all()
    #         # print(singer.voice_part)
    #
    #         for s in singers:
    #             print(s.id)
    #             print(s.voice_part)
    #
    #     except Exception as e:
    #         print(e)
    #         # abort(404)
    #
    #     return('from voice_type')


    # @app.route('/singers/<int:id>/voice_type', method=['GET'])
    # def get_singer_by_type():




    # @app.route('/singers/<int:id>/name', method=['GET'])




    @app.route('/choirs', methods=['GET'])
    def get_choirs():

        all_choirs = Choir.query.all()

        for c in all_choirs:
            print(c.id)
            print(c.name)

        return('all choir names')


    return app

# @app.route('/add_singer'):
# def add_singer():
