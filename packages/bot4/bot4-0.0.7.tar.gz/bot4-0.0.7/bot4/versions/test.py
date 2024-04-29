import json


with open('version_protocols.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps({"1.16.5": 754, 
                            "1.18": 757,
                            '1.18.0': 757,
                            "1.18.1": 757,
                            754: "1.16.5",
                            757: "1.18",
                            757: '1.18.0',
                            757: "1.18.1"}))






