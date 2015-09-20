from django.conf.urls import include, url,patterns


urlpatterns = patterns('home.views',
    # Examples:
    url(r'^$', 'home'),   
    url(r'^images/$','captureImage'),
   
   #  url(r'^$', include('home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
)