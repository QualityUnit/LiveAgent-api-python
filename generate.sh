#!/bin/sh

java -XX:MaxPermSize=256M -Xmx1024M -jar "../swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate -i "../LiveAgent/codegen/descriptor/liveagent.yaml" -l python -o "." -c ./client.json
