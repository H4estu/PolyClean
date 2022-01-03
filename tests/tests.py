"""tests.py

Testing module.

"""

import geopandas as gpd
import unittest

from shapely.geometry import Polygon
from src import polyclean


class TestFunctions(unittest.TestCase):

    def test_fill_holes(self):
        poly_with_holes = Polygon(
            shell = [(0,0), (0,10), (10,10), (10,0), (0,0)],
            holes = [
                [(1,1), (1,2), (2,3), (1,1)],  # Area = 0.5
                [(5,5), (4,6), (5,7), (6,7), (7,6), (6,5), (5,5)]  # Area = 4
            ]
        )

        gdf = gpd.GeoDataFrame(geometry=[poly_with_holes], crs=3857)
        small_hole_filled = polyclean.fill_holes(gdf, 0.5)
        both_holes_filled = polyclean.fill_holes(gdf, 4)
        
        self.assertEqual(len(small_hole_filled.interiors[0]), 1)
        self.assertEqual(len(both_holes_filled.interiors[0]), 0)

if __name__ == '__main__':
    unittest.main()
