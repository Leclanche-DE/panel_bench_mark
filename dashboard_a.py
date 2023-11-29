from abstract_dashboard import AbstractDashboard
import panel as pn

class DashboardA(AbstractDashboard):
    title = 'A'

    def view(self):
        return pn.template.VanillaTemplate(title=self.title, main=[super().view()])

if __name__.startswith('bokeh'):
    DashboardA().view().servable()