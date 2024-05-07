from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def index_form(request):
    if request.method == "POST":
        long_url = request.POST.get('long_url')
        new_url = shorten_url(long_url)

        return render(request, "home/new_url.html", context={"url": new_url})
    return render(request, "home/index.html")

def shorten_url(url):
    headers = {
        'Authorization': 'Bearer 37018472cb8ac861f78446007f92e7be857bb430', 
        # 'Authorization': 'Bearer {TOKEN}', 
        'Content-Type': 'application/json', 
    }
    data_dict = {"long_url": url, "domain": "bit.ly"} 

    # convert data_dict to json 
    data = json.dumps(data_dict) 

    response = requests.post( 
        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data) 
  
    # convert json string to dict 
    response_dict = json.loads(response.text) 
  
    print(response_dict) 
    return response_dict['link'] 