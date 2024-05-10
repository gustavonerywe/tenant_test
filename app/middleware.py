from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import logging
logger = logging.getLogger(__name__)

class SubdomainMiddleware(MiddlewareMixin):
    def process_request(self, request):
        domain = 'localhost'
    
        host = request.get_host().split(":")[0]
        
        if '.' in host and host.split('.')[0]:
            request_subdomain = host.split('.')[0]
        else:
            request_subdomain = domain 

        print(host, domain)
        print(request.user.username, "request_subdomain", request_subdomain)
        
        if host == domain:
            pass
        else:
            if request.user.is_authenticated and request.user.username != request_subdomain:
                return HttpResponseForbidden("Acesso não permitido para este domínio")