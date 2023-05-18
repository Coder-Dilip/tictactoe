
# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render



def index(request):
    return render(request,'predict.html')


import ast
def predict(request):
    import tensorflow as tf
    import numpy as np

    input_array = request.GET['input_array']
    input_array=ast.literal_eval(input_array)
    print(input_array)
    game = tf.keras.models.load_model('myModel2')
    predict = game.predict(np.array([input_array]))
    prediction = int(np.argmax(predict))


    response_data = {
        'prediction': prediction
    }

    return HttpResponse(json.dumps(response_data), content_type='application/json')