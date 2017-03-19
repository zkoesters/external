#!/bin/bash

# Search zeal docsets from albert. Must have docsets installed.
# Ex: "zeal python,go,ruby print"

case $ALBERT_OP in
  "METADATA")
    STDOUT='{
      "iid":"org.albert.extension.external/v2.0",
      "name":"Zeal",
      "version":"1.0",
      "author":"Zachary Koesters",
      "dependencies":["zeal"],
      "trigger":"zeal "
    }'
    echo -n "${STDOUT}"
    exit 0
    ;;
  "INITIALIZE")
    if hash zeal 2>/dev/null; then
      exit 0
    else
      exit 1
    fi
    echo -n "{}"
    ;;
  "QUERY")
    docsets=`echo ${ALBERT_QUERY:5} | cut -d ' ' -f1`
    docquery=`echo ${ALBERT_QUERY:5} | cut -d ' ' -f2`
    echo -n '{
      "items":[{
        "id":"zeal",
        "name":"Search Zeal docsets",
        "description":"Search for '"'${docquery}'" in "'${docsets}'"'.",
        "icon":"zeal",
        "actions":[{
          "name":"zeal",
          "command":"zeal",
          "arguments":["'"dash-plugin://keys=${docsets}&query=${docquery}"'"]
        }]
      }]
    }'
    exit 0
    ;;
esac