from django.apps import AppConfig

from core.custom_filters import CustomFilterRegistryPoint
from payroll.payments_registry import PaymentsMethodRegistryPoint

MODULE_NAME = 'payroll'

DEFAULT_CONFIG = {
    "gql_payment_point_search_perms": ["201001"],
    "gql_payment_point_create_perms": ["201002"],
    "gql_payment_point_update_perms": ["201003"],
    "gql_payment_point_delete_perms": ["201004"],
    "gql_payroll_search_perms": ["202001"],
    "gql_payroll_create_perms": ["202002"],
    "gql_payroll_delete_perms": ["202004"],
    "gql_csv_reconciliation_search_perms": ["206001"],
    "gql_csv_reconciliation_create_perms": ["206002"],
    "payroll_accept_event": "payroll.accept_payroll",
    "payroll_reconciliation_event": "payroll.payroll_reconciliation",
    "payroll_reject_event": "payroll.payroll_reject",
    "csv_reconciliation_field_mapping": {
        'payrollbenefitconsumption__payroll__name': 'Payroll Name',
        'payrollbenefitconsumption__payroll__status': 'Payroll Status',
        'individual__first_name': 'First Name',
        'individual__last_name': 'Last Name',
        'individual__dob': 'Date of Birth',
        'code': 'Code',
        'status': 'Status',
        'amount': 'Amount',
        'type': 'Type',
        'receipt': 'Receipt',
    },
    "csv_reconciliation_status_column": "Status",
    "csv_reconciliation_paid_extra_field": "Paid",
    "csv_reconciliation_receipt_column": "receipt",
    "csv_reconciliation_errors_column": "errors",
    "csv_reconciliation_code_column": "code",
    "csv_reconciliation_paid_yes": "Yes",
    "csv_reconciliation_paid_no": "No",
    "payroll_delete_event": "payroll.payroll_delete",
}


class PayrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = MODULE_NAME

    gql_payment_point_search_perms = None
    gql_payment_point_create_perms = None
    gql_payment_point_update_perms = None
    gql_payment_point_delete_perms = None
    gql_payroll_search_perms = None
    gql_payroll_create_perms = None
    gql_payroll_delete_perms = None
    gql_csv_reconciliation_search_perms = None
    gql_csv_reconciliation_create_perms = None
    payroll_accept_event = None
    payroll_reconciliation_event = None
    payroll_reject_event = None
    csv_reconciliation_field_mapping = None
    csv_reconciliation_status_column = None
    csv_reconciliation_paid_extra_field = None
    csv_reconciliation_receipt_column = None
    csv_reconciliation_errors_column = None
    csv_reconciliation_code_column = None
    csv_reconciliation_paid_yes = None
    csv_reconciliation_paid_no = None
    payroll_delete_event = None

    def ready(self):
        from core.models import ModuleConfiguration

        cfg = ModuleConfiguration.get_or_default(self.name, DEFAULT_CONFIG)
        self.__load_config(cfg)
        self.__register_filters_and_payment_methods()

    @classmethod
    def __load_config(cls, cfg):
        """
        Load all config fields that match current AppConfig class fields, all custom fields have to be loaded separately
        """
        for field in cfg:
            if hasattr(PayrollConfig, field):
                setattr(PayrollConfig, field, cfg[field])

    def __register_filters_and_payment_methods(cls):
        from social_protection.custom_filters import BenefitPlanCustomFilterWizard
        CustomFilterRegistryPoint.register_custom_filters(
            module_name=cls.name,
            custom_filter_class_list=[BenefitPlanCustomFilterWizard]
        )

        from payroll.strategies import (
            StrategyOfflinePayment
        )
        PaymentsMethodRegistryPoint.register_payment_method(
            payment_method_class_list=[
                StrategyOfflinePayment()
            ]
        )

    @staticmethod
    def get_payroll_payment_file_path(payroll_id, file_name=None):
        if file_name:
            return f"csv_reconciliation/payroll_{payroll_id}/{file_name}"
        return f"csv_reconciliation/payroll_{payroll_id}"
