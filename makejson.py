import json

intent_json = {
    'Alation-down': {
        'question': 'Is Alation Down',
        'response': 'https://datacatalog.intuit.com:8080/api/v1/health/full',
        'action': 'Alation is working'
    },
    'hive-query-not-running': {
        'question': 'I am not able to run a hive query. Can someone help',
        'response': 'Check if you have access to the EMR',
        'action': 'if the error contains, permission denied :1) Check if you have access to the EMR'
    },
    'access-schema-sbg': {
        'question': 'what is the process to get access to more schemas?'
                    'I get the following error when running a query  '
                    '"USAGE on SCHEMA SBG_SOURCE not granted for current user"',
        'response': 'can you check with the channel  #sbseg_qdplatform_help',
        'action': 'can you check with the channel  #sbseg_qdplatform_help'
    },
    'enable-alation-access': {
        'question': 'Could you please enable my alation access? '
                    'I think I used last month it was working fine, '
                    'what is the idle period before it is disabled ',
        'response': 'the idle time out Is 30 days',
        'action': 'the idle time out Is 30 days'
    },
    'access-bu': {
        'question': 'I am wondering how to get access to the BU - QBOA (MM) DB',
        'response': 'I will on my developers to get back to you',
        'action': 'I will on my developers to get back to you'
    },

}
with open('intent.json', 'w') as f:
    json.dump(intent_json, f)