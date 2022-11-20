import sys
from lib.action_builder import action
from models.item import Item
from lib.router import Controller
from resolvers.tvb import get_tokenized_link

import xbmcgui
import xbmcplugin

_handle = int(sys.argv[1])
_screen = xbmcplugin


@Controller
class MainController:
    '''
        Each handler function should return 2 values,
        1. list of items DTO
        2. title, None to use default
    '''

    @action(results_in="screen")
    def landing_screen(params=None):
        items = [
            Item(name="TVB News", description="TVB News", image="http://img.tvb.com/ti_img/inews/20191210/live_51ececd4a4b9a44d3286036c_small_1575965391.jpg",
                 params={'path': 'tvb_handler', 'channel': 'news'}),
            Item(name="TVB Finance", description="TVB Finance", image="http://img.tvb.com/ti_img/inews/20180213/live_5a699f3668c55cc22098da62_small_1518512099.jpg",
                 params={'path': 'tvb_handler', 'channel': 'finance'}),
            Item(name="TVB iNews", description="TVB iNews", image="http://img.tvb.com/ti_img/inews/20191210/live_51ececd4a4b9a44d3286036c_small_1575965391.jpg",
                 params={'path': 'tvb_handler', 'channel': 'inews'})
        ]

        return items, None

    def tvb_handler(params):
        ''' handles resolving and playing media '''

        channel = params['channel']

        link = get_tokenized_link(channel)

        if not link:
            return

        listItem = xbmcgui.ListItem()
        listItem.setPath(link)

        _screen.setResolvedUrl(_handle, True, listItem)
