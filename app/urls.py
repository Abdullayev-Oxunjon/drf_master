from django.urls import path

from app.views import LoginAPIView, LeaveRequestView, ListRequestView, GetRequestView, UpdateRequestView, \
    DeleteRequestView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),

    # Request URLs

    path("leave_request/", LeaveRequestView.as_view(), name="leave_request"),
    path("list_requests/", ListRequestView.as_view(), name="list_requests"),
    path("get_request/<int:pk>/", GetRequestView.as_view(), name="get_request"),
    path("update_request/<int:pk>/", UpdateRequestView.as_view(), name="update_request"),
    path("delete_request/<int:pk>/", DeleteRequestView.as_view(), name="delete_request"),
]
