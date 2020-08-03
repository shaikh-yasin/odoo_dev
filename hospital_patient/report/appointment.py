from odoo import api, models, _
from odoo import api, models


class AppointmentReport(models.AbstractModel):
    _name = 'report.hospital_patient.appointment_report'
    _description = 'Appointment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data['form']['patient_id']:
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', data['form']['patient_id'][0])])
        else:
            appointments = self.env['hospital.appointment'].search([])
        # appointment_list = []
        # for app in appointments:
        #     vals = {
        #         'name': app.name,
        #         'notes': app.notes,
        #         'appointment_date': app.appointment_date
        #     }
        #     appointment_list.append(vals)
        return {
            'doc_model': 'hospital.patient',
            'appointments': appointments,
        }
        
#
#class ParticularReport(models.AbstractModel):
#    _name = 'report.module.report_name'
#
#    @api.model
#    def _get_report_values(self, docids, data=None):
#        report_obj = self.env['ir.actions.report']
#        report = report_obj._get_report_from_name('module.report_name')
#        docargs = {
#            'doc_ids': docids,
#            'doc_model': report.model,
#            'docs': self,
#        }
#        return docargs        