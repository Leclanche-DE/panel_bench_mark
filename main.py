from panel import serve
from dashboard_a import DashboardA
from dashboard_b import DashboardB
from dashboard_c import DashboardC

dashboards = {'A': DashboardA().view, 'B': DashboardB().view, 'C': DashboardC().view}

if __name__ == '__main__':
    serve(dashboards)
