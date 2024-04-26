import os


Usa_house_price_prediction = """
# # Download CSV from -> https://rb.gy/rogm9q

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv('USA_Housing.csv')
df

df.dtypes

x = df.drop(['Price', 'Address'], axis=1)
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
print(mse)

plt.scatter(y_test, y_pred)
plt.xlabel('actual')
plt.ylabel('predcited')
plt.title('act vs pred')
plt.show()
"""

multi_class_cnn_with_conf_matrix = """
!pip install tensorflow
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Data Preprocessing
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

# Predict on the test set
y_pred = np.argmax(model.predict(X_test), axis=-1)
y_true = np.argmax(y_test, axis=-1)

# Create confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt='g', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()
"""

rnn_variant_lstm_gru = """
!pip install tensorflow
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense

# Load the IMDb dataset
num_words = 10000  # Only consider the top 10,000 most common words
max_len = 200  # Limit the length of each review to 200 words
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# Pad sequences to make them all of the same length
x_train = pad_sequences(x_train, maxlen=max_len)
x_test = pad_sequences(x_test, maxlen=max_len)

# Define the LSTM model
model = Sequential([
    Embedding(input_dim=num_words, output_dim=128, input_length=max_len),
    LSTM(units=128),
    Dense(units=1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print("Test Accuracy:", accuracy)
"""

cnn_image_for_classification = """
!pip install tensorflow

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values to be between 0 and 1
x_train = x_train / 255.0
x_test = x_test / 255.0

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),  # Dropout regularization to prevent overfitting
    Dense(10, activation='softmax')
])

# Compile the model
learning_rate = 0.001  # Set learning rate hyperparameter
optimizer = Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print("Test Accuracy:", accuracy)
"""

convolutional_gan = """
!pip install tensorflow
# code % matplotlib inline
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from IPython import display

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
x_train.shape, x_test.shape

# We plot first 25 images of training dataset
plt.figure(figsize =(10, 10))
for i in range(25):
	plt.subplot(5, 5, i + 1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(x_train[i], cmap = plt.cm.binary)
plt.show()

# code
batch_size = 32
# This dataset fills a buffer with buffer_size elements,
# then randomly samples elements from this buffer, 
# replacing the selected elements with new elements.
def create_batch(x_train):
    dataset = tf.data.Dataset.from_tensor_slices(x_train).shuffle(1000)
# Combines consecutive elements of this dataset into batches.

    dataset = dataset.batch(batch_size, drop_remainder = True).prefetch(1)
# Creates a Dataset that prefetches elements from this dataset
    return dataset

# code
num_features = 100

generator = keras.models.Sequential([
	keras.layers.Dense(7 * 7 * 128, input_shape =[num_features]),
	keras.layers.Reshape([7, 7, 128]),
	keras.layers.BatchNormalization(),
	keras.layers.Conv2DTranspose(
		64, (5, 5), (2, 2), padding ="same", activation ="selu"),
	keras.layers.BatchNormalization(),
	keras.layers.Conv2DTranspose(
		1, (5, 5), (2, 2), padding ="same", activation ="tanh"),
])
generator.summary()

discriminator = keras.models.Sequential([
	keras.layers.Conv2D(64, (5, 5), (2, 2), padding ="same", input_shape =[28, 28, 1]),
	keras.layers.LeakyReLU(0.2),
	keras.layers.Dropout(0.3),
	keras.layers.Conv2D(128, (5, 5), (2, 2), padding ="same"),
	keras.layers.LeakyReLU(0.2),
	keras.layers.Dropout(0.3),
	keras.layers.Flatten(),
	keras.layers.Dense(1, activation ='sigmoid')
])
discriminator.summary()

discriminator = keras.models.Sequential([
	keras.layers.Conv2D(64, (5, 5), (2, 2), padding ="same", input_shape =[28, 28, 1]),
	keras.layers.LeakyReLU(0.2),
	keras.layers.Dropout(0.3),
	keras.layers.Conv2D(128, (5, 5), (2, 2), padding ="same"),
	keras.layers.LeakyReLU(0.2),
	keras.layers.Dropout(0.3),
	keras.layers.Flatten(),
	keras.layers.Dense(1, activation ='sigmoid')
])
discriminator.summary()

# compile discriminator using binary cross entropy loss and adam optimizer
discriminator.compile(loss ="binary_crossentropy", optimizer ="adam")
# make discriminator no-trainable as of now
discriminator.trainable = False
# Combine both generator and discriminator
gan = keras.models.Sequential([generator, discriminator])
# compile generator using binary cross entropy loss and adam optimizer

gan.compile(loss ="binary_crossentropy", optimizer ="adam")

seed = tf.random.normal(shape =[batch_size, 100])

def train_dcgan(gan, dataset, batch_size, num_features, epochs = 5):
	generator, discriminator = gan.layers
	for epoch in tqdm(range(epochs)):
		print()
		print("Epoch {}/{}".format(epoch + 1, epochs))

		for X_batch in dataset:
			# create a random noise of sizebatch_size * 100
			# to passit into the generator
			noise = tf.random.normal(shape =[batch_size, num_features])
			generated_images = generator(noise)

			# take batch of generated image and real image and
			# use them to train the discriminator
			X_fake_and_real = tf.concat([generated_images, X_batch], axis = 0)
			y1 = tf.constant([[0.]] * batch_size + [[1.]] * batch_size)
			discriminator.trainable = True
			discriminator.train_on_batch(X_fake_and_real, y1)

			# Here we will be training our GAN model, in this step
			# we pass noise that uses generatortogenerate the image
			# and pass it with labels as [1] So, it can fool the discriminator
			noise = tf.random.normal(shape =[batch_size, num_features])
			y2 = tf.constant([[1.]] * batch_size)
			discriminator.trainable = False
			gan.train_on_batch(noise, y2)

			# generate images for the GIF as we go
			generate_and_save_images(generator, epoch + 1, seed)

	generate_and_save_images(generator, epochs, seed)

# code
def generate_and_save_images(model, epoch, test_input):
    predictions = model(test_input, training = False)
    fig = plt.figure(figsize =(10, 10))

    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap ='binary')
        plt.axis('off')

    plt.savefig('image_epoch_{:04d}.png'.format(epoch))

# reshape to add a color map
x_train_dcgan = x_train.reshape(-1, 28, 28, 1) * 2. - 1.
# create batches
dataset = create_batch(x_train_dcgan)
# callthe training function with 10 epochs and record time %% time
train_dcgan(gan, dataset, batch_size, num_features, epochs = 10)

import imageio
import glob

anim_file = 'dcgan_results.gif'

with imageio.get_writer(anim_file, mode ='I') as writer:
    filenames = glob.glob('image*.png')
    filenames = sorted(filenames)
    last = -1
for i, filename in enumerate(filenames):
	frame = 2*(i)
	if round(frame) > round(last):
		last = frame
	else:
		continue
	image = imageio.imread(filename)
	writer.append_data(image)
image = imageio.imread(filename)
writer.append_data(image)
display.Image(filename = anim_file)
"""

sentiment_analysis = """
!pip install tensorflow

from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Bidirectional, Dense, Embedding
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
import numpy as np

# Getting reviews with words that come under 5000
# most occurring words in the entire
# corpus of textual review data
vocab_size = 5000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

print(x_train[0])
#These are the index values of the words and hence we done see any reviews 

# Getting all the words from word_index dictionary
word_idx = imdb.get_word_index()

# Originally the index number of a value and not a key,
# hence converting the index as key and the words as values
word_idx = {i: word for word, i in word_idx.items()}

# again printing the review
print([word_idx[i] for i in x_train[0]])

# Get the minimum and the maximum length of reviews
print("Max length of a review:: ", len(max((x_train+x_test), key=len)))
print("Min length of a review:: ", len(min((x_train+x_test), key=len)))

from tensorflow.keras.preprocessing import sequence

# Keeping a fixed length of all reviews to max 400 words
max_words = 400

x_train = sequence.pad_sequences(x_train, maxlen=max_words)
x_test = sequence.pad_sequences(x_test, maxlen=max_words)

x_valid, y_valid = x_train[:64], y_train[:64]
x_train_, y_train_ = x_train[64:], y_train[64:]

# fixing every word's embedding size to be 32
embd_len = 32

# Creating a RNN model
RNN_model = Sequential(name="Simple_RNN")
RNN_model.add(Embedding(vocab_size,
						embd_len,
						input_length=max_words))

# In case of a stacked(more than one layer of RNN)
# use return_sequences=True
RNN_model.add(SimpleRNN(128,
						activation='tanh',
						return_sequences=False))
RNN_model.add(Dense(1, activation='sigmoid'))

# printing model summary
print(RNN_model.summary())

# Compiling model
RNN_model.compile(
	loss="binary_crossentropy",
	optimizer='adam',
	metrics=['accuracy']
)

# Training the model
history = RNN_model.fit(x_train_, y_train_,
						batch_size=64,
						epochs=5,
						verbose=1,
						validation_data=(x_valid, y_valid))

# Printing model score on test data
print()
print("Simple_RNN Score---> ", RNN_model.evaluate(x_test, y_test, verbose=0))

# Defining LSTM model
lstm_model = Sequential(name="LSTM_Model")
lstm_model.add(Embedding(vocab_size,
						embd_len,
						input_length=max_words))
lstm_model.add(LSTM(128,
					activation='relu',
					return_sequences=False))
lstm_model.add(Dense(1, activation='sigmoid'))

# Printing Model Summary
print(lstm_model.summary())

# Compiling the model
lstm_model.compile(
	loss="binary_crossentropy",
	optimizer='adam',
	metrics=['accuracy']
)

# Training the model
history3 = lstm_model.fit(x_train_, y_train_,
						batch_size=64,
						epochs=5,
						verbose=2,
						validation_data=(x_valid, y_valid))

# Displaying the model accuracy on test data
print()
print("LSTM model Score---> ", lstm_model.evaluate(x_test, y_test, verbose=0))
"""

data_classification_algorithm = """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data 
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression() 

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

species_names = iris.target_names[y]

sepal_length = X[:, 0]
sepal_width = X[:, 1]

setosa_data = (sepal_length[y == 0], sepal_width[y == 0])
versicolor_data = (sepal_length[y == 1], sepal_width[y == 1])
virginica_data = (sepal_length[y == 2], sepal_width[y == 2])

plt.figure(figsize=(8, 6))

plt.scatter(*setosa_data, label="setosa", color='black')
plt.scatter(*versicolor_data, label="versicolor", color='red')
plt.scatter(*virginica_data, label="virginica", color='orange')

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Sepal Measurements Colored by Species")
plt.legend()
plt.grid(True)

plt.show()
"""

data_clustering_algorithm = """
!pip install seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
from sklearn.cluster import KMeans

iris = datasets.load_iris()
print("Dataset loaded successfully")

#Creating data frame 
Data = pd.DataFrame(iris.data, columns = iris.feature_names)

#Top values of Dataset
Data.head()


#Bottom Values of Dataset
Data.tail()

Data.shape

Data.info()

Data.describe()

sns.heatmap(Data.corr(), annot = True, linecolor='black')

Data.hist()
plt.show()

# Setting the data
x=Data.iloc[:,0:3].values

css=[]

# Finding inertia on various k values
for i in range(1,8):
    kmeans=KMeans(n_clusters = i, init = 'k-means++', 
                    max_iter = 100, n_init = 10, random_state = 0).fit(x)
    css.append(kmeans.inertia_)
    
plt.plot(range(1, 8), css, 'bx-', color='black')
plt.title('The elbow method') #The Elbow method is one of the most popular ways to find the optimal number of clusters.
plt.xlabel('Number of clusters')
plt.ylabel('CSS') 
plt.show()

#Applying Kmeans classifier
kmeans = KMeans(n_clusters=3,init = 'k-means++', max_iter = 100, n_init = 10, random_state = 0)

y_kmeans = kmeans.fit_predict(x)

kmeans.cluster_centers_

# Visualising the clusters - On the first two columns
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], 
            s = 100, c = 'green', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], 
            s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],
            s = 100, c = 'red', label = 'Iris-virginica')

# Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], 
            s = 100, c = 'pink', label = 'Centroids')

plt.legend()

"""

data_visualization_and_ETL = """
!pip install seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris_df.head())

# Transformation: Group by species and calculate mean of sepal_length
species_sepal_length_mean = iris_df.groupby('species')['sepal_length'].mean().reset_index()

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=species_sepal_length_mean, x='species', y='sepal_length')
plt.title('Mean Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Mean Sepal Length')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species', palette='viridis')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.grid(True)
plt.show()

"""

import_data_and_load_in_target_system = """
# Download data from (heart.csv) -> https://rb.gy/kteskv
!pip install flask flask_sqlalchemy 

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HeartData(db.Model):
    __tablename__ = 'heart_data'  # Ensures the table name is explicitly set
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    Age = db.Column(db.Float)
    Sex = db.Column(db.Float)
    ChestPainType = db.Column(db.Float)
    RestingBP = db.Column(db.Float)
    Cholesterol = db.Column(db.Float)
    FastingBS = db.Column(db.Float)
    RestingECG = db.Column(db.Float)
    MaxHR = db.Column(db.Float)
    ExerciseAngina = db.Column(db.Float)
    Oldpeak = db.Column(db.Float)
    ST_Slope = db.Column(db.Float)
    HeartDisease = db.Column(db.Float)

    def __repr__(self):
        return f'<HeartData {self.id}>'

def load_data_from_csv(csv_file):
    with app.app_context():
        data = pd.read_csv(csv_file)
        data.reset_index(inplace=True)  # Reset index to create an automatic 'index' column
        data.rename(columns={'index': 'id'}, inplace=True)  # Rename 'index' column to 'id'
        data.to_sql('heart_data', db.engine, index=False, if_exists='replace')  # 'index=False' avoids creating an extra unnamed column

@app.route('/')
def index():
    return 'Flask App with SQLAlchemy'

@app.route('/data')
def view_data():
    heart_data = HeartData.query.all()
    data = [{
        'Age': entry.Age,
        'Sex': entry.Sex,
        'ChestPainType': entry.ChestPainType,
        'RestingBP': entry.RestingBP,
        'Cholesterol': entry.Cholesterol,
        'FastingBS': entry.FastingBS,
        'RestingECG': entry.RestingECG,
        'MaxHR': entry.MaxHR,
        'ExerciseAngina': entry.ExerciseAngina,
        'Oldpeak': entry.Oldpeak,
        'ST_Slope': entry.ST_Slope,
        'HeartDisease': entry.HeartDisease
    } for entry in heart_data]

    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drop all tables
        db.create_all()  # Create tables based on model definitions
        load_data_from_csv('heart.csv')
    app.run(debug=True)
"""

etl_in_sql_server = """
!pip install flask flask_sqlalchemy 
# Download data from (heart.csv) -> https://rb.gy/kteskv

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HeartData(db.Model):
    __tablename__ = 'heart_data'
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.Float)
    Sex = db.Column(db.Float)
    ChestPainType = db.Column(db.Float)
    RestingBP = db.Column(db.Float)
    Cholesterol = db.Column(db.Float)
    FastingBS = db.Column(db.Float)
    RestingECG = db.Column(db.Float)
    MaxHR = db.Column(db.Float)
    ExerciseAngina = db.Column(db.Float)
    Oldpeak = db.Column(db.Float)
    ST_Slope = db.Column(db.Float)
    HeartDisease = db.Column(db.Float)

class TransformedHeartData(db.Model):
    __tablename__ = 'transformed_heart_data'
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.Float)
    MaxHR_Age_Ratio = db.Column(db.Float)
    NormalizedCholesterol = db.Column(db.Float)

def load_data_from_csv(csv_file):
    with app.app_context():
        data = pd.read_csv(csv_file)
        data.reset_index(inplace=True)  # Reset index to create an automatic 'index' column
        data.rename(columns={'index': 'id'}, inplace=True)  # Rename 'index' column to 'id'
        data.to_sql('heart_data', db.engine, index=False, if_exists='replace')  # 'index=False' avoids creating an extra unnamed column

def transform_data():
    # Extract
    df = pd.read_sql('heart_data', db.engine)

    # Transform
    df['MaxHR_Age_Ratio'] = df['MaxHR'] / df['Age']
    df['NormalizedCholesterol'] = (df['Cholesterol'] - df['Cholesterol'].mean()) / df['Cholesterol'].std()

    # Ensure the 'id' column is preserved in the transformed DataFrame
    transformed_df = df[['id', 'Age', 'MaxHR_Age_Ratio', 'NormalizedCholesterol']]
    
    # Load
    transformed_df.to_sql('transformed_heart_data', db.engine, index=False, if_exists='replace', index_label='id')

@app.route('/')
def index():
    return 'Flask App with SQLAlchemy'

@app.route('/data')
def view_data():
    heart_data = HeartData.query.all()
    data = [{column.name: getattr(entry, column.name) for column in entry.__table__.columns} for entry in heart_data]
    return jsonify(data)

@app.route('/ETL')
def view_transformed_data():
    transformed_data = TransformedHeartData.query.all()
    data = [{column.name: getattr(entry, column.name) for column in entry.__table__.columns} for entry in transformed_data]
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drop all tables for demonstration purposes
        db.create_all()  # Create all tables based on models
        load_data_from_csv('heart.csv')
        transform_data()  # Perform ETL
    app.run(debug=True)
"""

map_reduce_to_generate_grades_of_students = """
Step 1: Generate CSV file of students with marks:


import csv
import random

# Generate random student data
def generate_student_data(num_students):
    students = []
    for i in range(1, num_students + 1):
        name = f"Student{i}"
        math_score = random.randint(60, 100)
        science_score = random.randint(60, 100)
        english_score = random.randint(60, 100)
        students.append([name, math_score, science_score, english_score])
    return students

# Write student data to CSV file
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math Score", "Science Score", "English Score"])
        writer.writerows(data)

# Number of students
num_students = 50

# Generate student data
students_data = generate_student_data(num_students)

# Write data to CSV file
csv_filename = "student_data.csv"
write_to_csv(csv_filename, students_data)

print(f"CSV file '{csv_filename}' generated successfully!")


Step 2 :MapReduce program to find the grades of students

from mrjob.job import MRJob

class StudentGrade(MRJob):

    def mapper(self, _, line):
        # Split the line into fields
        fields = line.split(',')
        name = fields[0]
        math_score = int(fields[1])
        science_score = int(fields[2])
        english_score = int(fields[3])
        
        # Calculate total score and average
        total_score = math_score + science_score + english_score
        average_score = total_score / 3
        
        # Assign grades based on average score
        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        # Emit student name and grade
        yield name, grade

    def reducer(self, name, grades):
        # Output student name and final grade
        yield name, list(grades)[0]

if _name_ == '_main_':
    StudentGrade.run()
"""

mapreduce_to_calculate_freq_of_given_word_in_file = """
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequency(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if _name_ == '_main_':
    MRWordFrequency.run()
This code defines a MapReduce job using mrjob. Here's what each part does:

WORD_RE: Regular expression pattern to extract words from each line of the input.
mapper: This function takes a line from the input file and yields key-value pairs where the key is a word and the value is 1 (indicating that the word occurred once).
reducer: This function receives key-value pairs from the mapper, where the key is a word and the values are counts of occurrences. It sums up the counts for each word and yields the final word frequency.
To run this MapReduce job on your local machine, save the code to a file (e.g., word_frequency.py) and run the following command in your terminal:

Copy code
python word_frequency.py your_input_file.txt
Replace your_input_file.txt with the path to your input file. The output will display the frequency of each word in the file.
"""

mapreduce_for_mat_multiplication = """
from mrjob.job import MRJob
from mrjob.step import MRStep

class MatrixMultiplication(MRJob):

    def mapper_multiply(self, _, line):
        # Split the line into matrix name, row, column, and value
        matrix_name, i, j, value = line.split(',')
        i = int(i)
        j = int(j)
        value = int(value)

        # Emit intermediate key-value pairs for multiplication
        if matrix_name == 'A':
            for k in range(self.matrix_b_columns):
                yield (i, k), (j, value)
        else:
            for k in range(self.matrix_a_rows):
                yield (k, j), (i, value)

    def reducer_multiply(self, key, values):
        # Initialize a dictionary to store the partial result
        result = {}
        for index, value in values:
            if index in result:
                result[index] += value
            else:
                result[index] = value

        # Emit the final key-value pair
        yield key, sum(result.values())

    def steps(self):
        # Determine the dimensions of the matrices
        self.matrix_a_rows = 2  # Change this to the number of rows in matrix A
        self.matrix_a_columns = 2  # Change this to the number of columns in matrix A
        self.matrix_b_rows = 2  # Change this to the number of rows in matrix B
        self.matrix_b_columns = 2  # Change this to the number of columns in matrix B

        return [
            MRStep(mapper=self.mapper_multiply, reducer=self.reducer_multiply)
        ]

if _name_ == '_main_':
    MatrixMultiplication.run()
This code defines a MapReduce job using mrjob to perform matrix multiplication. Here's a breakdown of how it works:

mapper_multiply: This mapper function reads lines from the input files, which are assumed to be in the format "matrix_name, row, column, value". It emits intermediate key-value pairs where the key is a tuple (i, k) for matrix A and (k, j) for matrix B, and the value is a tuple (j, value) for matrix A and (i, value) for matrix B.
reducer_multiply: This reducer function receives the intermediate key-value pairs from the mappers. It aggregates the values for each key, performing the multiplication for the corresponding elements of the matrices, and emits the final result as a key-value pair.
steps: This method defines the steps of the MapReduce job. In this case, there is only one step, which consists of the mapper and reducer functions for matrix multiplication.
You can run this code on your local machine by saving it to a file (e.g., matrix_multiplication.py) and running the following command in your terminal:

Copy code
python matrix_multiplication.py input_matrix_A.csv input_matrix_B.csv > output_matrix_C.csv
Replace input_matrix_A.csv and input_matrix_B.csv with the paths to your input matrices. The output will be written to output_matrix_C.csv, which will contain the result of the matrix multiplication.   csv for input input_matrix_A.csv:

css
Copy code
A,0,0,1
A,0,1,2
A,1,0,3
A,1,1,4
input_matrix_B.csv:

css
Copy code
B,0,0,5
B,0,1,6
B,1,0,7
B,1,1,8
"""


masterDict = {
    "Usa_house_price_prediction": Usa_house_price_prediction,
    "multi_class_cnn_with_conf_matrix": multi_class_cnn_with_conf_matrix,
    "rnn_variant_lstm_gru": rnn_variant_lstm_gru,
    "cnn_image_for_classification": cnn_image_for_classification,
    "convolutional_gan": convolutional_gan,
    "sentiment_analysis": sentiment_analysis,
    "data_classification_algorithm": data_classification_algorithm,
    "data_clustering_algorithm": data_clustering_algorithm,
    "data_visualization_and_ETL": data_visualization_and_ETL,
    "import_data_and_load_in_target_system": import_data_and_load_in_target_system,
    "etl_in_sql_server":etl_in_sql_server,
    "map_reduce_to_generate_grades_of_students": map_reduce_to_generate_grades_of_students,
    "mapreduce_to_calculate_freq_of_given_word_in_file": mapreduce_to_calculate_freq_of_given_word_in_file,
    
}


class Writer:
    def __init__(self, filename):
        self.filename = os.path.join(os.getcwd(), filename)
        self.masterDict = masterDict
        self.questions = list(masterDict.keys())

    def getCode(self, input_string):
        input_string = self.masterDict[input_string]
        with open(self.filename, "w") as file:
            file.write(input_string)
        print(f"##############################################")


if __name__ == "__main__":
    write = Writer("output.txt")
    print(write.questions)
    # write.getCode("rpc")
