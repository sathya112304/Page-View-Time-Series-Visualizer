import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time_series as ts

class TestTimeSeriesVisualizer(unittest.TestCase):

    def test_draw_line_plot(self):
        fig = ts.draw_line_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        self.assertEqual(fig.axes[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        self.assertEqual(fig.axes[0].get_xlabel(), "Date")
        self.assertEqual(fig.axes[0].get_ylabel(), "Page Views")

    def test_draw_bar_plot(self):
        fig = ts.draw_bar_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        self.assertEqual(fig.axes[0].get_xlabel(), "Years")
        self.assertEqual(fig.axes[0].get_ylabel(), "Average Page Views")

    def test_draw_box_plot(self):
        fig = ts.draw_box_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        self.assertEqual(fig.axes[0].get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(fig.axes[1].get_title(), "Month-wise Box Plot (Seasonality)")
        self.assertEqual(fig.axes[0].get_xlabel(), "Year")
        self.assertEqual(fig.axes[0].get_ylabel(), "Page Views")
        self.assertEqual(fig.axes[1].get_xlabel(), "Month")
        self.assertEqual(fig.axes[1].get_ylabel(), "Page Views")

if __name__ == "__main__":
    unittest.main()