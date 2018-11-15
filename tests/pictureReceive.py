from flask import request, Flask
import time
import pymysql
import os
app = Flask(__name__)

@app.route("/pictureUpload", methods=['POST'])
def pictureUpload():
    upload_file = request.files['file']
    old_file_name = upload_file.filename
    if upload_file:
        file_path = os.path.join('../src/pics', old_file_name)
        upload_file.save(file_path)
        db = pymysql.connect("localhost","root","123456","iotplatform")
        cursor = db.cursor()
        a = 'dsf'
        sql = "insert into picture(location) values(%s)",a
        try:
            cursor.execute("insert into picture(location) values(%s)",file_path[:30])
            db.commit()
        except:
            db.rollback()
        db.close()
        print('success')
        print('file saved to %s' % file_path)
        return 'success'
    else:
        return 'failed'


if __name__ == "__main__":
    app.run(host="0.0.0.0")