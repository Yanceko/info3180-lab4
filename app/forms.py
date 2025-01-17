from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename


class UploadForm(FlaskForm):
    pict = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Please Upload Image!')])