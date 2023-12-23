# README #

### What is this repository for? ###

* Quick summary
The purpose of this respository is to have an Arduino script that you can add to platform IO. The script will create a header file that will give you these as cpp variables.
* Version 1.1

### How do I get set up? ###

* Summary of set up

1. Copy py script to your project folder
2. In your platform.ini file, include this line:
```extra_scripts = pre:embed_git_info.py```
3. Include generated header in your main.cpp file: ```#include "git_info.h"```
4. Add a serial printout for your git info:
```
  // This is the recommended setup, you may choose other setups
  Serial.print("Git Information:\n");
  Serial.print("Build Date/Time (local time): "); Serial.print(BUILD_DATE); Serial.print("\n");
  Serial.print("Builder Name: "); Serial.print(GIT_NAME); Serial.print(" Email: "); Serial.print(GIT_EMAIL); Serial.print("\n");
  Serial.print("Repository URL: "); Serial.print(GIT_REPO_URL); Serial.print("\n");
  Serial.print("Branch: "); Serial.print(GIT_BRANCH); Serial.print(" Tag: "); Serial.print(GIT_TAG); Serial.print("\n\n"); // Optional, only use if using tags.
  Serial.print("Commit Hash: "); Serial.print(GIT_COMMIT_HASH); Serial.print("\n");
  Serial.print("CRC: "); Serial.println(static_cast<long>(MAIN_FILE_CRC));
  Serial.print("\n=================================\n");

  // These are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  // To enable, go into python script and uncomment.
  //Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  //Serial.print("Author: "); Serial.println(GIT_AUTHOR);
  //Serial.print("Author Email: "); Serial.println(GIT_AUTHOR_EMAIL);
  //Serial.print("Git Update Date");


```
or if using streaming library:
```
// Using Streaming Library
  Serial << "Git Information:\n"
    << "Build Date/Time (local time): " << BUILD_DATE << "\n"
    << "Builder Name:  " << GIT_NAME << " Email: " << GIT_EMAIL  << "\n"
    << "Repository URL: " << GIT_REPO_URL << "\n"
    << "Branch: " << GIT_BRANCH << " Tag: " << GIT_TAG  << "\n\n"
    << "Commit Hash: " << GIT_COMMIT_HASH << "\n" 
    << "CRC: " << static_cast<long>(MAIN_FILE_CRC) 
    << "\n=================================\n";
```

* Configuration: It is recommended to make a function that does all of this printing, as it helps simplify code. You may organize how you desire, but this is how I prefer it.
* Dependencies:
PlatformIO is necessary, this will not work with Arduino IDE. Python is also a dependency, but this script uses platformIO's python environment, so no download or install is necessary. In fact, it is likely this code will not run successfully on your local environment, it is designed to be ran in PlatformIO python environment.

### Who do I talk to? ###

Repo owner: Elon Goliger egoliger@exploratorium.edu