_includeFile=$(type -p overrides.inc)
if [ ! -z ${_includeFile} ]; then
  . ${_includeFile}
else
  _red='\033[0;31m'; _yellow='\033[1;33m'; _nc='\033[0m'; echo -e \\n"${_red}overrides.inc could not be found on the path.${_nc}\n${_yellow}Please ensure the openshift-developer-tools are installed on and registered on your path.${_nc}\n${_yellow}https://github.com/BCDevOps/openshift-developer-tools${_nc}"; exit 1;
fi

# ========================================================================
# Special Deployment Parameters needed for the SchemaSpy Oracle instance.
# ------------------------------------------------------------------------
# The results need to be encoded as OpenShift template
# parameters for use with oc process.
#
# The generated config map is used to update the Caddy configuration
# ========================================================================

CONFIG_MAP_NAME=caddy-conf
SOURCE_FILE=./templates/schema-spy-oracle/Caddyfile
OUTPUT_FORMAT=json
OUTPUT_FILE=caddy-configmap_DeploymentConfig.json

printStatusMsg "Generating ConfigMap; ${CONFIG_MAP_NAME} ..."
generateConfigMap "${CONFIG_MAP_NAME}" "${SOURCE_FILE}" "${OUTPUT_FORMAT}" "${OUTPUT_FILE}"

_userName=$(generateUsername)
_password=$(generatePassword)
SPECIALDEPLOYPARMS="-p SCHEMASPY_USER=${_userName} -p SCHEMASPY_PASSWORD=${_password}"
echo ${SPECIALDEPLOYPARMS}

