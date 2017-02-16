#!/usr/bin/env python

import os
import sys
import json

albert_op = os.environ.get("ALBERT_OP")

if albert_op == "METADATA":
    metadata="""{
      "iid":"org.albert.extension.external/v2.0",
      "name":"Banking",
      "version":"1.0",
      "author":"Manuel Schneider",
      "dependencies":[],
      "trigger":"bank"
    }"""
    print(metadata)
    sys.exit(0)

elif albert_op == "NAME":
    print(IBAN)
    sys.exit(0)

elif albert_op == "INITIALIZE":
    sys.exit(0)

elif albert_op == "FINALIZE":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "TEARDOWNSESSION":
    sys.exit(0)

elif albert_op == "QUERY":

    albert_query = os.environ.get("ALBERT_QUERY")

    class Object(object):
        pass

    items = []

    #--------------------------- ADJUST THIS BLOCK -----------------------------
    item = Object()
    item.id = "bank_account"
    item.name = "Bank account"
    item.description = "Bank account (78788098)"
    item.icon = "accessories-calculator"
    item.actions = []

    # The things you want the action to copy to cb
    actionData = {
        "IBAN":"DE0587857857857856785557",
        "BIC":"GENODE5867867867ko58",
        "KNR":"586785678567",
        "BLZ":"5856785" }

    for key, value in actionData.items():
        action = Object()
        action.command = "sh"
        action.name = "Copy {} to clipboard".format(key)
        action.arguments = ["-c", 'echo -n "{0}" | xclip -i; echo -n "{0}" | xclip -i -selection clipboard;'.format(value)]
        item.actions.append(action)

    items.append(item)

    # You can add furter accounts here, just copy the block above

    #---------------------------------------------------------------------------

    results = []
    for it in items:
        results += [json.dumps(item, default=lambda o: o.__dict__)]

    print('{"items": [' + ", ".join(results) + "]}")
    sys.exit(0)

elif albert_op == "COPYTOCLIPBOARD":
    clipboard.copy(sys.argv[1])
    sys.exit(0)
