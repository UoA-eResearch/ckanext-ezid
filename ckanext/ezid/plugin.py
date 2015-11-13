import logging
import requests

import pylons.config as config

import ckan
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.external_id.interfaces import IExternalIDProvider

from ckan.logic.action.get import organization_show

import re
import datetime

log = logging.getLogger(__name__)

def escape (s):
  return re.sub("[%:\r\n]", lambda c: "%%%02X" % ord(c.group(0)), s)

class EZIDPlugin(plugins.SingletonPlugin):
    plugins.implements(IExternalIDProvider)

    def get_external_id(self, context):
        metadata = context['package'].as_dict()
        ckan_url = metadata['ckan_url']
        log.info('minting %s' % ckan_url)

        try:
            org = organization_show(context, {'id':metadata['owner_org']})['title']
        except:
            org = metadata['owner_org']

        metadata = {'_target': ckan_url,
                    'datacite.creator': metadata['author'],
                    'datacite.title': metadata['title'],
                    'datacite.publisher': org,
                    'datacite.publicationyear': str(datetime.datetime.now().year),
                    'datacite.resourcetype': 'Dataset'}
        anvl = "\n".join("%s: %s" % (escape(name), escape(value)) for name,
            value in metadata.items()).encode("UTF-8")
        namespace = config.get('ckanext.ezid.namespace')
        username = config.get('ckanext.ezid.username')
        password = config.get('ckanext.ezid.password')
        api_url = 'https://ezid.cdlib.org/shoulder/%s' % namespace
        r = requests.post(api_url,
                          data = anvl,
                          headers = {'Content-Type':'text/plain; charset=UTF-8'},
                          auth = (username, password))
        log.info('EZID reply: %s' % r.text)
        if 'success' in r.text:
            doi = re.search('success: doi:(.+?) \|.+', r.text).group(1)
            return "http://dx.doi.org/%s" % doi
        return r.text

    def get_pretty_name(self):
        return "EZID"