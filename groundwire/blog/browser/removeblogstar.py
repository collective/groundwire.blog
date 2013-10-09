from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class RemoveBlogStar(BrowserView):
    """
    Remove collective.blog.star and *all* its dependencies:
      - collective.blog.view
      - collective.blog.portlets
      - collective.twitterportlet
      - collective.flowplayer
      - qi.portlet.TagClouds
      - Products.fatsyndication
      - plone.app.jquerytools (installed by collective.flowplayer)
    """
    
    def __call__(self):
        
        # Remove collective.blog.star from the quickinstaller.
        qi = getToolByName(self.context, 'portal_quickinstaller')
        if qi.isProductInstalled('collective.blog.star'):
            qi.uninstallProducts(products=['collective.blog.star',])
            
        # Run the uninstall profile.
        setup_tool = getToolByName(self.context, 'portal_setup')
        profile = 'profile-groundwire.blog:removeblogstar'
        setup_tool.runAllImportStepsFromProfile(profile)
        
        # Clean up some properties that can't be removed using GenericSetup.
        pprops = getToolByName(self.context, 'portal_properties')
        if 'flowplayer_properties' in pprops.objectIds():
            del pprops['flowplayer_properties']
            
        site_props = pprops['site_properties']
        if site_props.hasProperty('blog_view_items'):
            site_props.manage_delProperties(ids=['blog_view_items'])
        if site_props.hasProperty('blog_types'):
            site_props.manage_delProperties(ids=['blog_types'])
        
        # Get rid of Flowplayer's TinyMCE styles.
        tinymce = getToolByName(self.context, 'portal_tinymce')
        old_styles = tinymce.styles.split('\n')
        new_styles = [s for s in old_styles if not 'FlowPlayer' in s]
        tinymce.styles = '\n'.join(new_styles)
        
        return 'Success!'
            
        