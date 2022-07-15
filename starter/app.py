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
            new_singer = Singer(
                name = new_name,
                phone = new_phone,
                voice_part = new_voice_part,
                not_available = new_not_available
            )

            new_singer.insert()

            return jsonify({
              'success': True,
              'singers': new_name + ' added'
            }), 200

        except Exception as e:
            print(e)
            abort(404)


    @app.route('/singers/<voice_part>', methods=['GET'])
    def get_voice_type(voice_part):

        parts = ['soprano', 'alto', 'tenor', 'bass']

        if voice_part in parts:
            print('voice_part: {}'.format(voice_part))
        else:
            print("sorry we don't have {}".format(voice_part))
            abort(404)

        try:
            singers = Singer.query.filter(Singer.voice_part==voice_part).all()

            return jsonify({
                'success': True,
                voice_part: [s.name for s in singers]
            })

        except Exception as e:
            print(e)
            abort(404)

    @app.route('/singers/<int:id>/', methods=['GET'])
    #
    def get_singer_type(id):
        try:
            singer = Singer.query.filter(Singer.id == id).one_or_none()

            return jsonify({
                'success': True,
                'singer': singer.long()
            })

        except Exception as e:
            print(e)
            abort(404)


    @app.route('/singers/<int:id>/', methods=['PATCH'])
    def modify_singer(id):
        body = request.get_json()
        updated_singer = Singer.query.filter(Singer.id==id).one_or_none()

        if updated_singer is None:
            return('id does not exist')
            abort(404)

        try:
            if not body.get("name", None) is None:
                updated_singer.name = body.get("name")

            if not body.get("phone", None) is None:
                updated_singer.phone = body.get("phone")

            if not body.get("voice_part", None) is None:
                updated_singer.voice_part = body.get("voice_part")

            if not body.get("not_available", None) is None:
                updated_singer.not_available = body.get("not_available")

            updated_singer.update()

            return jsonify({
                'success': True,
                'singer': updated_singer.long()
            }), 200


        except Exception as e:
            print(e)
            abort(400)


    @app.route('/singers/<int:id>/', methods=['DELETE'])
    def delete_singer(id):
        delete_singer = Singer.query.filter(Singer.id==id).one_or_none()

        if not delete_singer:
            abort(404)

        try:
            delete_singer.delete()

            return jsonify({
                'success': True,
                'deleted singer': delete_singer.short()
            })

        except Exception as e:
            print(e)
            abort(422)



    @app.route('/choirs', methods=['GET'])
    def get_choirs():

        choirs = Choir.query.all()
        print('let see')
        print(choirs)

        return jsonify({
            'success': True,
            'choirs': [ choir.long() for choir in choirs ]
        }), 200


    @app.route('/choirs', methods=['POST'])
    def add_choir():

        body = request.get_json()

        new_name = body.get("name", None)
        new_practice_time = body.get("practice_time", None)

        print('new_practice_time: {}'.format(new_practice_time))

        try:
            new_choir = Choir(
                name = new_name,
                practice_time = new_practice_time
            )

            new_choir.insert()

            return jsonify({
                'success': True,
                'choir added': new_choir.name
            })

        except Exception as e:
            print(e)
            abort(404)


    @app.route('/choirs/<int:id>', methods=['PATCH'])
    def update_choir(id):
        body = request.get_json()

        updated_choir = Choir.query.filter(Choir.id==id).one_or_none()

        if updated_choir is None:
            return('id does not exist')
            abort(404)

        try:
            if not body.get("name", None) is None:
                updated_choir.name=body.get("name")

            if not body.get("practice_time", None) is None:
                updated_choir.practice_time=body.get("practice_time")

            updated_choir.update()

            return jsonify({
                'success': True,
                'updated choir': updated_choir.long()
            }), 200

        except Exception as e:
            print(e)
            abort(404)

    @app.route('/choirs/<int:id>', methods=['DELETE'])
    def delete_choir(id):

        delete_choir = Choir.query.filter(Choir.id==id).one_or_none()

        if not delete_choir:
            return('id does not exist')
            abort(404)

        try:
            delete_choir.delete()

            return jsonify({
                'success': True,
                'removed choir': delete_choir.long()
            }), 200

        except Exception as e:
            print(e)
            abort(404)


    #  who is in which choir, pass in choir id
    @app.route('/test/<int:cid>', methods=['GET'])
    def test(cid):

        # get_choir_name = Choir.query.filter_by(cid)
        get_choir_name = Choir.query.join(ChoirEnrollment, ChoirEnrollment.choir_id==cid)
        # get_singers = Singer.query.join(ChoirEnrollment, ChoirEnrollment.choir_id == cid)

        print(get_choir_name)

        for i in get_choir_name:
            print(i)

        return('lets see')

    return app


