import collections


class Aircraft(collections.namedtuple('Aircraft', ['jsbsim_id', 'flightgear_id',
                                                   'name', 'cruise_speed_kts'])):
    KTS_TO_M_PER_S = 0.51444
    KTS_TO_FT_PER_S = 1.6878

    def get_max_distance_m(self, episode_time_s: float) -> float:
        """ Estimates the maximum distance this aircraft can travel in an episode """
        margin = 0.1
        return self.cruise_speed_kts * self.KTS_TO_M_PER_S * episode_time_s * (1 + margin)

    def get_cruise_speed_fps(self) -> float:
        return self.cruise_speed_kts * self.KTS_TO_FT_PER_S
