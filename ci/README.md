## Project Overview

It is necessary to create a pipeline to work with a real project containing a compilation (if necessary), testing, building packages (*.deb, *.rpm or wheel) for two operating systems (Ubuntu and CentOS), and demonstrate its functionality. 

---

#### Requirements:

- build docker images with Ubuntu and CentOS and necessary dependencies and put them into registry
- load project code, .gitlab-ci.yml, Dockerfile's, Vagrantfile for virtual machines, playbook.yml into repository
- make several commits in dev branch:
    + with incorrect tests - pipeline fails
    + with correct tests - pipeline runs properly
- perform MR and merge from dev to staging branch - pipeline should run, build packages and save them in artifacts
- perform MR from staging to main - pipeline also should run properly
 