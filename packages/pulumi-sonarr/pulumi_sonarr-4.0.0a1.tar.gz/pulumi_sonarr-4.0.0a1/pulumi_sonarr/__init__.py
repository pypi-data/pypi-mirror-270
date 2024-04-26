# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from ._inputs import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_sonarr.config as __config
    config = __config
    import pulumi_sonarr.downloadclients as __downloadclients
    downloadclients = __downloadclients
    import pulumi_sonarr.importlists as __importlists
    importlists = __importlists
    import pulumi_sonarr.indexers as __indexers
    indexers = __indexers
    import pulumi_sonarr.languages as __languages
    languages = __languages
    import pulumi_sonarr.mediamanagement as __mediamanagement
    mediamanagement = __mediamanagement
    import pulumi_sonarr.metadata as __metadata
    metadata = __metadata
    import pulumi_sonarr.notifications as __notifications
    notifications = __notifications
    import pulumi_sonarr.profiles as __profiles
    profiles = __profiles
    import pulumi_sonarr.series as __series
    series = __series
    import pulumi_sonarr.system as __system
    system = __system
    import pulumi_sonarr.tags as __tags
    tags = __tags
else:
    config = _utilities.lazy_import('pulumi_sonarr.config')
    downloadclients = _utilities.lazy_import('pulumi_sonarr.downloadclients')
    importlists = _utilities.lazy_import('pulumi_sonarr.importlists')
    indexers = _utilities.lazy_import('pulumi_sonarr.indexers')
    languages = _utilities.lazy_import('pulumi_sonarr.languages')
    mediamanagement = _utilities.lazy_import('pulumi_sonarr.mediamanagement')
    metadata = _utilities.lazy_import('pulumi_sonarr.metadata')
    notifications = _utilities.lazy_import('pulumi_sonarr.notifications')
    profiles = _utilities.lazy_import('pulumi_sonarr.profiles')
    series = _utilities.lazy_import('pulumi_sonarr.series')
    system = _utilities.lazy_import('pulumi_sonarr.system')
    tags = _utilities.lazy_import('pulumi_sonarr.tags')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/aria2",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/aria2:Aria2": "Aria2"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/config",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/config:Config": "Config"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/deluge",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/deluge:Deluge": "Deluge"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/downloadClient",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/downloadClient:DownloadClient": "DownloadClient"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/flood",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/flood:Flood": "Flood"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/hadouken",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/hadouken:Hadouken": "Hadouken"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/nzbget",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/nzbget:Nzbget": "Nzbget"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/nzbvortex",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/nzbvortex:Nzbvortex": "Nzbvortex"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/pneumatic",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/pneumatic:Pneumatic": "Pneumatic"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/qbittorrent",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/qbittorrent:Qbittorrent": "Qbittorrent"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/remotePathMapping",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/remotePathMapping:RemotePathMapping": "RemotePathMapping"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/rtorrent",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/rtorrent:Rtorrent": "Rtorrent"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/sabnzbd",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/sabnzbd:Sabnzbd": "Sabnzbd"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/torrentBlackhole",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/torrentBlackhole:TorrentBlackhole": "TorrentBlackhole"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/torrentDownloadStation",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/torrentDownloadStation:TorrentDownloadStation": "TorrentDownloadStation"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/transmission",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/transmission:Transmission": "Transmission"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/usenetBlackhole",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/usenetBlackhole:UsenetBlackhole": "UsenetBlackhole"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/usenetDownloadStation",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/usenetDownloadStation:UsenetDownloadStation": "UsenetDownloadStation"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/utorrent",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/utorrent:Utorrent": "Utorrent"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "DownloadClients/vuze",
  "fqn": "pulumi_sonarr.downloadclients",
  "classes": {
   "sonarr:DownloadClients/vuze:Vuze": "Vuze"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/custom",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/custom:Custom": "Custom"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/exclusion",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/exclusion:Exclusion": "Exclusion"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/imdb",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/imdb:Imdb": "Imdb"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/importList",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/importList:ImportList": "ImportList"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/plex",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/plex:Plex": "Plex"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/plexRss",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/plexRss:PlexRss": "PlexRss"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/simklUser",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/simklUser:SimklUser": "SimklUser"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/sonarr",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/sonarr:Sonarr": "Sonarr"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/traktList",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/traktList:TraktList": "TraktList"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/traktPopular",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/traktPopular:TraktPopular": "TraktPopular"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "ImportLists/traktUser",
  "fqn": "pulumi_sonarr.importlists",
  "classes": {
   "sonarr:ImportLists/traktUser:TraktUser": "TraktUser"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/broadcasthenet",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/broadcasthenet:Broadcasthenet": "Broadcasthenet"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/config",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/config:Config": "Config"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/fanzub",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/fanzub:Fanzub": "Fanzub"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/filelist",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/filelist:Filelist": "Filelist"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/hdbits",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/hdbits:Hdbits": "Hdbits"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/indexer",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/indexer:Indexer": "Indexer"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/iptorrents",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/iptorrents:Iptorrents": "Iptorrents"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/newznab",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/newznab:Newznab": "Newznab"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/nyaa",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/nyaa:Nyaa": "Nyaa"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/torrentRss",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/torrentRss:TorrentRss": "TorrentRss"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/torrentleech",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/torrentleech:Torrentleech": "Torrentleech"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Indexers/torznab",
  "fqn": "pulumi_sonarr.indexers",
  "classes": {
   "sonarr:Indexers/torznab:Torznab": "Torznab"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "MediaManagement/mediaManagement",
  "fqn": "pulumi_sonarr.mediamanagement",
  "classes": {
   "sonarr:MediaManagement/mediaManagement:MediaManagement": "MediaManagement"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "MediaManagement/naming",
  "fqn": "pulumi_sonarr.mediamanagement",
  "classes": {
   "sonarr:MediaManagement/naming:Naming": "Naming"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "MediaManagement/rootFolder",
  "fqn": "pulumi_sonarr.mediamanagement",
  "classes": {
   "sonarr:MediaManagement/rootFolder:RootFolder": "RootFolder"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Metadata/kodi",
  "fqn": "pulumi_sonarr.metadata",
  "classes": {
   "sonarr:Metadata/kodi:Kodi": "Kodi"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Metadata/metadata",
  "fqn": "pulumi_sonarr.metadata",
  "classes": {
   "sonarr:Metadata/metadata:Metadata": "Metadata"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Metadata/roksbox",
  "fqn": "pulumi_sonarr.metadata",
  "classes": {
   "sonarr:Metadata/roksbox:Roksbox": "Roksbox"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Metadata/wdtv",
  "fqn": "pulumi_sonarr.metadata",
  "classes": {
   "sonarr:Metadata/wdtv:Wdtv": "Wdtv"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/apprise",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/apprise:Apprise": "Apprise"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/customScript",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/customScript:CustomScript": "CustomScript"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/discord",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/discord:Discord": "Discord"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/email",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/email:Email": "Email"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/emby",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/emby:Emby": "Emby"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/gotify",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/gotify:Gotify": "Gotify"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/join",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/join:Join": "Join"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/kodi",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/kodi:Kodi": "Kodi"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/mailgun",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/mailgun:Mailgun": "Mailgun"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/notification",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/notification:Notification": "Notification"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/ntfy",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/ntfy:Ntfy": "Ntfy"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/plex",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/plex:Plex": "Plex"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/prowl",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/prowl:Prowl": "Prowl"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/pushbullet",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/pushbullet:Pushbullet": "Pushbullet"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/pushover",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/pushover:Pushover": "Pushover"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/sendgrid",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/sendgrid:Sendgrid": "Sendgrid"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/signal",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/signal:Signal": "Signal"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/simplepush",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/simplepush:Simplepush": "Simplepush"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/slack",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/slack:Slack": "Slack"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/synologyIndexer",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/synologyIndexer:SynologyIndexer": "SynologyIndexer"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/telegram",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/telegram:Telegram": "Telegram"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/trakt",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/trakt:Trakt": "Trakt"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/twitter",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/twitter:Twitter": "Twitter"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Notifications/webhook",
  "fqn": "pulumi_sonarr.notifications",
  "classes": {
   "sonarr:Notifications/webhook:Webhook": "Webhook"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Profiles/customFormat",
  "fqn": "pulumi_sonarr.profiles",
  "classes": {
   "sonarr:Profiles/customFormat:CustomFormat": "CustomFormat"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Profiles/definition",
  "fqn": "pulumi_sonarr.profiles",
  "classes": {
   "sonarr:Profiles/definition:Definition": "Definition"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Profiles/delayProfile",
  "fqn": "pulumi_sonarr.profiles",
  "classes": {
   "sonarr:Profiles/delayProfile:DelayProfile": "DelayProfile"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Profiles/profile",
  "fqn": "pulumi_sonarr.profiles",
  "classes": {
   "sonarr:Profiles/profile:Profile": "Profile"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Profiles/releaseProfile",
  "fqn": "pulumi_sonarr.profiles",
  "classes": {
   "sonarr:Profiles/releaseProfile:ReleaseProfile": "ReleaseProfile"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Series/series",
  "fqn": "pulumi_sonarr.series",
  "classes": {
   "sonarr:Series/series:Series": "Series"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "System/host",
  "fqn": "pulumi_sonarr.system",
  "classes": {
   "sonarr:System/host:Host": "Host"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Tags/autoTag",
  "fqn": "pulumi_sonarr.tags",
  "classes": {
   "sonarr:Tags/autoTag:AutoTag": "AutoTag"
  }
 },
 {
  "pkg": "sonarr",
  "mod": "Tags/tag",
  "fqn": "pulumi_sonarr.tags",
  "classes": {
   "sonarr:Tags/tag:Tag": "Tag"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "sonarr",
  "token": "pulumi:providers:sonarr",
  "fqn": "pulumi_sonarr",
  "class": "Provider"
 }
]
"""
)
