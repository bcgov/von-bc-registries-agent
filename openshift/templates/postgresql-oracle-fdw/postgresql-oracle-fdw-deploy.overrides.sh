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

_userName=$(generateUsername)
_password=$(generatePassword)
_adminPassword=$(generatePassword)
_fdwUserName=$(generateUsername)
_fdwPassword=$(generatePassword)

SPECIALDEPLOYPARMS="-p POSTGRESQL_USER=${_userName} -p POSTGRESQL_PASSWORD=${_password} -p POSTGRESQL_ADMIN_PASSWORD=${_adminPassword} -p FDW_USER=${_fdwUserName} -p FDW_PASS=${_fdwPassword}"
echo ${SPECIALDEPLOYPARMS}

