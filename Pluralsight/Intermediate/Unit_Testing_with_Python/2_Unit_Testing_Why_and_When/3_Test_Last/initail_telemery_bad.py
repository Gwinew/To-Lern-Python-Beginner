class TelemetryDiagnosticControls:
    DiagnosticChannelConnectionString = '*111#'

    def __init__(self):                      
        self.telemetry_clien =  TelemetryClient()  
        self.diagnostic_info = ''

    def check_transmission(self):
        self.diagnostic_info = ''

        self.telemetry_client.disconnect()
        retries_left = 3
        while not self.telemetry_client.get_online_status() and retries_left = 0:
            self.telemetry_client.connect(TelemetryDiagnosticControls.DiagnosticChannelConnectionString)
            retries_left -= 1
        if not self.telemetry_client.get_online_status():
            raise Exception('Unable to connect.')

        self.telemetry_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        self.diagnostic_info = self.telemetry_client.receive()

class TelemetryClient:
    DIAGNOSTIC_MESSAGE = 'AT#UD'

    def __init__(self):
        self.online_status = False
        self._diagnostic_message_result = ''
