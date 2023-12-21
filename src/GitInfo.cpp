#include "GitInfo.h"
#include <Arduino.h>

void GitInfo::printGitInfo() {
    Serial.println("Git Information:");
    Serial.print("Tag: "); Serial.println(GIT_TAG);
    Serial.print("Branch: "); Serial.println(GIT_BRANCH);
    Serial.print("Commit Hash: "); Serial.println(GIT_COMMIT_HASH);
    Serial.print("Author Email: "); Serial.println(GIT_AUTHOR_EMAIL);
    Serial.print("Repository Name: "); Serial.println(GIT_REPO_NAME);
    // Add more if needed
}
