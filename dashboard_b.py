from abstract_dashboard import AbstractDashboard
import panel as pn

class DashboardB(AbstractDashboard):
    title = 'B'

    def view(self):
        return pn.template.VanillaTemplate(title=self.title, main=[super().view()])

if __name__.startswith('bokeh'):
    DashboardB().view().servable()