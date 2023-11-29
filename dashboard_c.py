from abstract_dashboard import AbstractDashboard
import panel as pn

class DashboardC(AbstractDashboard):
    title = 'C'

    def view(self):
        return pn.template.VanillaTemplate(title=self.title, main=[super().view()])

if __name__.startswith('bokeh'):
    DashboardC().view().servable()