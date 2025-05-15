from django.utils.deprecation import MiddlewareMixin

class GlobalVarMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.global_var = "category"
