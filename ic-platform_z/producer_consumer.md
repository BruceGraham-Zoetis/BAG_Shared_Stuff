log: /var/log/vetscan/setscan-platform.log

docker exec -it vetscan-hub_broker_1 /bin/kafka-console-producer --bootstrap-server localhost:9092 --topic printAccessObject

docker exec -it vetscan-hub_broker_1 /bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic printJobState --from-beginning

//valid 
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "Print_to_PDF","fileName": "/home/bag/vetscan-hub/ic-platform/src/test/resources/file.pdf","duplexEnabled": true,"colorEnabled": true,"duplexEnabled": true,"copies": 3}}

// invalid printer
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "bogus printer name","fileName": "/home/bag/vetscan-hub/ic-platform/src/test/resources/file.pdf","duplexEnabled": true,"colorEnabled": true,"duplexEnabled": true,"copies": 3}}

// invalid file name
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "Print_to_PDF","fileName": "bogus.pdf","duplexEnabled": true,"colorEnabled": true,"duplexEnabled": true,"copies": 3}}

// printerName not provided. should use default printer "Print_to_PDF".
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "","fileName": "/home/bag/vetscan-hub/ic-platform/src/test/resources/file.pdf","duplexEnabled": true,"colorEnabled": true,"duplexEnabled": true,"copies": 3}}

// options not provided. should default to false for each option.
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "Print_to_PDF","fileName": "/home/bag/vetscan-hub/ic-platform/src/test/resources/file.pdf","copies": 3}}

// copies not provided. should default to 1.
{"action": "PRINT_FILE", "payload": {"correlationID": 123, "printerName": "Print_to_PDF","fileName": "/home/bag/vetscan-hub/ic-platform/src/test/resources/file.pdf","duplexEnabled": true,"colorEnabled": true,"duplexEnabled": true}}




