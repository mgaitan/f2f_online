import os
import subprocess

from flask import Flask, url_for, redirect, request, jsonify

cmd_folder = os.path.dirname(os.path.abspath(__file__))
f2f_path = os.path.join(cmd_folder, 'lib', 'f2f.pl')
app = Flask(__name__, static_url_path='')


#2. Define needed routes here
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/api', methods=['GET', 'POST'])
def f2fb():
    if (request.method == 'POST' and request.is_xhr):

        cmd = ['perl', f2f_path,
               '--tab', request.form['tab']]

        base_indent = request.form['base-indent']
        if base_indent != u'-1':
            cmd.extend(['--base-indent', base_indent])
        dp = request.form['dp']
        if dp == u'8':
            cmd.extend(['--dp-to-star-kind', '8'])
        elif dp == u'dp':
            cmd.extend(['--dp-to-star-kind', 'dp'])

        p = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        output, error = p.communicate(input=request.form['source'])

        if request.form['lowercase'] == 'on':
            output = output.lower()

        return jsonify({'output': output, 'error': error})

    else:
        redirect('/')



#4. Main method for local developement
if __name__ == "__main__":
    app.run(debug=True)