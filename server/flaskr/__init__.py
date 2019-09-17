import os

from flask import Flask, request, g
import pymysql

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect("aliasMeToDB","viper","viper67","IXPlus")

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/addsegment')
    def addSegment():
        segment = request.args.get('segment')
        pid     = request.args.get('pid')
        if not segment or not pid:
            return "no segment or no pid", 400
        else:
            add_PID_segment(pid, segment)
            return "{}, {}".format(segment, pid)

    return app

def add_PID_segment(pid, segmentID):
    db = get_db()
    cursor = db.cursor()

    sql = "INSERT INTO PIDSegmentMappings(PID, segmentID, count) \
           VALUES('%s', '%s', 1) \
           ON DUPLICATE KEY UPDATE count = count + 1" % \
                   (pid, segmentID)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
