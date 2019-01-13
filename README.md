# Introduction

Welcome to the Health Hackers AI/ML Project group's repo. This will be the group's codebase. If you want to join the group and contribute write an email to kaggle at pablo-gomez.net with your GitHub profile name. This repo will certainly grow over time, for now it's mostly a stub to help us get started. 

In the first meeting we decided to work on the [Kaggle Histopathologic Cancer Detection Challenge](https://www.kaggle.com/c/histopathologic-cancer-detection/overview).

If you have any questions or problems you can, of course, ask at the meetings, in the issues section here or via email/Slack.

# First Steps / How to get started

To get started you will need a few things. In particular, a recent python version, the TensorFlow framework (or PyTorch if you want) and the necessary accounts and such.

## Setup your system

These steps are necessary if you want to execute the code on your system.

### Python

We recommend using the [anaconda python platform](https://www.anaconda.com/distribution/). It has most of the stuff (modules etc.), that you will need, already and saves you from dependency hell by providing virtual python environments.

You can find installers for Windows, Linux and macOS [here](https://www.anaconda.com/download/).

### TensorFlow

At the first meeting it was decided that we will use [TensorFlow](https://www.tensorflow.org). 

Currently, TensorFlow does not support Python 3.7, therefore you will need to install 3.6. You can do this in the anaconda prompt by executing `conda install python=3.6` .

In the same prompt, you can install TensorFlow by running either `pip install tensorflow` or `pip install tensorflow-gpu` if you have a CUDA compatible GPU. If you want to use the GPU version you will need to install [additional dependencies](https://www.tensorflow.org/install/gpu). 
## Setup your Kaggle, GitHub and Slack

### Slack

TBA

### GitHub

If you are new to using git,  you can find an introduction [online](https://www.atlassian.com/git/tutorials/what-is-version-control).

A guide to installing to git on the common operating systems can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Depending on your terminal affinity, you might also want a GUI like GitKraken, TortoiseGit, etc.

To clone this repo follow [this guide](https://help.github.com/articles/cloning-a-repository/).

### Kaggle

To participate on [Kaggle](https://www.kaggle.com/) you will have to sign up there too. 

Then you can join the competition [here](https://www.kaggle.com/c/histopathologic-cancer-detection/overview).

Once you have accepted competition's terms you can download the related data [here](https://www.kaggle.com/c/11848/download-all).
