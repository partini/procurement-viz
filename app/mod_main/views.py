from flask import Blueprint, render_template
from app import mongo_utils
from geopy.geocoders import Nominatim

geolocator = Nominatim()
mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    procedure_types = mongo_utils.get_procedures()
    activities = mongo_utils.get_activities()

    categories = mongo_utils.get_categories()

    categories_by_date = mongo_utils.group_by_date()
    categories_chart_data = [{
                    'name': " Health",
                    'data': []
                }]
    for category in categories_by_date['result']:
        categories_chart_data.append({
            'name': category['_id']['name'],
            'data': []
        })

    for category in categories_by_date['result']:
        for cat in categories_chart_data:
            if category['_id']['name'] == cat['name']:
                cat['data'].append(category['count'])


    unique = {each['name']: each for each in categories_chart_data}.values()



    municipalities = mongo_utils.get_by_municipality()

    municipality_result = []
    for muni in municipalities:
        if muni['_id']['name']:
            # location = geolocator.geocode(cyrtranslit.to_latin(muni['_id']['name'].encode('utf-8')))
            # time.sleep(5)
            # if location:
            municipality_result.append({
              'numberOfContracts': muni['y'],
              'selia': muni['_id']['name'],
              'price': muni['y'],
              'name': muni['_id']['name'],
              'gjeresia': 0,
              'value': muni['y'],
              'gjatesia': 0
            })

    return render_template('index.html', procedure_types=procedure_types, activities=activities, categories=categories, categories_by_date=unique, municipality_result=municipality_result)
