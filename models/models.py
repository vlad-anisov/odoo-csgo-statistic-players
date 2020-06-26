from odoo import models, fields

class Player(models.Model):
    _name = 'csgo_player_statistic.player'
    _description = 'Player'

    country = fields.Char(String='Country', required=True)
    name = fields.Char(string="Name", required=True)
    nickname = fields.Char(string="Nickname", required=True)
    rating = fields.Float(string="Rating", required=True)
    maps_played = fields.Integer(string="Maps played", required=True)
