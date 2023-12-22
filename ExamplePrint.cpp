  // This is the recommended setup, you may choose other setups
Serial.print("Git Information:\n");
  Serial.print("Build Date/Time (local time): "); Serial.print(BUILD_DATE); Serial.print("\n");
  Serial.print("Builder Name: "); Serial.print(GIT_NAME); Serial.print(" Email: "); Serial.print(GIT_EMAIL); Serial.print("\n");
  Serial.print("Repository URL: "); Serial.print(GIT_REPO_URL); Serial.print("\n");
  Serial.print("Branch: "); Serial.print(GIT_BRANCH); Serial.print(" Tag: "); Serial.print(GIT_TAG); Serial.print("\n\n"); // Optional, only use if using tags.
  Serial.print("Commit Hash: "); Serial.print(GIT_COMMIT_HASH); Serial.print("\n");
  Serial.print("CRC: "); Serial.println(static_cast<long>(MAIN_FILE_CRC));
  Serial.print("\n=================================\n");

  // These  are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  //Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  //Serial.print("Author: "); Serial.println(GIT_AUTHOR);
  //Serial.print("Author Email: "); Serial.println(GIT_AUTHOR_EMAIL);
  //Serial.print("Git Update Date");

  // Using Streaming Library
Serial << "Git Information:\n"
    << "Build Date/Time (local time): " << BUILD_DATE << "\n"
    << "Builder Name:  " << GIT_NAME << " Email: " << GIT_EMAIL  << "\n"
    << "Repository URL: " << GIT_REPO_URL << "\n"
    << "Branch: " << GIT_BRANCH << " Tag: " << GIT_TAG  << "\n\n"
    << "Commit Hash: " << GIT_COMMIT_HASH << "\n" 
    << "CRC: " << static_cast<long>(MAIN_FILE_CRC) 
    << "\n=================================\n";