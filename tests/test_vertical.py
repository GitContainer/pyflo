
import unittest


from pyflo.geometry.vertical import Profile


class VerticalCurveTest(unittest.TestCase):

    def setUp(self):
        self.profile = Profile()
        self.profile.create_pt(113600.00, 063.003)
        self.profile.create_pt(114712.97, 051.873, 0800.0)
        self.profile.create_pt(117454.76, 099.854, 2360.0)
        self.profile.create_pt(119104.00, 052.026, 0800.0)
        self.profile.create_pt(120633.36, 059.673, 0800.0)
        self.profile.create_pt(122474.50, 114.907, 1700.0)
        self.profile.create_pt(124750.00, 108.081, 0800.0)
        self.profile.create_pt(126341.51, 139.911, 2000.0)
        self.profile.create_pt(127829.35, 113.130, 0800.0)
        self.profile.create_pt(131083.05, 103.369, 0800.0)
        self.profile.create_pt(132155.02, 108.729, 1000.0)
        self.profile.create_pt(134842.88, 092.601, 0800.0)
        self.profile.create_pt(136497.65, 112.176)
        self.pt1 = self.profile.pts[1]
        self.pt_next = self.profile.pt_pvt_next(120400.00)

    def test_g1(self):
        expected = -0.010
        produced = self.pt1.g1()
        self.assertAlmostEqual(expected, produced, 3)

    def test_g2(self):
        expected = 0.017
        produced = self.pt1.g2()
        self.assertAlmostEqual(expected, produced, 3)

    def test_r(self):
        expected = 0.344
        produced = self.pt1.r()
        self.assertAlmostEqual(expected, produced, 3)

    def test_pvc_station(self):
        expected = 114312.97
        produced = self.pt1.pvc_station
        self.assertAlmostEqual(expected, produced, 2)

    def test_pvt_station(self):
        expected = 115112.97
        produced = self.pt1.pvt_station
        self.assertAlmostEqual(expected, produced, 2)

    def test_g1_next(self):
        expected = 0.005
        produced = self.pt_next.g1()
        self.assertAlmostEqual(expected, produced, 3)

    def test_r_next(self):
        expected = 0.312
        produced = self.pt_next.r()
        self.assertAlmostEqual(expected, produced, 3)

    def test_pvc_station_next(self):
        expected = 120233.36
        produced = self.pt_next.pvc_station
        self.assertAlmostEqual(expected, produced, 2)

    def test_slopes(self):
        s1 = round(self.profile.slope(120500.00), 3)
        s2 = round(self.profile.slope(120400.00), 3)
        s3 = round(self.profile.slope(120300.00), 3)
        s4 = round(self.profile.slope(120233.36), 3)
        s5 = round(self.profile.slope(119504.00), 3)
        s6 = round(self.profile.slope(119386.35), 3)
        s7 = round(self.profile.slope(119225.00), 3)
        s8 = round(self.profile.slope(119386.35), 3)
        s9 = round(self.profile.slope(119225.00), 3)
        s10 = round(self.profile.slope(119386.35), 3)
        s11 = round(self.profile.slope(120300.00), 3)
        s12 = round(self.profile.slope(120233.36), 3)
        s13 = round(self.profile.slope(119504.00), 3)
        s14 = round(self.profile.slope(119386.35), 3)
        s15 = round(self.profile.slope(117595.00), 3)
        s16 = round(self.profile.slope(117850.00), 3)
        s17 = round(self.profile.slope(118170.00), 3)
        s18 = round(self.profile.slope(118470.00), 3)
        s19 = round(self.profile.slope(118605.00), 3)
        s20 = round(self.profile.slope(118940.00), 3)
        s21 = round(self.profile.slope(119225.00), 3)
        s22 = round(self.profile.slope(119386.35), 3)
        s23 = round(self.profile.slope(114980.00), 3)
        s24 = round(self.profile.slope(114773.06), 3)
        s25 = round(self.profile.slope(114065.00), 3)
        s26 = round(self.profile.slope(114200.00), 3)
        s27 = round(self.profile.slope(114412.85), 3)
        s28 = round(self.profile.slope(114603.88), 3)
        produced = (
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20,
            s21, s22, s23, s24, s25, s26, s27, s28
        )
        expected = (
            0.013,
            0.010,
            0.007,
            0.005,
            0.005,
            0.000,
            -0.007,
            0.000,
            -0.007,
            0.000,
            0.007,
            0.005,
            0.005,
            0.000,
            -0.009,
            -0.014,
            -0.020,
            -0.026,
            -0.028,
            -0.019,
            -0.007,
            0.000,
            0.013,
            0.006,
            -0.010,
            -0.010,
            -0.007,
            0.000,
        )
        self.assertTupleEqual(expected, produced)

    def test_elevation(self):
        produced = round(self.profile.elevation(114065.00), 3)
        expected = 58.353
        self.assertAlmostEqual(expected, produced, 3)
    
    def test_elevations(self):
        z1 = round(self.profile.elevation(120500.00), 3)
        z2 = round(self.profile.elevation(120400.00), 3)
        z3 = round(self.profile.elevation(120300.00), 3)
        z4 = round(self.profile.elevation(120233.36), 3)
        z5 = round(self.profile.elevation(119504.00), 3)
        z6 = round(self.profile.elevation(119386.35), 3)
        z7 = round(self.profile.elevation(119225.00), 3)
        z8 = round(self.profile.elevation(119386.35), 3)
        z9 = round(self.profile.elevation(120300.00), 3)
        z10 = round(self.profile.elevation(120233.36), 3)
        z11 = round(self.profile.elevation(119504.00), 3)
        z12 = round(self.profile.elevation(119386.35), 3)
        produced = (
            z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12
        )
        expected = (
            60.117,
            58.940,
            58.076,
            57.673,
            54.026,
            53.732,
            54.285,
            53.732,
            58.076,
            57.673,
            54.026,
            53.732
        )
        self.assertTupleEqual(expected, produced)
