for app in $apps; do
       # Check if the deployment-config.json exists for the app
       configPath="apps/$app/deployment-configs/deployment-config.${{ parameters.target_environment }}.json"
       if [ -f "$configPath" ]; then
          secretName=$(jq -r '.secretName' "$configPath") # Retrieve secret name from config file
          # TODO: RETRIEVE SECRET STORED IN A SECURE PLACE!
       fi
    done
