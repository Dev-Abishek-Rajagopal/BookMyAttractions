from django.urls import path
from django.conf.urls import url
from .views import (
    AttractionVeiwSet, InventoryVeiwSet, BookingVeiwSet, update_Booking
)


attractions = AttractionVeiwSet.as_view({
    'get' : 'list_Attraction',
    'post' : 'create_Attraction',
})

attractions_id = AttractionVeiwSet.as_view({
    'get' : 'get_Attraction',
    'put': 'update_Attraction',
    'delete': 'delete_Attraction'
})

inventory = InventoryVeiwSet.as_view({
    'get' : 'list_Inventory',
    'post' : 'create_Inventory',
})

inventory_id = InventoryVeiwSet.as_view({
    'get' : 'get_Inventory',
    'put': 'update_Inventory',
    'delete': 'delete_Inventory'
})

booking = BookingVeiwSet.as_view({
    'get' : 'list_Booking',
    'post' : 'create_Booking',
})

booking_id = BookingVeiwSet.as_view({
    'get' : 'get_Booking',
    
    'delete': 'delete_Booking'
})




app_name = "attractions"
urlpatterns  = [
        
    url(r'^attr/(?P<pk>\d+)/$', attractions_id),
    url(r'^attr/$', attractions),

    url(r'^invent/(?P<pk>\d+)/$', inventory_id),
    url(r'^invent/$', inventory),

    url(r'^book/(?P<pk>\d+)/$', booking_id),
    url(r'^book/$', booking),
    url(r'^editbook/$', update_Booking),
    # path('get/', create_Dp, name = 'view_products')
]
