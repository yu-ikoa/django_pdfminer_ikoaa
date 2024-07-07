from django import forms
from django.conf import settings
from django.core.files.storage import default_storage
from upload_validator import FileTypeValidator
import os, random, string
from .custom_widgets import CustomClearableFileInput  # カスタムウィジェットをインポート


def create_dir(n):
    """一時フォルダ名生成関数"""
    return 'pdf/' + ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def save(uploaded_files):
    temp_dir = os.path.join(settings.MEDIA_ROOT, create_dir(10))  # 一時フォルダの生成
    for pdf in uploaded_files:
        default_storage.save(os.path.join(temp_dir, pdf.name), pdf)  # 一時フォルダにPDFを保存
    return temp_dir


class UploadForm(forms.Form):
    """PDFアップロード用フォームの定義
       saveメソッドはアップロードしたPDFを一時フォルダに保存する。
    """
    document = forms.FileField(label="PDFアップロード",
                               widget=CustomClearableFileInput(attrs={'multiple': True,
                                                                      'title': 'Choose PDF files to upload',
                                                                      # title属性を追加
                                                                      'placeholder': 'Select files'
                                                                      # placeholder属性を追加
                                                                      }),
                               validators=[FileTypeValidator(allowed_types=['application/pdf'])])
