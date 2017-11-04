from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^notifications/$', views.notifs, name="notifications"),
	url(r'^deactivate/$', views.deactivate, name="deactivate"),
	url(r'^make_admin/$', views.madmin, name="make admin"),
	url(r'^make_mentor/$', views.mmentor, name="make mentor"),
	url(r'^assign_mentor/$', views.amentor, name="assign mentor"),
	url(r'^create_project/$', views.cproj, name="create project"),
	url(r'^join_proj/$', views.jproj, name="join project"),
	url(r'^del_proj/$', views.dproj, name="delete project"),
	url(r'^create_event/$', views.cevent, name="create event"),
	url(r'^call_meeting/$', views.call_meeting, name="allteammeat"),
	url(r'^attend/$', views.attend_meet, name="attendmeet"),
	url(r'^send_designs/$', views.sdesigns, name="send_des"),
	url(r'^changeavatar/$', views.cava, name="change avatar"),
	url(r'^merch_des/(?P<ID>[0-9]+)$', views.mavatar, name="merch_des"),
	url(r'^avatar/$', views.avatar, name="avatar"),
	url(r'^join_ev/$', views.jev, name="join event"),
	url(r'^del_ev/$', views.devent, name="delete event"),
	url(r'^profile/$', views.dashboard, name="dashboard"),
	url(r'^order/$', views.order, name="order"),
	url(r'^login/$', views.login, name="login"),
	url(r'^cpg/$', views.cpg, name='cpg'),
	url(r'^ml/$', views.ml, name='ml'),
	url(r'^dev/$', views.dev, name='dev'),
	url(r'^fin/$', views.fin, name='fin'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^infosec/$', views.infosec, name='infosec'),
	url(r'^merchandise/$', views.merch, name='merchandise'),
	url(r'^projects/$', views.proj, name='projects'),
	url(r'^events/$', views.events, name='events'),
	# url(r'^sponsors/$', views.sponsors, name="sponsors"),
	url(r'^logout/$', views.logout, name="logout"),
	url(r'^register/$', views.register, name="register"),
	url(r'^$', views.home, name='home'),
]