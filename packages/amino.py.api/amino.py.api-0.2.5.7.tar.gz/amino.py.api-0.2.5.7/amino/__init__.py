from .client import Client
from .community_client import CommunityClient
from .helpers import generators, exceptions
from . import asynclib
from . import models
from .helpers.types import all_ws_types




def create_community_client(client: Client, comId: int = None, community_link: str = None, aminoId: str = None):
	return CommunityClient(
		comId=comId,
		community_link=community_link,
		aminoId=aminoId,
		profile=client.profile,
		language=client.language,
		user_agent=client.user_agent,
		auto_user_agent=client.auto_user_agent,
		deviceId=client.deviceId,
		auto_device=client.auto_device,
		proxies=client.proxies,
		certificate_path=client.verify,
		http_connect=client.http_connect,
		requests_debug=client.requests_debug
	)



__title__ = 'amino.api'
__author__ = 'Xsarz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-2024 Xsarz'
__version__ = '0.2.5.7'
