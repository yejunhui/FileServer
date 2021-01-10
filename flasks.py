from flask import Flask,render_template,redirect,request,url_for
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index(tisp=''):
    data = {}

    if 'flies' not in os.listdir(os.getcwd()):
        os.mkdir(os.getcwd() + '/flies/')

    data['path'] = os.getcwd()+'/files'
    if request.method == 'POST':
        f = request.files['file']
        upload_path = os.getcwd()+'/flies/'+secure_filename(f.filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        data['tisp'] = '<'+secure_filename(f.filename)+'>上传成功'
        return redirect(url_for('index',tisp=data['tisp']))
    else:
        data['tisp'] = request.args.get('tisp')
        return render_template('file.html',data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=303,debug=True)