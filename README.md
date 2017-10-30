# Insight-Assingment:
#In this readme I will provide a complete breakdown of my code, as it was asked in the assingment. 
#First, I read the file and tryed it for erors. Then I made each line (one at a time) into a lists of values.
#I checked and separated the important values (ID, date, zip, total amount), and also made sure that Other ID was null.
#I created a new list containing just the aforementioned important values.
#I made two different checks (1) for valide date and (2) for valide zip.
#If (1) was true then the list was a potential input to the medians_by_zip.txt.
#Yet the list could not have been added straight, so I made a search algorhitm that found all the values already present in the list(if thelength was not empty).
#Out of allthese found values I made a heap, andusing mix-max heaps I was able to calculate the runing median (for the idea I thank Venkl @http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/).
#Then I had to reconfigure the running median value column for all preceedign rows.
#Finally, I addedthe row to an unsorted 2D list of values.
#Next, if (2) was true (which may have not been excluded by (1)) then the list was a potential candidate for medians_by_dt.txt.
#medians_by_dt.txt had to come out sorted, so I desired to make it an AVL tree with binary search.
#Each row candidate was transformed into a node (absolutely typial), with one nuance, every node had two additional internal data values.
#The two datafields: was acount integer (corresponding to the amount of times there was a donation) and a list containing all the donation sums.
#Obviously, the pair (ID, date) were the keys.
#Then the node was going through the insertion process, which included a binary search through the tree. 
#If the search found nothing the node was simply inserted and the tree reabalnced.
#Yet if the search came up with the node, then the count of that node was increased, and its array got a new value.
#Next,I wrote to medianvals_by_zip.txt.
#Finally, I wrote medianvals_by_dt.txtusing th ebuilt in toString function of the AVL class. 
#This function has a built in feature which gets a median of every node (using the numpy median function).
