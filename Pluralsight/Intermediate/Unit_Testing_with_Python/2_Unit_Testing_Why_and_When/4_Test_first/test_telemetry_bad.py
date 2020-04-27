import...

class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_check_transmission_should_send_a_diagnostic_message_and_recaive_status_mesage_response(self):
        constrols = TelemetryDiagnostocControls(MockTelemetryClient(online=True, receive_data='foo'))
        constrols.check_transmission()
        self.assertEqual('foo', controls.diagnostic_info)
        
    def test_check_transmission_fails_if_telemetry_client_doesnt_connect(self):
        constrols = TelemetryDiagnostocControls(MockTelemetryClient(online=True, receive_data='foo'))
        self.assertRaises(Exception, control.check_transmission)
        self.assertEqual('foo', controls.diagnostic_info)
        
    def test_check_transmission_fails_if_telemetry_client_disconnects_before_receive(self):
        constrols = TelemetryDiagnostocControls(MockTelemetryClient(online=True, receive_data='foo', go_offline_on_send=False))
        self.assertRaises(Exception, control.check_transmission)
        self.assertEqual('foo', controls.diagnostic_info)

class MockTelemetryClient:

    def __init__(self, online, receive_data='', go_offline_on_send=False, go_online_on_third_attempt=False):
        self.online_status = online
        self.receive_data = receive_data
