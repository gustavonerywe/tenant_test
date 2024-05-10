# from django.http import HttpResponseRedirect
# from django.contrib.auth import logout
# from django.urls import reverse_lazy

# class TenantAccessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("Middleware initialized")  # Esta linha deve ser impressa durante a inicialização do servidor

#     def __call__(self, request):
#         print("Middleware called")  # Verifique se esta linha é impressa em cada requisição
#         if request.user.is_authenticated:
#             print("User is authenticated")
#             host = request.get_host().split('.')
#             current_subdomain = host[0] if len(host) > 2 else None

#             expected_subdomain = request.user.username
#             print(f"Current subdomain: {current_subdomain}, Expected subdomain: {expected_subdomain}")

#             if current_subdomain != expected_subdomain:
#                 print('Subdomain does not match, logging out user')
#                 logout(request)
#         else:
#             print("User is not authenticated")
#         response = self.get_response(request)
#         return response