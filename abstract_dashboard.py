import param
import panel as pn
import time

class AbstractDashboard(param.Parameterized):
    duration = param.Selector(objects=[1, 2, 3, 5], default=1)
    execute_button = param.Action(lambda x: x.param.trigger('execute_button'), label='Execute')
    loading_widget = pn.indicators.LoadingSpinner(value=False, width=50, height=50)

    def __init__(self, **params):
        super().__init__(**params)
        self.execute_button = self.execute_button
        self._register_callbacks()

    def _register_callbacks(self):
        self.param.watch(self.execute, 'execute_button')

    def execute(self, event):
        self.loading_widget.value = True
        time.sleep(self.duration)
        self.loading_widget.value = False

    def view(self):
        return pn.Column(self.param, self.loading_widget)
