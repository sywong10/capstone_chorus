from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setup_db, db, Singer, Choir, ChoirEnrollment
from .auth.auth import AuthError, requires_auth


def sort_by_voice_part(singers):
    SOPRANO = []
    ALTO = []
    TENOR = []
    BASS = []

    for i in singers:
        if i.voice_part == 'soprano':
            SOPRANO.append(i.name)
        elif i.voice_part == 'alto':
            ALTO.append(i.name)
        elif i.voice_part == 'tenor':
            TENOR.append(i.name)
        elif i.voice_part == 'bass':
            BASS.append(i.name)

    return(SOPRANO, ALTO, TENOR, BASS)


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
    # @requires_auth('get:singers')
    def get_singers():

        try:
            singers = Singer.query.all()

            return jsonify({
                'success': True,
                'singers': [s.long() for s in singers]
            }), 200

        except Exception as e:
            print(e)
            abort(404)


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
            abort(422)


    @app.route('/singers/<voice_part>', methods=['GET'])
    def get_voice_type(voice_part):

        parts = ['soprano', 'alto', 'tenor', 'bass']

        if not voice_part in parts:
            abort(422)

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


    # list singers of each voice type in the overall pool
    # return of this function does not take enrollment into consideration

    @app.route('/<voice_part>', methods=['GET'])
    def list_singers_in_pool(voice_part):
        try:
            parts = ['soprano', 'alto', 'tenor', 'bass']
            if not voice_part in parts:
                abort(422)

            singer_list = Singer.query.filter(Singer.voice_part == voice_part).all()

            return jsonify({
                'success': True,
                'overall pool': [ s.name for s in singer_list ]
            }), 200

        except Exception as e:
            print(e)


    @app.route('/singers/<int:id>/', methods=['PATCH'])
    def modify_singer(id):
        body = request.get_json()
        updated_singer = Singer.query.filter(Singer.id==id).one_or_none()

        if updated_singer is None:
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
            abort(422)


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

        try:
            choirs = Choir.query.all()

            return jsonify({
                'success': True,
                'choirs': [ choir.long() for choir in choirs ]
            }), 200

        except Exception as e:
            abort(422)


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
            abort(422)


    @app.route('/choirs/<int:id>', methods=['PATCH'])
    def update_choir(id):
        body = request.get_json()
        updated_choir = Choir.query.filter(Choir.id==id).one_or_none()

        if updated_choir is None:
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
            abort(422)


    @app.route('/choirs/<int:id>', methods=['DELETE'])
    def delete_choir(id):

        delete_choir = Choir.query.filter(Choir.id==id).one_or_none()

        if not delete_choir:
            abort(404)


        try:
            delete_choir.delete()

            return jsonify({
                'success': True,
                'removed choir': delete_choir.long()
            }), 200

        except Exception as e:
            print(e)
            abort(422)




     # who is in which choir, pass in choir id
    @app.route('/choir/<int:cid>', methods=['GET'])
    def list_singers_in_choir(cid):

        try:
            selected_choir = Choir.query.filter(Choir.id == cid).one_or_none()
            singers = Singer.query.with_entities(Singer).join(ChoirEnrollment).filter(ChoirEnrollment.choir_id == cid).all()
            SOPRANO, ALTO, TENOR, BASS = sort_by_voice_part(singers)

            return jsonify({
                'success': True,
                'Choir name': selected_choir.name,
                'voice_type': {
                    'SOPRANO': (None, SOPRANO)[len(SOPRANO) > 0],
                    'ALTO': (None, SOPRANO)[len(ALTO) > 0],
                    'TENOR': (None, TENOR)[len(TENOR) > 0],
                    'BASS': (None, BASS)[len(BASS) > 0]
                }
            }), 200

        except Exception as e:
            print(e)
            abort(404)


    #  query the enrolled singers and their voice part in specific choir
    @app.route('/choir/<int:cid>/<s_voice_part>', methods=['GET'])
    def choir_id_soprano(cid, s_voice_part):

        try:
            selected_choir = Choir.query.filter(Choir.id == cid).one_or_none()
            choir_part_result = Singer.query.with_entities(Singer).join(ChoirEnrollment).filter(
                ChoirEnrollment.choir_id == cid, Singer.voice_part == s_voice_part).all()

            return jsonify({
                'success': True,
                'Choir name': selected_choir.name,
                s_voice_part: [p.name for p in choir_part_result]
            }), 200

        except Exception as e:
            print(e)
            abort(404)


    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable_entity"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    return app


