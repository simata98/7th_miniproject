from django.shortcuts import render
from django.utils import timezone
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
from keras.models import load_model
import os
from pathlib import Path


# from pybo.model import Result
from .models import Result

# Create your views here.

logger = logging.getLogger('mylogger')

def index(request):
    return render(request, 'language/index.html')

def upload(request):
    if request.method == 'POST' and request.FILES['files']:
        #todo form에서 전송한 파일을 획득한다.
        file = request.FILES['files']
        # class names 준비
        class_names = list(string.ascii_lowercase)
        class_names = np.array(class_names)
        mapping = {i:s for i, s in enumerate(class_names)}

        #todo 모델 로딩
        model_path = os.path.join(Path(__file__).resolve().parent, "model/CNN_second.h5")
        model = load_model(model_path)
        
        #todo history 저장을 위해 객체에 담아서 DB에 저장한다.
        # 이때 파일시스템에 저장도 된다.
        result = Result()
        result.answer = request.POST.get('answer', '')
        result.image = file
        result.pub_date = timezone.datetime.now()
        result.save()
        
        img = cv2.imread(result.image.path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28, 28))
        img = img/255
        img = img.reshape(-1, 28, 28, 1)
        
        img_pred = model.predict(img)
        
        #todo 예측 결과를 DB에 저장한다.
        result.result = mapping[int(np.argmax(img_pred, axis=1))]
        result.save()

        context = {
            'result': result,
        }


    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠.
    else:
        test = request.GET['test']
        logger.error(('Something went wrong!!',test))

    return render(request, 'language/result.html', context)    

