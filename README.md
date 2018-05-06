# TestStandInterfaceServer

## The PARSEC Language

Please check out the [PARSEC Documentation](https://goo.gl/HHzsXD) for example code, definition of key words, and other reference materials.

In this project, we have written a scripting language, dubbed PARSEC, for use in controlling the valves on the Test Stand. Parsed using PLY (Python Lex-Yacc), our language is described by a CFG in Yacc, and instances of the code are tokenized by Lex. 

PARSEC provides support for easy control of valves and reading of sensor values, with a user-friendly API for controlling timing and parallelizing actions.


## Milestones

### Milestone Zero - Server Set up - Before Start of 2nd term
Set up a basic server on the Beagle Bone, which must be able to:
1. Receive commands from a remote client via wifi or ethernet
2. Send realtime data to a remote client
3. Record data locally to prevent data loss
4. If the EE's are ready: communicate with the EE boards to control the test stand

### Milestone One - Data Collection - Week 4 of 2nd term
1. CLI for starting/stopping a test, specify file to write to - 1 week (parallelizable)
2. All data from sensors stored in raw format to files - 1 week (parallelizable)
3. KTLO (Keeping the Lights On) tasks for the server, potentially including communicating with the EE boards  

### Milestone Two - Basic GUI - End of 2nd term
1. Infrastructure - Set up some sort of generic GUI. Docker based? - 2 weeks
2. Add buttons/etc to start/stop a test - <1 week
3. Add a real-time graph of the data coming in - 2 weeks

### Milestone Three - Better Reporting and Analysis - Infinitely Optimizable
1. Add video and recording capabilities - 4 weeks
2. Analyze the data and give relevant information

