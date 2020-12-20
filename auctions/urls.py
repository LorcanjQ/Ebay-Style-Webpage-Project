from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create, name="create"),
    path("listing:<int:listing_id>", views.listing, name="listing"),
    path("listing:<int:listing_id>/addtofavourites", views.add_fave, name="add_fave"),
    path("watchlist:<int:user_id>", views.watchlist, name="wl"),


]
