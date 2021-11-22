class Script {
  /**
   * @params {object} request
   */
  process_incoming_request({ request }) {
    var find = '\n';
    var regex = new RegExp(find, 'g');

    let data = request.content;
    let attachmentColor = `#36A64F`;
    let statusMsg = `Status`;
    let isError = data.statusCode === `ERROR`;
    if (isError) {
      statusMsg = `Error`;
      attachmentColor = `#A63636`;
    }

    let friendlyProjectName=``;
    if(data.friendlyProjectName) {
      friendlyProjectName = data.friendlyProjectName
    }

    let projectName=``;
    if (data.projectName) {
      projectName = data.projectName
      if(!friendlyProjectName) {
        friendlyProjectName = projectName
      }
    }

    if(projectName) {
      statusMsg += ` message received from [${friendlyProjectName}](https://console.pathfinder.gov.bc.ca:8443/console/project/${projectName}/overview):`;
    } else {
      statusMsg += ` message received:`;
    }

    if (isError) {
      statusMsg = `**${statusMsg}**`;
    }

    return {
      content:{
        text: statusMsg,
        attachments: [
          {
            text: `${data.message.replace(regex, '  \n')}`,
            color: attachmentColor
          }
        ]
      }
    };
  }
}