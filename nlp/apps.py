from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf 
import tensorflow_text as text 


class NlpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nlp'
    model_path = settings.MODELS
    loaded_model = tf.saved_model.load(model_path)