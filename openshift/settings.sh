export PROJECT_NAMESPACE="devex-von-bc-registries-agent"
export GIT_URI="https://github.com/bcgov/von-bc-registries-agent.git"
export GIT_REF="master"

# The templates that should not have their GIT referances(uri and ref) over-ridden
# Templates NOT in this list will have they GIT referances over-ridden
# with the values of GIT_URI and GIT_REF
export -a skip_git_overrides="postgresql-oracle-fdw-build.json backup-build.json"

# The project components
# - They are all contained under the main OpenShift folder.
export components="."

# The builds to be triggered after buildconfigs created (not auto-triggered)
export builds=""

# The images to be tagged after build
export images="postgresql-oracle-fdw schema-spy-with-oracle-jdbc"

# The routes for the project
export routes="schema-spy-oracle-fdw"
