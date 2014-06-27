from AccessControl.Permissions import copy_or_move
from AccessControl import getSecurityManager
from Products.Archetypes.BaseFolder import BaseFolderMixin
from AccessControl.PermissionRole import PermissionRole


def cb_userHasCopyOrMovePermission(self):
    has_copy_or_move = getSecurityManager().checkPermission(copy_or_move, self)
    has_del = getSecurityManager().checkPermission(
        "Delete portal content", self)
    if has_copy_or_move and has_del:
        return 1

# Patch manage_cutObjects security.
# By default AT's BaseFolderMixin sets the permission of manage_cutObjects
# to ModifyPortalContent
# We have to change this afterwards.
# Set manage_cutObjects__roles__, which stores the definition generated by
# AccessControl.class_init or App.class_init.
setattr(BaseFolderMixin, 'manage_cutObjects__roles__',
        PermissionRole("Delete objects", None))
