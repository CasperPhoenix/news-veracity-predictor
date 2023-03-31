import tensorflow as tf
from transformers import AutoTokenizer,TFBertModel
from tensorflow.keras.optimizers import Adam
model = tf.keras.models.load_model('fake_news_bert.h5',custom_objects={"TFBertModel": TFBertModel}, compile=False)
model.compile()
def get_tokens(X):
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    
    X = tokenizer(
                text = list(X),
                add_special_tokens = True,
                max_length = 128,
                truncation = True,
                padding = 'max_length',
                return_tensors = 'tf',
                return_token_type_ids = False,
                return_attention_mask = True,
                verbose = True
                )
    
    return X

