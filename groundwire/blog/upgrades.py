from plone.browserlayer.utils import registered_layers, unregister_layer
from groundwire.blog.interfaces import IGroundwireBlogLayer

def null_upgrade_step(setup_tool):
    """
    This is a null upgrade. Use it when nothing happens.
    """
    pass
    
def upgrade_10_to_20(setup_tool):
    """
    Upgrade 1.0 to 2.0.
    """

    # Remove the browser layer.
    if IGroundwireBlogLayer in registered_layers():
        unregister_layer('groundwire.blog')
