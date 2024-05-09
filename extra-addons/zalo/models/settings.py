from odoo import models, fields,api
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_id = fields.Char(string='App ID', required=True)
    secret_key = fields.Char(string='Secret Key', required=True)
#     redirect_uri = fields.Char(string='Redirect URI', required=True)


# @api.model
# def set_values(self):
#     ICP=self.env['ir.config_parameter'].sudo()
#     ICP.set_param('zalo.app_id',self.app_id)
#     super(ResConfigSettings,self).set_values()

# @api.model
# def get_values(self):
#     ICP = self.env["ir.config_parameter"].sudo()
#     res = super(ResConfigSettings, self).get_values()
#     res['app_id']=ICP.get_param('zalo.app_id', default='')


#@api.model
#def set_values(self):
   # ICP=self.env['ir.config_parameter'].sudo()
    #ICP.set_param('zalo.app_id',self.app_id)
    #super(ResConfigSettings,self).set_values()

#@api.model
#def get_values(self):
   # ICP = self.env["ir.config_parameter"].sudo()
    #res = super(ResConfigSettings, self).get_values()
    #res['app_id']=ICP.get_param('zalo.app_id', default='')
