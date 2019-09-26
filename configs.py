# Default Setting

# batch_size(배치 크기) = 64
# train_steps(학습 에포크) = 20000
# dropout_width(드랍아웃 크기) = 0.5
# layer_size(멀티 레이어 크기, multi RNN) = 3
# hidden_size(가중치 크기) = 128
# learning_rate(학습률) = 1e-3
# shiffle_seek(셔플 시드값) = 1000
# max_sequence_length(시퀀스 길이) = 25
# embedding_size(임베딩 크기) = 128
# tokenize_as_morph(형태소에 따른 토크나이징 사용 유무) = True
# embedding(임베딩 사용 유무) = True
# multilayer(멀티 RNN 사용 유무) = True
# data_path(데이터 위치), vocabulary_path(사전 위치), check_point_path(체크 포인트 위치)는 수정불가

import tensorflow as tf

batch_size = 64
train_steps = 20000
dropout_width = 0.5
layer_size = 3
hidden_size = 128
learning_rate = 1e-3
shiffle_seek = 1000
max_sequence_length = 25
embedding_size = 128
tokenize_as_morph = True
embedding = True
multilayer = True

tf.app.flags.DEFINE_string('f', '', 'kernel') #
tf.app.flags.DEFINE_integer('batch_size', batch_size, 'batch size') # 배치 크기
tf.app.flags.DEFINE_integer('train_steps', train_steps, 'train steps') # 학습 에포크
tf.app.flags.DEFINE_float('dropout_width', dropout_width, 'dropout width') # 드롭아웃 크기
tf.app.flags.DEFINE_integer('layer_size', layer_size, 'layer size') # 멀티 레이어 크기 (multi rnn)
tf.app.flags.DEFINE_integer('hidden_size', hidden_size, 'weights size') # 가중치 크기
tf.app.flags.DEFINE_float('learning_rate', learning_rate, 'learning rate') # 학습률
tf.app.flags.DEFINE_string('data_path', './../data_in/ChatBotData.csv', 'data path') #  데이터 위치
tf.app.flags.DEFINE_string('vocabulary_path', './data_out/vocabularyData.voc', 'vocabulary path') # 사전 위치
tf.app.flags.DEFINE_string('check_point_path', './data_out/check_point', 'check point path') # 체크 포인트 위치
tf.app.flags.DEFINE_integer('shuffle_seek', shiffle_seek, 'shuffle random seek') # 셔플 시드값
tf.app.flags.DEFINE_integer('max_sequence_length', max_sequence_length, 'max sequence length') # 시퀀스 길이
tf.app.flags.DEFINE_integer('embedding_size', embedding_size, 'embedding size') # 임베딩 크기
tf.app.flags.DEFINE_boolean('tokenize_as_morph', tokenize_as_morph, 'set morph tokenize') # 형태소에 따른 토크나이징 사용 유무
tf.app.flags.DEFINE_boolean('embedding', embedding, 'Use Embedding flag') # 임베딩 유무 설정
tf.app.flags.DEFINE_boolean('multilayer', multilayer, 'Use Multi RNN Cell') # 멀티 RNN 유무

# Define FLAGS
DEFINES = tf.app.flags.FLAGS