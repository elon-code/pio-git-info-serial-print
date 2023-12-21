# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
The purpose of this respository is to have an Arduino script that you can add to platform IO. The script will create a header file that will give you these as cpp variables.
* Version 1

### How do I get set up? ###

* Summary of set up

1. Add py script to your project folder
2. In your platform.ini file, include this line:
```extra_scripts = pre:embed_git_info.py```
3. Include generated header in your main.cpp file: ```#include "git_info.h"```
4. Add a serial printout for your git info:
```
  Serial.println("Git Information:");
  Serial.print("Repository Name: "); Serial.println(GIT_REPO_NAME); // NECESSARY
  Serial.print("Date last updated (UTC): "); Serial.println(GIT_DATE); // NECESSARY
  Serial.print("Repository URL: "); Serial.println(REPO_URL); // NECESSARY
  Serial.print("Tag: "); Serial.println(GIT_TAG); // Optional, only use if using tags.
  Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  Serial.print("Commit Hash: "); Serial.println(GIT_COMMIT_HASH); // NECESSARY

  // These two are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  Serial.print("Author: "); Serial.println(GIT_AUTHOR);
  Serial.print("Author Email: "); Serial.println(GIT_AUTHOR_EMAIL);
```
or if using streaming library:
```
Serial << "Git Information:\n";
Serial << "Repository Name: " << GIT_REPO_NAME << '\n';
Serial << "Date last updated (UTC): " << GIT_DATE << '\n';
Serial << "Repository URL: " << REPO_URL << '\n';
Serial << "Tag: " << GIT_TAG << '\n';
Serial << "Branch: " << GIT_BRANCH << '\n';
Serial << "Commit Hash: " << GIT_COMMIT_HASH << '\n';
Serial << "Author: " << GIT_AUTHOR << '\n';
Serial << "Author Email: " << GIT_AUTHOR_EMAIL << '\n';
```

* Configuration: It is recommended to make a function that does all of this printing, as it helps simplify 
* Dependencies:
PlatformIO is necessary, this will not work with Arduino IDE. Python is also a dependency, but this script uses platformIO's python environment, so no download or install is necessary.

### Who do I talk to? ###

Repo owner: Elon Goliger egoliger@exploratorium.edu