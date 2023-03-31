import requests
from flask import Flask, render_template,request
import tokenModule
import apikey
import translation

app = Flask(__name__)
#put your api key instead
data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey='+apikey.apikey).json()
total_max = len(data['articles'])

totaldata = []
for i in range(total_max):
    totaldata.append(tokenModule.get_tokens([data['articles'][i]['description']+" "+data['articles'][i]['title']]))
prediction=[]
for i in range(total_max):
    prediction.append(tokenModule.model.predict({'input_ids':totaldata[i]['input_ids'],'input_mask':totaldata[i]['attention_mask']}))
print("Done")
@app.route("/")
@app.route("/home/<page>")
def home(page=0):
    page = int(page)
    url = data['articles'][int(page)]['urlToImage']
    desc = data['articles'][int(page)]['description']
    title = data['articles'][int(page)]['title']
    return render_template('home.html',page=int(page),data=data['articles'][int(page)],url=url,desc=desc,title=title, max=total_max,pred=prediction,path="")

@app.route("/home/<page>/translate")
def translated(page=0):
    page = int(page)
    url = data['articles'][int(page)]['urlToImage']
    desc = translation.query(data['articles'][int(page)]['description'])
    title = translation.query(data['articles'][int(page)]['title'])
    return render_template('home.html',page=int(page),data=data['articles'][int(page)],url=url,title=title,desc=desc, max=total_max,pred=prediction,path="../")

if __name__=="__main__":
    app.run(debug=True)