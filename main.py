import joblib
from google.cloud import storage, aiplatform
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def upload_to_gcs(bucket_name='bucket-ol1', model_file='model.pkl'):
    # Kreiranje klijenta za komunikaciju s Cloud Storageom
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    #upload datoteke modela
    blob = bucket.blob(model_file)
    blob.upload_from_filename(model_file)

    print(f"Model je uspješno prenesen na: gs://{bucket_name}/{model_file}")

#korištenje DataFrame za vizualizaciju i upravljanje podacima
iot_data = pd.read_csv('weather_info_2023.csv')
iot_data['significant_prcp'] = iot_data['prcp'].apply(lambda x: 1 if x > 5 else 0)

print(iot_data.head(15))

#podjela podataka na podatke senzora i anomalijske podatke
X = iot_data[['temp', 'max', 'min', 'wdsp', 'dewp', 'slp', 'visib']]
y = iot_data['significant_prcp']

#podjela podataka na testne podatke i podatke za trening
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#kreiranje Decision Tree Classifiera i treniranje istog
model = DecisionTreeClassifier()

#treniranje podataka senzora X s podacima anomalija y
model.fit(X_train, y_train)
#kreiranje datoteke modela
joblib.dump(model, 'model2f.pkl')

#predviđanja prema testnim podacima
y_pred = model.predict(X_test)

#ocjena i procjena modela
accuracy = accuracy_score(y_test, y_pred) #usporedivanje točne vrijednosti y_test s predviđanjima y_pred
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)

#prenošenje modela na Google Cloud
upload_to_gcs()

instances = [
     {"temp": 26.1, "max": 18.4, "min": 15.5, "wdsp": 5.6, "dewp": 11.5, "slp": 1007.2, "visib": 15.6},
]