from odoo import models, fields

class Reclamation(models.Model):
    _name = 'reclamation.ticket'
    _description = 'Réclamation Interne'

    name = fields.Char(string='Sujet', required=True)
    description = fields.Text(string='Description détaillée')
    date_creation = fields.Date(string='Date', default=fields.Date.today)
    priorite = fields.Selection([
        ('0', 'Basse'),
        ('1', 'Moyenne'),
        ('2', 'Haute')
    ], string='Priorité', default='1')
    etat = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('cours', 'En cours'),
        ('resolu', 'Résolu')
    ], string='Statut', default='nouveau')