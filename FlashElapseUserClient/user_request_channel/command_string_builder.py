'''This file has the template for the string used by the front end to communicate 
   the back end. In the real communication, it will communicate in json format
   and the rpb controller will know how to translate it
   The command inside should be well documented for developer to communicate between 
   these two part. 
   '''

 class CommandStringBuilder():
 	'''This builder builds the string for transfering the communication. This is the 
 		front end file, and it's been placed here for test and command line way of input
		The property and the string inside will be used by the rpb controller to translate. 
		Make sure they talk in the same vocabulary
		For different command, in the future, it might have subclass for different use in the 
		front end.

		  '''

 	def __init__ (self, cmd_manager):
 		

 		pass;
