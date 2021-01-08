from django.shortcuts import render

# Create your views here.
def home(request):
  import json
  import requests

  if request.method == "POST":
    zipcode = request.POST['zipcode']
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zipcode+'&distance=5&API_KEY=6C934D4B-5822-4636-BB20-A3655BC270A0')

    try:
      api = json.loads(api_request.content)

      if api[0]['Category']['Name'] == "Good":
        category_color = 'good'
        category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little o no risk.'
      
      elif api[0]['Category']['Name'] == "Moderate":
        category_color = 'moderate'
        category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
      
      elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        category_color = 'usg'
        category_description = '(101 - 150) Althought general public is not likely to be affected at this AQI range, people with lung disease, older adult and children are at a greater risk from exposure to ozone, wheras persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
      
      elif api[0]['Category']['Name'] == "Unhealthy":
        category_color = 'unhealthy'
        category_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
      
      elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_color = 'veryunhealthy'
        category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
      
      elif api[0]['Category']['Name'] == "Hazardous":
        category_color = 'hazardous'
        category_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected.'

    except Exception as e:
      api = 'Error...'

    return render(request, 'home.html', {
      'api': api,
      'category_color': category_color,
      'category_description': category_description
    })

  else :
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=6C934D4B-5822-4636-BB20-A3655BC270A0')

    try:
      api = json.loads(api_request.content)

      if api[0]['Category']['Name'] == "Good":
        category_color = 'good'
        category_description = '(0 - 50) Air quality is considered satisfactory, and air pollution poses little o no risk.'
      
      elif api[0]['Category']['Name'] == "Moderate":
        category_color = 'moderate'
        category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
      
      elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        category_color = 'usg'
        category_description = '(101 - 150) Althought general public is not likely to be affected at this AQI range, people with lung disease, older adult and children are at a greater risk from exposure to ozone, wheras persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
      
      elif api[0]['Category']['Name'] == "Unhealthy":
        category_color = 'unhealthy'
        category_description = '(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
      
      elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_color = 'veryunhealthy'
        category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
      
      elif api[0]['Category']['Name'] == "Hazardous":
        category_color = 'hazardous'
        category_description = '(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected.'

    except Exception as e:
      api = 'Error...'

    return render(request, 'home.html', {
      'api': api,
      'category_color': category_color,
      'category_description': category_description
    })
  
def about(request):
  return render(request, 'about.html', {})