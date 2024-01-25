 
   // This is the recommended setup, you may choose other setups
// Note: The F macro is used to store the string in flash memory, which is where the Arduino stores the sketch. This is to save RAM.
// however, it only does stuff for AVR boards, so it's not necessary for ARM boards. It doesn't hurt to use it though.
Serial.print(F("Git Information:\n"));
Serial.print(F("Build Date/Time (local time): ")); Serial.print(BUILD_DATE); Serial.print(F("\n"));
Serial.print(F("Builder's Name: ")); Serial.print(GIT_USER_NAME); Serial.print(F(" Email: ")); Serial.print(GIT_USER_EMAIL); Serial.print(F("\n"));
Serial.print(F("Repository URL: ")); Serial.print(GIT_REPO_URL); Serial.print(F("\n"));
Serial.print(F("Branch: ")); Serial.print(GIT_BRANCH); Serial.print(F(" | Tag: ")); Serial.print(GIT_TAG); Serial.print(F("\n\n")); // Optional, only use if using tags.
Serial.print(F("Commit Hash: ")); Serial.print(GIT_COMMIT_HASH); Serial.print(F("\n"));
Serial.print(F("\n=================================\n"));
Serial.flush(); // Flush the buffer to ensure all the data is sent to the serial port

  // These are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  // To enable, go into python script and uncomment.
  //Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  //Serial.print("Git Update Date"); Serial.println(GIT_UPDATE_DATE); // Optional, depending on your workflow

// If using Streaming Library: https://github.com/janelia-arduino/Streaming
Serial << F("Git Information:\n")
  << F("Build Date/Time (local time): ") << BUILD_DATE << F("\n")
  << F("Builder's Name:  ") << GIT_USER_NAME << F(" Email: ") << GIT_USER_EMAIL  << F("\n")
  << F("Repository URL: ") << GIT_REPO_URL << F("\n")
  << F("Branch: ") << GIT_BRANCH << F(" | Tag: ") << GIT_TAG  << F("\n\n")
  << F("Commit Hash: ") << GIT_COMMIT_HASH << F("\n") 
  << F("\n=================================") << endl;