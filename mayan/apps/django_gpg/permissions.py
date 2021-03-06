from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from permissions import PermissionNamespace

namespace = PermissionNamespace('django_gpg', _('Key management'))

permission_key_view = namespace.add_permission(
    name='key_view', label=_('View keys')
)
permission_key_delete = namespace.add_permission(
    name='key_delete', label=_('Delete keys')
)
permission_keyserver_query = namespace.add_permission(
    name='keyserver_query', label=_('Query keyservers')
)
permission_key_receive = namespace.add_permission(
    name='key_receive', label=_('Import keys from keyservers')
)
