 
   // This is the recommended setup, you may choose other setups
Serial.print("Git Information:\n");
Serial.print("Build Date/Time (local time): "); Serial.print(BUILD_DATE); Serial.print("\n");
Serial.print("Builder's Name: "); Serial.print(GIT_USER_NAME); Serial.print(" Email: "); Serial.print(GIT_USER_EMAIL); Serial.print("\n");
Serial.print("Repository URL: "); Serial.print(GIT_REPO_URL); Serial.print("\n");
Serial.print("Branch: "); Serial.print(GIT_BRANCH); Serial.print(" | Tag: "); Serial.print(GIT_TAG); Serial.print("\n\n"); // Optional, only use if using tags.
Serial.print("Commit Hash: "); Serial.print(GIT_COMMIT_HASH); Serial.print("\n");
Serial.print("CRC: "); Serial.println(static_cast<long>(MAIN_FILE_CRC));
Serial.print("\n=================================\n");

  // These are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  // To enable, go into python script and uncomment.
  //Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  //Serial.print("Git Update Date"); Serial.println(GIT_UPDATE_DATE); // Optional, depending on your workflow

```
// If using Streaming Library: https://github.com/janelia-arduino/Streaming
  Serial << "Git Information:\n"
    << "Build Date/Time (local time): " << BUILD_DATE << "\n"
    << "Builder's Name:  " << GIT_USER_NAME << " Email: " << GIT_USER_EMAIL  << "\n"
    << "Repository URL: " << GIT_REPO_URL << "\n"
    << "Branch: " << GIT_BRANCH << " | Tag: " << GIT_TAG  << "\n\n"
    << "Commit Hash: " << GIT_COMMIT_HASH << "\n" 
    << "CRC: " << static_cast<long>(MAIN_FILE_CRC) 
    << "\n=================================\n";