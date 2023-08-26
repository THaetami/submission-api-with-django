from rest_framework.views import APIView
from rest_framework.response import Response

class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'Admin Page': " /admin | ubah data kolom is_superuser dan is_staff pada tabel user menjadi 1, agar bisa mengakses admin page ",
            'User Register': '/user/register',
            'User Login': '/user/login',
            'View User Logged in': '/user',
            'User Logout': '/user/logout',
            'Get Sales All': '/sales',
            'Add Sales': '/sales/create',
            'Get Sales By sal_id': '/sales/<sal_id:str>',
            'Update Sales': '/sales/<sal_id:str>/update',
            'Delete Sales': '/sales/<sal_id:str>/delete'
        }
        return Response(api_urls)