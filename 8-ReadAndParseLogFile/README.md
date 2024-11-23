# Read and parse log file

Skripts atver failu (1.arguments) un tajā meklē rindas ar norādīto Keyword (2.arguments) un izvada atrastās rindas.
Ja ir norādīts pattern, tad izmantojot regex atrāda tikai nepieciešmo info katrā rindā

Testa fails:
2024-11-23 10:15:32 USB_DEVICE_ATTACHED: VID=1234, PID=5678, Port=3
2024-11-23 10:15:33 SYSTEM_INFO: CPU Usage: 15%, Memory Usage: 43%
2024-11-23 10:15:34 USB_DATA_SENT: Endpoint=0x01, DataLength=512, CRC=0x8F3A
2024-11-23 10:15:35 USB_DEVICE_DETACHED: VID=1234, PID=5678, Port=3
2024-11-23 10:15:36 SYSTEM_INFO: Network Latency: 18ms, Jitter: 2ms
2024-11-23 10:15:37 PROCESS_STARTED: Application=Notepad, PID=1024
2024-11-23 10:15:38 USB_DEVICE_ATTACHED: VID=8765, PID=4321, Port=1


Piemērs: python 8-ParseLogFile.py testa_fails.txt USB
Fails: <_io.TextIOWrapper name='testa_fails.txt' mode='r' encoding='cp1252'>
2024-11-23 10:15:32 USB_DEVICE_ATTACHED: VID=1234, PID=5678, Port=3
2024-11-23 10:15:34 USB_DATA_SENT: Endpoint=0x01, DataLength=512, CRC=0x8F3A
2024-11-23 10:15:35 USB_DEVICE_DETACHED: VID=1234, PID=5678, Port=3
2024-11-23 10:15:38 USB_DEVICE_ATTACHED: VID=8765, PID=4321, Port=1

Piemērs: python 8-ParseLogFile.py testa_fails.txt USB --pattern "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w*USB\w*"
Fails: <_io.TextIOWrapper name='testa_fails.txt' mode='r' encoding='cp1252'>
2024-11-23 10:15:32 USB_DEVICE_ATTACHED
2024-11-23 10:15:34 USB_DATA_SENT
2024-11-23 10:15:35 USB_DEVICE_DETACHED
2024-11-23 10:15:38 USB_DEVICE_ATTACHED
