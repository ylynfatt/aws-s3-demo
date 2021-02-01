from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
import boto3
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
AWS_BUCKET = 'coders-toolkit-aws-demo' # Change this to your Bucket name

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/s3-upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Let's use Amazon S3
        s3 = boto3.resource('s3')

        # Upload files to Amazon S3
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            s3.Bucket(AWS_BUCKET).put_object(Key=filename, Body=file)

            flash('File Successfully uploaded')
            return redirect(url_for('files'))
    return render_template('upload.html')

@app.route("/s3-files", methods=["GET"])
def files():
    # Let's use Amazon S3
    s3 = boto3.resource('s3')

    # Print out bucket names
    # for bucket in s3.buckets.all():
    #     print(bucket.name)

    # Get files from Bucket
    contents = []
    for item in s3.Bucket(AWS_BUCKET).objects.all():
        contents.append(item)
    app.logger.info(contents)
    return render_template('list.html', files=contents)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)