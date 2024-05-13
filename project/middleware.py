from django_tenants.middleware.main import TenantMainMiddleware

class TenantMainMiddleware(TenantMainMiddleware):
    def get_tenant(self, domain_model, hostname):
        tenant = super().get_tenant(domain_model, hostname)
        if not tenant.schema_name:
            return self.TENANT_NOT_FOUND_EXCEPTION("Tenant not found")
        return tenant