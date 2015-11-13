"""Tests for plugin.py."""
import ckanext.ezid.plugin as plugin
import pylons.config as config

class StubPackageContext():
    dict = {}
    def as_dict(self):
        return self.dict
    def set_dict(self, dict):
        self.dict = dict

def test_plugin():
    namespace = config.get('ckanext.ezid.namespace')
    username = config.get('ckanext.ezid.username')
    password = config.get('ckanext.ezid.password')
    assert namespace is not None and username is not None and password is not None
    context = {'package': StubPackageContext()}
    context['package'].set_dict({
        'ckan_url': 'https://github.com/UoA-eResearch/ckanext-ezid',
        'owner_org': 'test_org',
        'author': 'test_author',
        'title': 'test_title'
    })
    instance = plugin.EZIDPlugin()
    external_id = instance.get_external_id(context)
    assert 'http://dx.doi.org/' in external_id
    assert instance.get_pretty_name() == 'EZID'

def test_metadata_incomplete():
    namespace = config.get('ckanext.ezid.namespace')
    username = config.get('ckanext.ezid.username')
    password = config.get('ckanext.ezid.password')
    assert namespace is not None and username is not None and password is not None
    context = {'package': StubPackageContext()}
    context['package'].set_dict({
        'ckan_url': 'https://github.com/UoA-eResearch/ckanext-ezid',
        'owner_org': 'test_org',
        'author': '',
        'title': ''
    })
    instance = plugin.EZIDPlugin()
    external_id = instance.get_external_id(context)
    assert external_id == \
        'error: bad request - DOI metadata requirements not satisfied: no creator'