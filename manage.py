from flask import request, Flask, jsonify, send_from_directory
import time
import json
import pymysql
import os
app = Flask(__name__)

@app.route("/shareUpload", methods=['POST'])
def pictureUpload():
    upload_file = request.files['file']
    old_file_name = upload_file.filename
    if upload_file:
        file_path = os.path.join('./src/img', old_file_name)
        upload_file.save(file_path)
        db = pymysql.connect("localhost","root","123456","iotplatform")
        cursor = db.cursor()
        try:
            cursor.execute("insert into share values(null, %s, 1, '2016-1-1 1:1:1')",file_path[:30])
            db.commit()
        except:
            db.rollback()
        db.close()
        print('success')
        print('file saved to %s' % file_path)
        return 'success'
    else:
        return 'failed'

@app.route("/shareShow", methods=['GET'])
def shareShow1():
    db = pymysql.connect("localhost", "root", "123456", "iotplatform")
    cursor = db.cursor()
    try:
        cursor.execute("select user_ID, location, time from share order by ID desc")
        temp = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    re = {'list': []}
    for i in range(len(temp)):
        re['list'].append({'user_ID': temp[i][0], 'location': temp[i][1]});
    return jsonify(re);

@app.route("/shareShow/<path:sharePath>")
def shareShow2(sharePath):
    return send_from_directory('./',sharePath,as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0")