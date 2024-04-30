# -*- coding: utf-8 -*-

import time

from odoo import models, fields, api
from odoo.tools.translate import _

from odoo.addons.sm_maintenance.models.models_sm_resources import sm_resources
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils
from odoo.addons.sm_partago_invoicing.models.batch_type_enum import BatchType
import logging

_logger = logging.getLogger(__name__)

class smp_batch_reservation_compute(models.Model):
    _name = 'smp.sm_batch_reservation_compute'

    batch_type = fields.Selection([
        ('usage', 'Usage'),
        ('teletac', 'Teletac')],
        string=_("Batch type"),
        default="usage"
    )
    name = fields.Char(string=_("Name"), required=True)
    description = fields.Char(string=_("Description"))
    reports_id = fields.One2many(
        comodel_name='smp.sm_report_reservation_compute',
        inverse_name='batch_reservation_compute_id',
        string=_("Reports")
    )
    state = fields.Selection([
        ('invoice_report', 'Inv report'),
        ('modify_penalty_ratings', 'Modify penalty ratings'),
        ('account_invoices_report', 'Account invoice report'),
        ('apply_discounts', 'Apply discounts'),
        ('generate_invoices', 'Generate invoices'),
        ('validate_invoices', 'Validate invoices'),
        ('closed', 'Closed'),
        ('closed_sent', 'SEPA sent')],
        default='invoice_report'
    )
    invoice_report_id = fields.Many2one(
        'sm.invoice_report',
        string=_("Invoice Report")
    )
    invoice_id = fields.Many2one(
        'account.invoice',
        string=_("Related Invoice"),
        compute="_get_related_invoice"
    )
    total_invoiced_amount_no_discount = fields.Float(
        string=_("Total income base (before discounts)"),
        compute="_get_inv_report_total_no_discount"
    )
    total_discount = fields.Float(
        string=_("Total discount base"),
        compute="_get_total_discount"
    )
    total_invoiced_amount = fields.Float(
        string=_("Total income base (after discounts)"),
        compute="_get_inv_report_total"
    )
    invoice_total = fields.Float(
        string=_("Invoiced total"),
        compute="_get_invoice_total"
    )
    invoice_taxes = fields.Float(
        string=_("Invoiced taxes"),
        compute="_get_invoice_taxes"
    )
    is_grouped_report = fields.Boolean(
        string=_("is_grouped_report"),
        compute="check_is_grouped_report",
        store=False
    )

    _order = "name desc"

    ######################################
    # COMPUTED FIELDS
    ######################################
    @api.depends('invoice_report_id', 'reports_id')
    def check_is_grouped_report(self):
        for record in self:
            record.is_grouped_report = False
            if record.invoice_report_id:
                if record.invoice_report_id.grouped_report:
                    record.is_grouped_report = True

    @api.depends('invoice_report_id')
    def _get_related_invoice(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.invoice_id = record.invoice_report_id.invoice_id

    @api.depends('invoice_report_id', 'reports_id')
    def _get_inv_report_total_no_discount(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.total_invoiced_amount_no_discount = \
                        record.invoice_report_id.total_amount_lines_untaxed
            else:
                total = 0
                for report in record.reports_id:
                    if report.invoice_report_id:
                        total += report.report_total_no_discounts
                record.total_invoiced_amount_no_discount = total

    @api.depends('invoice_report_id', 'reports_id', 'name')
    def _get_total_discount(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.total_discount = \
                        record.invoice_report_id.discount_amount_subtotal
            else:
                total = 0
                for report in record.reports_id:
                    if report.invoice_report_id:
                        total += report.report_discount
                record.total_discount = total

    @api.depends('invoice_report_id', 'reports_id')
    def _get_inv_report_total(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.total_invoiced_amount = \
                        record.invoice_report_id.ir_total_amount_signed
            else:
                total = 0
                for report in record.reports_id:
                    if report.invoice_report_id:
                        total += report.report_total
                record.total_invoiced_amount = total

    @api.depends('invoice_report_id', 'reports_id')
    def _get_invoice_total(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.invoice_total = \
                        record.invoice_report_id.total_amount_in_invoice
            else:
                total = 0
                for report in record.reports_id:
                    if report.invoice_report_id:
                        total += report.invoice_total
                record.invoice_total = total

    @api.depends('invoice_report_id', 'reports_id')
    def _get_invoice_taxes(self):
        for record in self:
            if record.is_grouped_report:
                if record.invoice_report_id:
                    record.invoice_taxes = \
                        record.invoice_report_id.total_taxes_in_invoice
            else:
                total = 0
                for report in record.reports_id:
                    if report.invoice_report_id:
                        total += report.invoice_taxes
                record.invoice_taxes = total

    ######################################
    # ACTIONS
    ######################################
    @api.multi
    def reset_state_action(self):
        if self.env.context:
            if 'active_ids' in self.env.context:
                active_record = self.env[
                    'smp.sm_batch_reservation_compute'
                ].browse(
                    self.env.context['active_ids']
                )
                if active_record.exists():
                    for brc in active_record:
                        brc.state = "invoice_report"

    @api.multi
    def massive_validate_action(self):
        _logger.debug(f"\n massive_validate_action \n batch_reservation ID: {str(self.id)} \n" )
        def execute_from_coincidence(states, check):
            try:
                # Find the index of the first occurrence of the object in the first element of each sublist
                index = next(i for i, sublist in enumerate(states) if sublist[0] == check)
            except StopIteration: # If the object is not found in any sublist, next() raises an error, which we handle here
                return False
            
            for i in range(index, len(states)): # Iterate from the index of the first occurrence to the end of the array
                function, args = states[i][1]
                if callable(function):
                    function(*args)
            
            return True

        if self.env.context:
            if 'active_ids' in self.env.context:
                _logger.debug(f"Active: \n {str(self.env.context['active_ids'])}" )
                active_record = self.env[
                    'smp.sm_batch_reservation_compute'
                ].browse(
                    self.env.context['active_ids']
                )
                if active_record.exists():
                    for brc in active_record:
                        if brc.state not in ['invoice_report', 'modify_penalty_ratings', 'closed_sent']:

                            # The following is the format of the 
                            #
                            #   List( List( String, Tuple( Callable, List(Any) ) )
                            #
                            #   [
                            #       [
                            #            'state',
                            #            (
                            #                obj.callable,
                            #                (*args)
                            #            )
                            #       ],
                            #       ...
                            #   ]

                            states = [
                                #['invoice_report', (brc.prepare_report_invoices, (collected_member, timeframe_desc))],
                                #['modify_penalty_ratings', (brc.modify_penalty_ratings_action, ())],
                                ['account_invoices_report', (brc.account_invoice_reports_action, ())],
                                ['apply_discounts', (brc.apply_discounts_action, ())],
                                ['generate_invoices', (brc.generate_invoices_action, ())],
                                ['validate_invoices', (brc.validate_invoices_action, ())],
                                ['closed', (brc.email_send_invoices_action, ())]
                            ]
                            execute_from_coincidence(states, brc.state)

    ######################################
    # WORKFLOW ACTIONS
    ######################################
    @api.multi
    def create_invoice_report_action(self):
        _logger.debug(f"\n create_invoice_report_action \n batch_reservation ID: {str(self.id)} \n" )
        return {
            "context": self.env.context,
            "view_type": "form",
            "view_mode": "form",
            "res_model": "sm_partago_invoicing.sm_invoice_report_wizard",
            "type": "ir.actions.act_window",
            "name": "Create collected invoice report",
            "target": "new",
        }

    @api.multi
    def modify_penalty_ratings_action(self):
        _logger.debug(f"\n modify_penalty_ratings_action \n batch_reservation ID: {str(self.id)}\n")
        self.ensure_one()
        if self.batch_type == 'usage':
            if self.is_grouped_report:
                self.invoice_report_id.set_to_zero_cancelled_unused_inv_lines()
            else:
                for report in self.reports_id:
                    report.invoice_report_id.set_to_zero_cancelled_unused_inv_lines()
        self._set_status_bar('account_invoices_report')

    @api.multi
    def account_invoice_reports_action(self):
        _logger.debug(f"\n account_invoice_reports_action \n batch_reservation ID: {str(self.id)} \n" )
        self.ensure_one()
        if self.batch_type == 'usage':
            if self.is_grouped_report:
                invoice_report = self.invoice_report_id
                invoice_report.partner_id.sanitize_tariffs()
                invoice_report.account_report_lines()
            else:
                self._sanitize_all_report_members_tariffs()
                for report in self.reports_id:
                    report.invoice_report_id.account_report_lines()
        self._set_status_bar('apply_discounts')

    @api.multi
    def apply_discounts_action(self):
        _logger.debug(f"\n apply_discounts_action \n batch_reservation ID: {str(self.id)} \n" )
        self.ensure_one()
        if self.is_grouped_report:
            self.invoice_report_id.create_discount_lines()
        else:
            for report in self.reports_id:
                report.invoice_report_id.create_discount_lines()
        self._set_status_bar('generate_invoices')

    @api.multi
    def generate_invoices_action(self):
        _logger.debug(f"\n generate_invoices_action \n batch_reservation ID: {str(self.id)} \n" )
        self.ensure_one()
        if self.is_grouped_report:
            self.invoice_report_id.create_related_invoice(self.batch_type)
        else:
            for report in self.reports_id:
                report.invoice_report_id.create_related_invoice(
                    self.batch_type)
        self._set_status_bar('validate_invoices')

    @api.multi
    def validate_invoices_action(self):
        _logger.debug(f"\n validate_invoices_action \n batch_reservation ID: {str(self.id)} \n" )
        self.ensure_one()
        if self.is_grouped_report:
            self.invoice_report_id.validate_related_invoice()
        else:
            for report in self.reports_id:
                report.invoice_report_id.validate_related_invoice()
        self._set_status_bar('closed')

    @api.multi
    def email_send_invoices_action(self):
        _logger.debug(f"\n email_send_invoices_action \n batch_reservation ID: {str(self.id)} \n" )
        #self.env.cr.commit()
        self.ensure_one()
        company = self.env.user.company_id
        email_template = company.invoice_mail_template_id
        email_values = {'send_from_code': True}
        _logger.debug(f"\n\t email_template: \n {str(email_template)} \n" )
        if email_template.id:
            if self.is_grouped_report:
                if self.invoice_report_id:
                    _logger.debug(f"\n\t invoice_id: \n {str(self.invoice_report_id.invoice_id)} \n" )
                    if self.invoice_report_id.invoice_id:
                        invoice = self.invoice_report_id.invoice_id
                        _logger.debug(f"\n\t invoice_email_sent: \n {str(invoice.invoice_email_sent)} \n..." )
                        if not invoice.invoice_email_sent:
                            email_template.with_context(
                                email_values
                            ).send_mail(invoice.id, True)
                            invoice.write({'invoice_email_sent': True})
                            _logger.debug(f"\n\t invoice_email_sent: \n {str(invoice.invoice_email_sent)} \n" )
                        else:
                            _logger.error(f"\n\n\t LA FACTURA YA FUE ENVIADA \n" )
                    else:
                        _logger.error(f"\n\n\t NO EXISTE LA FACTURA \n" )
                else:
                    _logger.error(f"\n\n\t NO EXISTE EL REPORTE DE LA FACTURA \n" )
            else:
                for report in self.reports_id:
                    if report.invoice_report_id:
                        if report.invoice_report_id.invoice_id:
                            invoice = report.invoice_report_id.invoice_id
                            if invoice:
                                _logger.debug(f"\n\t invoice.invoice_email_sent: \n {str(invoice.invoice_email_sent)} \n..." )
                                if not invoice.invoice_email_sent:
                                    email_template.with_context(
                                        email_values
                                    ).send_mail(invoice.id, True)
                                    invoice.write({'invoice_email_sent': True})
                                    _logger.debug(f"\n\t invoice_email_sent: \n {str(invoice.invoice_email_sent)} \n" )

    def set_closed_sent_action(self):
        self.set_status_bar("closed_sent")
        return True

    ######################################
    # MODEL METHODS
    ######################################
    def _sanitize_all_report_members_tariffs(self):
        if self.reports_id.exists():
            for report in self.reports_id:
                if report.report_type != BatchType.TELETAC.value:
                    report.member_id.sanitize_tariffs()
        return True

    def prepare_report_invoices(self, collected_member, timeframe_desc=''):
        batch_to_compute = [self.batch_type]
        if collected_member.id:
            collected_member.sanitize_tariffs()
            report_invoice_report = self.env['sm.invoice_report'].create({
                'name': self.name + '-' + collected_member.name,
                'partner_id': collected_member.id,
                'company_id': 1,
                'date': str(time.strftime("%Y-%m-%d")),
                'timeframe_desc': timeframe_desc,
                'grouped_report': True
            })
            self.write({
                'invoice_report_id': report_invoice_report.id
            })
            report_invoice_report.compute_report_lines(batch_to_compute)
            report_invoice_report.assign_previous_pocketbook()
        else:
            if self.reports_id.exists():
                for report in self.reports_id:
                    if report.member_id.id:
                        report.member_id.sanitize_tariffs()
                        report_invoice_report = self.env[
                            'sm.invoice_report'
                        ].create({
                            'name': self.name + '-' + report.member_id.name,
                            'partner_id': report.member_id.id,
                            'company_id': 1,
                            'date': str(time.strftime("%Y-%m-%d")),
                            'timeframe_desc': timeframe_desc,
                            'grouped_report': False
                        })
                        report.write({
                            'invoice_report_id': report_invoice_report.id
                        })
                        report_invoice_report.compute_report_lines(
                            batch_to_compute)
                        report_invoice_report.assign_previous_pocketbook()
        self._set_status_bar('modify_penalty_ratings')
        return True

    def _set_status_bar(self, state):
        self.write({
            'state': state,
        })
