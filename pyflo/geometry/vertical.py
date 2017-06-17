

class Point:

    def __init__(self, profile, station, elevation, length=0.0):
        """A vertical point along a profile.

        Args:
            profile (Profile): The parent profile, which can contain other points.
            station (float): The position along the profile, in :math:`feet`.
            elevation (float): The height from a specific datum, in :math:`feet`.
            length (float): The total curve distance, in :math:`feet`.

        """
        self.profile = profile
        self.station = station
        self.elevation = elevation
        self.length = length

    def pt_prev(self):
        if self is not self.profile.station_first:
            i = self.profile.pts.index(self)
            pt = self.profile.pts[i - 1]
            return pt

    def pt_next(self):
        if self is not self.profile.station_last:
            i = self.profile.pts.index(self)
            pt = self.profile.pts[i + 1]
            return pt

    def g1(self):
        pt = self.pt_prev()
        if pt:
            return (self.elevation-pt.elevation) / (self.station-pt.station)

    def g2(self):
        pt = self.pt_next()
        if pt:
            return (pt.elevation-self.elevation) / (pt.station-self.station)

    def r(self):
        g1, g2 = self.g1(), self.g2()
        if g1 and g2 and self.length:
            return (g2-g1) / self.length * 10000.0

    def k(self):
        g1, g2 = self.g1(), self.g2()
        if self.length and g1 and g2:
            return abs(self.length / (g2-g1) / 100.0)

    @property
    def pvc_station(self):
        return self.station - self.length/2.0

    @property
    def pvt_station(self):
        return self.station + self.length/2.0

    def pvc_elevation(self):
        return self.elevation + self.g1() * (self.pvc_station-self.station)

    def pvt_elevation(self):
        return self.elevation + self.g2() * (self.pvt_station - self.station)

    def pt_key(self):
        if self.r():
            return self.pvc_station - self.g1()/self.r()*10000.0


class Profile:

    def __init__(self):
        """A collection of points that represent a vertical alignment"""
        self.pts = []

    @property
    def station_first(self):
        if self.pts:
            return min(point.station for point in self.pts)
        return None

    @property
    def station_last(self):
        if self.pts:
            return max(point.station for point in self.pts)
        return None

    def create_pt(self, station, elevation, length=0.0):
        pt = Point(self, station, elevation, length)
        self.pts.append(pt)
        self.pts.sort(key=lambda p: p.station)
        return pt

    def pt_pvc_prev(self, station):
        for i, pt in enumerate(self.pts):
            pvc_station = pt.pvc_station
            if pvc_station > station:
                return self.pts[i - 1]

    def pt_pvt_next(self, station):
        for pt in self.pts:
            pvt_station = pt.pvt_station
            if pvt_station > station:
                return pt

    def slope(self, station):
        pt_pvc_prev = self.pt_pvc_prev(station)
        pt_pvt_next = self.pt_pvt_next(station)
        if pt_pvc_prev is pt_pvt_next:
            pt = pt_pvt_next
            return pt.g1() + (station-pt.pvc_station) * pt.r() / 10000.0
        return pt_pvt_next.g1()

    def elevation(self, station):
        pt_pvc_prev = self.pt_pvc_prev(station)
        pt_pvt_next = self.pt_pvt_next(station)
        pt = pt_pvt_next
        x = station-pt.pvc_station
        elevation = pt.pvc_elevation() + pt.g1()*x
        if pt_pvc_prev is pt_pvt_next:
            a = pt.g2()-pt.g1()
            elevation += a * x**2.0 / (2.0*pt.length)
        return elevation

    def pts_key(self):
        pts_key = []
        for pt in self.pts:
            pts_key.append(pt.pt_key())
        return pts_key
