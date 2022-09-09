from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .apps import NlpConfig
import json
from tensorflow import sigmoid

# Create your views here.
@api_view(['GET', 'POST'])
def sentiment(request):
    if request.method == 'POST':
        predictor = NlpConfig.loaded_model
        data = request.data 
        inputs = data['inputs']
        inference = sigmoid(predictor(inputs)).numpy().tolist()
        outputs = []
        for i in range(len(inference)):
            input_text = inputs[i]
            if inference[i][0] >= 0.5:
                sentiment_predict = 'Positive'
                probability = inference[i][0]
            else:
                sentiment_predict = 'Negative'
                probability = 1 - inference[i][0]
            output = {
                "input": input_text,
                "sentiment": sentiment_predict,
                "probability": probability
            }
            outputs.append(output)

        return Response(outputs)
    return Response({'error': "The api only supports POST operation!"})