#!/usr/bin/env python3
"""
@breif CMeasurementOperation.py

Purpose: Simulates the analyzer's measurement features
"""

class CMeasurementOperation():
    def __init__(self, measurement_id, elapsed_time_msec, measurement_status, status_detail):
        # str: ?
        self.measurement_id     = measurement_id
        # str: 0 to ?
        self.elapsed_time_msec  = elapsed_time_msec
        # str: enum = "Initializing", "Running", "Aborted", "Stopping", "Complete"
        self.measurement_status = measurement_status
        # str: "" or some kind of detail string 
        self.status_detail      = status_detail

    def measurement_results_get(self, start_datetime, end_datetime):
        # TODO Use start_datetime, end_datetime during the get.
        # start_datetime = util.deserialize_datetime(start_datetime)
        # end_datetime = util.deserialize_datetime(end_datetime)

        dict_rtn = self.get_status()
        return dict_rtn

    def get_status(self):
        dict_rtn = {
            'measurement_id': self.measurement_id,
            'elapsed_time_msec': self.elapsed_time_msec,
            'measurement_status': self.measurement_status,
            'status_detail': self.status_detail
        }
        return dict_rtn

    def cancel(self):
        self.measurement_id     = ''
        self.elapsed_time_msec  = '0'
        self.measurement_status = 'Complete'
        self.status_detail      = ''
        dict_rtn = self.get_status()
        return dict_rtn


