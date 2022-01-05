from flask import Flask,render_template,request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import usefull_fonction as uf

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')



@app.route('/predict', methods=['POST'])
def predict():
    d = pd.read_csv("drug_consumption.data", header=None)
    d.drop([0], axis=1, inplace=True)
    d.drop([i for i in range(13,32)], axis=1, inplace=True)
    d.columns = ["Tranche_Age", "Genre", "Niveau_Education", "Pays", "Ethnie", 
                      "Nscore", "Escore",
                      "Oscore", "Ascore", "Cscore", "Impulsive", "SS"]
    
    d = uf.datapreprocessing(d)
    
    #Loading models 
    RF_heroin_model = open('RF_heroin_model.pkl','rb')
    rf_heroinPl_model = joblib.load(RF_heroin_model)
    
    SVC_ecstasy_model = open('SVC_ecstasy_model.pkl','rb')
    svc_ecstasy_model = joblib.load(SVC_ecstasy_model)
    
    SVC_benzo_model = open('SVC_benzo_model.pkl','rb')
    svc_benzo_model = joblib.load(SVC_benzo_model)

    if request.method == 'POST':
        message = request.form['message']
        split_message = message.split(';')
        dict_message = {k:v for k,v in zip(d.columns, split_message)}
        dict_message_mef = uf.miseEnForme(dict_message)
        d = d.append(dict_message_mef, ignore_index= True)
        d = pd.get_dummies(columns=["Tranche_Age", "Genre", "Niveau_Education"], data = d)
        to_test = d.tail(1)
        d.drop([1885] , inplace=True)
        
        #prediction for rf model
        
        my_prediction = rf_heroinPl_model.predict(to_test)
        
        #scaling 

        scaler = StandardScaler()
        scaler.fit(d.iloc[:,:7])
        d.iloc[:,:7] = scaler.transform(d.iloc[:,:7])
        to_test.iloc[:,:7] = scaler.transform(to_test.iloc[:,:7])
        
        #prediction for the svc models
        my_prediction2 = svc_ecstasy_model.predict(to_test)
        
        my_prediction3 = svc_benzo_model.predict(to_test)
        
        
    return render_template('result.html', prediction = my_prediction,
                           prediction2 = my_prediction2,
                           prediction3 = my_prediction3)


if __name__ == '__main__':
	app.run(debug=True)
