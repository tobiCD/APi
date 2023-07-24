import requests

api_key="e2440514fabe9f7a12b1b87470346057"

def get_data(place , forecast=None , kind=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    reponse=requests.get(url)
    data=reponse.json()
    filtered_data=data['list']
    nr_values=8*forecast
    filtered_data=filtered_data[:nr_values]
    return filtered_data
if __name__=="__main__":

    print(get_data(place="Tokyo",forecast=3))


