_includeFile=$(type -p overrides.inc)
if [ ! -z ${_includeFile} ]; then
  . ${_includeFile}
else
  _red='\033[0;31m'; _yellow='\033[1;33m'; _nc='\033[0m'; echo -e \\n"${_red}overrides.inc could not be found on the path.${_nc}\n${_yellow}Please ensure the openshift-developer-tools are installed on and registered on your path.${_nc}\n${_yellow}https://github.com/BCDevOps/openshift-developer-tools${_nc}"; exit 1;
fi

# ======================================================
# Special Deployment Parameters needed for DB Deployment
# ------------------------------------------------------
# The results need to be encoded as OpenShift template
# parameters for use with oc process.
# ======================================================

if createOperation; then
  printStatusMsg "Creating a set of random user credentials ..."
  writeParameter "POSTGRESQL_USER" $(generateUsername) "false"
  writeParameter "POSTGRESQL_PASSWORD" $(generatePassword) "false"
  writeParameter "POSTGRESQL_ADMIN_PASSWORD" $(generatePassword) "false"

  readParameter "FDW_USER - Please provide the username required to athenticate with the foreign database.\nIf left blank, a random username will be created however it will likely cause authentication to fail:" FDW_USER $(generateUsername) "false"
  readParameter "FDW_PASS - Please provide the password required to athenticate with the foreign database.\nIf left blank, a random password will be created however it will likely cause authentication to fail:" FDW_PASS $(generatePassword) "false"
  
  readParameter "FDW_FOREIGN_SCHEMA - Please provide the schema name.  Values are case sensitive." FDW_FOREIGN_SCHEMA "" "false"
  readParameter "FDW_FOREIGN_SERVER - Please provide the connection string information.  [HostName|HostIpAddress]:PortNumber/ListenerServiceName Values are case sensitive." FDW_FOREIGN_SERVER "" "false"
else
  # Secrets are removed from the configurations during update operations ...
  printStatusMsg "Update operation detected ...\nSkipping the generation of random user credentials ...\nSkipping the prompts for the FDW_USER, and FDW_PASS ...\n"
  # Generated
  writeParameter "POSTGRESQL_USER" "generation_skipped" "false"
  writeParameter "POSTGRESQL_PASSWORD" "generation_skipped" "false"
  writeParameter "POSTGRESQL_ADMIN_PASSWORD" "generation_skipped" "false"
  # Prompted
  writeParameter "FDW_USER" "generation_skipped" "false"
  writeParameter "FDW_PASS" "generation_skipped" "false"

  readParameter "FDW_FOREIGN_SCHEMA - Please provide the schema name.  Values are case sensitive." FDW_FOREIGN_SCHEMA "" "false"
  readParameter "FDW_FOREIGN_SERVER - Please provide the connection string information.  [HostName|HostIpAddress]:PortNumber/ListenerServiceName Values are case sensitive." FDW_FOREIGN_SERVER "" "false"
fi

SPECIALDEPLOYPARMS="--param-file=${_overrideParamFile}"
echo ${SPECIALDEPLOYPARMS}