from collective.contactformprotection import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IContacformprotectionControlPanel(Interface):
    disable_form = schema.Bool(
        title=_("Disable contactform globally"),
        required=False,
        default=False,
    )

    use_captcha = schema.Choice(
        title=_(
            "Which captcha should be used",
        ),
        vocabulary="contactformprotection.captchavocabulary",
        required=False,
    )


class ContacformprotectionControlPanel(RegistryEditForm):
    schema = IContacformprotectionControlPanel
    schema_prefix = "collective.contactformprotection"
    label = _("Contacformprotection Control Panel")


ContacformprotectionControlPanelView = layout.wrap_form(
    ContacformprotectionControlPanel, ControlPanelFormWrapper
)
