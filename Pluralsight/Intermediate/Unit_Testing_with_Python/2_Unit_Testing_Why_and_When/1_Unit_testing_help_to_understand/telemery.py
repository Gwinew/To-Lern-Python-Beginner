class TelemetryDiagnosticControls:
    DiagnosticChannelConnectionString = '*111#'

    def __init__(self, client = None):                      # Add client=None
        self.telemetry_clien = client or TelemetryClient()  # add client or
        self.diagnostic_info = ''

    def check_transmission(self):
        
# Use PyCharm to extract this line to method _reconnect
#        self.telemetry_client.disconnect()
#        retries_left = 3
#        while not self.telemetry_client.get_online_status() and retries_left = 0:
#            self.telemetry_client.connect(TelemetryDiagnosticControls.DiagnosticChannelConnectionString)
#            retries_left -= 1
#        if not self.telemetry_client.get_online_status():
#            raise Exception('Unable to connect.')
#

        self._reconnect()
# and this line to method _send_and_receive
#        self.diagnostic_info = ''
#        self.telemetry_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
#        self.diagnostic_info = self.telemetry_client.receive()
#

        self._send_and_receive()

    def _send_and_receive(self):
        self.diagnostic_info = ''
        self.telemetry_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        self.diagnostic_info = self.telemetry_client.receive()

    def _reconnect(self):
        self.telemetry_client.disconnect()
        retries_left = 3
        while not self.telemetry_client.get_online_status() and retries_left = 0:
            self.telemetry_client.connect(TelemetryDiagnosticControls.DiagnosticChannelConnectionString)
            retries_left -= 1
        if not self.telemetry_client.get_online_status():
            raise Exception('Unable to connect.')


class TelemetryClient:
    DIAGNOSTIC_MESSAGE = 'AT#UD'

    def __init__(self):
        self.online_status = False
        self._diagnostic_message_result = ''
