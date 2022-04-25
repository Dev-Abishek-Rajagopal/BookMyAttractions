from planaday_developer_test.attractions.models import Attraction

ATTRACTIONS = [
    {
        'name': 'Helicopter Tour - Day Flight',
        'description': 'Experience Las Vegas from above during the day',
    },
    {
        'name': 'Helicopter Tour - Night Flight',
        'description': 'Experience Las Vegas from above during after dark',
    },
    {
        'name': 'Magic Show',
        'description': 'This show will make your boredom vanish',
    },
    {
        'name': 'Circus of the Sun',
        'description': 'French Acrobats showing off their talents',
    },
    {
        'name': 'The Ferris Wheel',
        'description': 'Spend 10 minutes going in a circle... how fun.',
    },
]

def run():
    print("--------------------")
    print("POPULATING ATTRACTIONS")
    print("--------------------")
    print("--------------------")
    print("--------------------")
    if Attraction.objects.count() < 5:
        print("CREATING TEST ATTRACTIONS")
        print("--------------------")
        for a in ATTRACTIONS:
            attraction, cr = Attraction.objects.get_or_create(name=a['name'], description=a['description'])
            if cr:
                attraction.save()
                print(f"CREATED ATTRACTION: {attraction.name}")
                print("--------------------")
    else:
        print("TEST ATTRACTIONS EXIST")

    print("--------------------")
    print("--------------------")
    print("COMPLETED POPULATING ATTRACTIONS")
    print("--------------------")

