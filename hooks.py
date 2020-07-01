from odoo.tools import convert_file
from .hltv_api.main import top_players_csv

def load_players(cr, registry):
    top_players_csv()
    convert_file(cr, 'csgo_player_statistic', 'hltv_api/csgo_player_statistic.player.csv', None, mode='init', noupdate=True, kind='init', report=None)

