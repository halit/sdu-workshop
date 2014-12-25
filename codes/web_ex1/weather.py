from bottle import route, run, template
import requests

site_url = "http://api.openweathermap.org/data/2.5/weather?q={city}"

@route('/weather/<city>')
def index(city):
    result = requests.get(site_url.format(city=city)).json()
    return template("weather", result=dict(result))

if __name__ == "__main__":
    run(host='localhost', port=8080)