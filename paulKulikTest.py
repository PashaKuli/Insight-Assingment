import os
import sys
import re
from numpy import median


class Heap():#I implement heap to dealwith the rolling median of the unosrted list.
	def __init__(self):
		self.max_heap = [] # for half left
		self.min_heap = [] # for half right

	def addNum(self, num):
		size_left = len(self.max_heap)
		size_right = len(self.min_heap)
		if size_left == 0 and size_right == 0:
			heappush(self.min_heap, num)
			return
		
		if self.max_heap:
			left_val = -self.max_heap[0]
		if self.min_heap:
			right_val = self.min_heap[0]
		
		if size_left == size_right:
			if num <= left_val:
				heappush(self.max_heap, -num)
			else:
				heappush(self.min_heap, num)
		elif size_left > size_right:
			if num >= left_val:
				heappush(self.min_heap, num) # then balance
			else:
				tmp = heappop(self.max_heap)
				heappush(self.min_heap, -tmp)
				heappush(self.max_heap, -num)
		else: # size_left < size_right
			if num < right_val:
				heappush(self.max_heap, -num) # then balance
			else:
				tmp = heappop(self.min_heap)
				heappush(self.max_heap, -tmp)
				heappush(self.min_heap, num)       

	def findMedian(self):
		size_left = len(self.max_heap)
		size_right = len(self.min_heap)
		
		if size_left == size_right:
			return rounding((-self.max_heap[0] + self.min_heap[0])/2.0)
		elif size_left > size_right:
			return rounding((-self.max_heap[0]))
		else:
			return rounding((self.min_heap[0]))

class Node():#This is a node of the AVl Tree, the onyl difference from a standard construction is that this node also has an array and acount
#The array is mean to contain unique transatcions amounts, and the count shows how many donations came to the same organization on the same date.
	def __init__(self, input_list):
		self.input_list=[]
		self.input_list.append(input_list[0])
		self.input_list.append(input_list[1]) 
		self.parent = None
		self.leftChild = None
		self.rightChild = None
		self.height = 0 
		self.valueslist=append(input_list[2])
		self.count=1

	def max_children_height(self):
		if self.leftChild and self.rightChild:
			return max(self.leftChild.height, self.rightChild.height)
		elif self.leftChild and not self.rightChild:
			return self.leftChild.height
		elif not self.leftChild and  self.rightChild:
			return self.rightChild.height
		else:
			return -1
		
	def balance (self):
		return (self.leftChild.height if self.leftChild else -1) - (self.rightChild.height if self.rightChild else -1)

	def toString(self):
		try:
			printer=str(self[0])+"|"+str(self[1])+"|"+str(rounding(median(self.valueslist)))+"|"+str(self.count)+"|"
			+str(unorderedsum(self.valueslist))+"\n"
			return printer
		except:
			return None

class avlTree():
	def __init__(self, *args):
		self.rootNode = None
		self.elements_count = 0
		self.rebalance_count = 0
		if len(args) == 1:
			for i in args[0]:
				self.insert (i)
		
	def height(self):
		if self.rootNode:
			return self.rootNode.height
		else:
			return 0
		
	def rebalance (self, node_to_rebalance):
		self.rebalance_count += 1
		A = node_to_rebalance 
		F = A.parent #allowed to be NULL
		if node_to_rebalance.balance() == -2:
			if node_to_rebalance.rightChild.balance() <= 0:
				"""Rebalance, case RRC """
				B = A.rightChild
				C = B.rightChild
				assert (not A is None and not B is None and not C is None)
				A.rightChild = B.leftChild
				if A.rightChild:
					A.rightChild.parent = A
				B.leftChild = A
				A.parent = B                                                               
				if F is None:                                                              
				   self.rootNode = B 
				   self.rootNode.parent = None                                                   
				else:                                                                        
				   if F.rightChild == A:                                                          
					   F.rightChild = B                                                                  
				   else:                                                                      
					   F.leftChild = B                                                                   
				   B.parent = F 
				self.recompute_heights (A) 
				self.recompute_heights (B.parent)                                                                                         
			else:
				"""Rebalance, case RLC """
				B = A.rightChild
				C = B.leftChild
				assert (not A is None and not B is None and not C is None)
				B.leftChild = C.rightChild
				if B.leftChild:
					B.leftChild.parent = B
				A.rightChild = C.leftChild
				if A.rightChild:
					A.rightChild.parent = A
				C.rightChild = B
				B.parent = C                                                               
				C.leftChild = A
				A.parent = C                                                             
				if F is None:                                                             
					self.rootNode = C
					self.rootNode.parent = None                                                    
				else:                                                                        
					if F.rightChild == A:                                                         
						F.rightChild = C                                                                                     
					else:                                                                      
						F.leftChild = C
					C.parent = F
				self.recompute_heights (A)
				self.recompute_heights (B)
		else:
			assert(node_to_rebalance.balance() == +2)
			if node_to_rebalance.leftChild.balance() >= 0:
				B = A.leftChild
				C = B.leftChild
				"""Rebalance, case LLC """
				assert (not A is None and not B is None and not C is None)
				A.leftChild = B.rightChild
				if (A.leftChild): 
					A.leftChild.parent = A
				B.rightChild = A
				A.parent = B
				if F is None:
					self.rootNode = B
					self.rootNode.parent = None                    
				else:
					if F.rightChild == A:
						F.rightChild = B
					else:
						F.leftChild = B
					B.parent = F
				self.recompute_heights (A)
				self.recompute_heights (B.parent) 
			else:
				B = A.leftChild
				C = B.rightChild 
				"""Rebalance, case LRC """
				assert (not A is None and not B is None and not C is None)
				A.leftChild = C.rightChild
				if A.leftChild:
					A.leftChild.parent = A
				B.rightChild = C.leftChild
				if B.rightChild:
					B.rightChild.parent = B
				C.leftChild = B
				B.parent = C
				C.rightChild = A
				A.parent = C
				if F is None:
				   self.rootNode = C
				   self.rootNode.parent = None
				else:
				   if (F.rightChild == A):
					   F.rightChild = C
				   else:
					   F.leftChild = C
				   C.parent = F
				self.recompute_heights (A)
				self.recompute_heights (B)
				
	def sanity_check (self, *args):
		if len(args) == 0:
			node = self.rootNode
		else:
			node = args[0]
		if (node  is None) or (node.is_leaf() and node.parent is None ):
			# trival - no sanity check needed, as either the tree is empty or there is only one node in the tree     
			pass    
		else:
			if node.height != node.max_children_height() + 1:
				raise Exception ("Invalid height for node " + str(node) + ": " + str(node.height) + " instead of " + str(node.max_children_height() + 1) + "!" )
				
			balFactor = node.balance()
			#Test the balance factor
			if not (balFactor >= -1 and balFactor <= 1):
				raise Exception ("Balance factor for node " + str(node) + " is " + str(balFactor) + "!")
			#Make sure we have no circular references
			if not (node.leftChild != node):
				raise Exception ("Circular reference for node " + str(node) + ": node.leftChild is node!")
			if not (node.rightChild != node):
				raise Exception ("Circular reference for node " + str(node) + ": node.rightChild is node!")
			
			if ( node.leftChild ): 
				if not (node.leftChild.parent == node):
					raise Exception ("Left child of node " + str(node) + " doesn't know who his father is!")
				if not (node.leftChild.input_list <=  node.input_list):
					raise Exception ("input_list of left child of node " + str(node) + " is greater than input_list of his parent!")
				self.sanity_check(node.leftChild)
			
			if ( node.rightChild ): 
				if not (node.rightChild.parent == node):
					raise Exception ("Right child of node " + str(node) + " doesn't know who his father is!")
				if not (node.rightChild.input_list >=  node.input_list):
					raise Exception ("input_list of right child of node " + str(node) + " is less than input_list of his parent!")
				self.sanity_check(node.rightChild)
			
	def recompute_heights (self, start_from_node):
		changed = True
		node = start_from_node
		while node and changed:
			old_height = node.height
			node.height = (node.max_children_height() + 1 if (node.rightChild or node.leftChild) else 0)
			changed = node.height != old_height
			node = node.parent
	   
	def add_as_child (self, parent_node, child_node):
		node_to_rebalance = None
		if child_node.input_list < parent_node.input_list:
			if not parent_node.leftChild:
				parent_node.leftChild = child_node
				child_node.parent = parent_node
				if parent_node.height == 0:
					node = parent_node
					while node:
						node.height = node.max_children_height() + 1
						if not node.balance () in [-1, 0, 1]:
							node_to_rebalance = node
							break #we need the one that is furthest from the root
						node = node.parent     
			else:
				self.add_as_child(parent_node.leftChild, child_node)
		else:
			if not parent_node.rightChild:
				parent_node.rightChild = child_node
				child_node.parent = parent_node
				if parent_node.height == 0:
					node = parent_node
					while node:
						node.height = node.max_children_height() + 1
						if not node.balance () in [-1, 0, 1]:
							node_to_rebalance = node
							break #we need the one that is furthest from the root
						node = node.parent       
			else:
				self.add_as_child(parent_node.rightChild, child_node)
		
		if node_to_rebalance:
			self.rebalance (node_to_rebalance)
	
	def insert (self, input_list):
		new_node = Node (input_list)
		if not self.rootNode:
			self.rootNode = new_node
		else:
			if not self.find(input_list):
				self.elements_count += 1
				self.add_as_child (self.rootNode, new_node)
			else:
				self.find(input_list).count=self.find(input_list).count+1
				self.find(input_list).valueslist.append(input_list[3])
		retlst = []
		while node.leftChild:
			node = node.leftChild
		while (node):
			retlst += [node.input_list]
			if (node.rightChild):
				node = node.rightChild
				while node.leftChild:
					node = node.leftChild
			else:
				while ((node.parent)  and (node == node.parent.rightChild)):
					node = node.parent
				node = node.parent
		return retlst

	def find(self, input_list):
		return self.find_in_subtree (self.rootNode, input_list )
	
	def find_in_subtree (self,  node, input_list):
		if node is None:
			return None  # input_list not found
		key=[]
		key.append(input_list[0])
		key.append(input_list[2])
		if key < node.input_list:
			return self.find_in_subtree(node.leftChild, input_list)
		elif key > node.input_list:
			return self.find_in_subtree(node.rightChild, input_list)
		else:  # input_list is equal to node input_list
			return node

	def toString(self, text=None):
		if text is None:
			text = "" 
		if node.leftChild:
			text = self.inorder(node.leftChild, text)
		text += node.toString() 
		if node.rightChild:
			text = self.inorder(node.rightChild, text)
		return text

def rounding(value):
	try:
		if value-math.floor(value)<0.50:
			return math.floor(value)
		else:
			return math.ceil(value)
	except:
		return math.floor(value)

def desCheck(string):
	try:
		n= decimal.Decimal(string)
	except:
		return False
	else:
		if n.as_tuple().exponent==2:
			return True
		else:
			return False

def zipCheck(string):
	try:
		if not string.isalnum() or len(string)<5 or len(string)>9:
			return false
	except:
		return False

def dtCheck(string):
	try:
		if len(string)==8 and ( int(string[0:2])<31 and int(string[0:2])>0) and (int(string[2:4])<12 and int(string[2:4])>0) and int(string[4:])>0 :
			return True
		else:
			return False
	except:
		return False
def unsortedsum(list):
	sum=0
	for i  in range(0,len(list),1):
		sum=sum+list(i)
	return sum


if __name__== "__main__":
	if os.path.isfile('itcont.txt'):
		fil= open(os.path.abspath( "traffic.txt"), "r+")
		try:
			with fil as txt:
				unsorted=[[]]
				dtDB= avlTree()
		except IOError as e:
			print ("I/O error({0}): {1}".format(e.errno, e.strerror))
		except: #handle other exceptions such as attribute errors
			 print ("Unexpected error:"+sys.exc_info()[0])
		else:
			for line in fil: #Iterate over each line in file
				index_of_line=1
				row=[]
				par=line.split("|")#ppartition the line by the pipe.
				if par[15]== None and (par[0].isalnum() and len(par[0])==9) and dtCheck(par[13]) and decCheck(par[14]):#validation
					for i in {0,10,13,14}:
						row.append(par[i])#new lists of important info
						row1=[]#This is dummy variable for rows(candidates) into the median_by_zip
						row2=[]#This is dummy variable for rows(candidates) into the median_by_zip
					if zipCheck(row[1]):#if this line has a well-formed zip then it goes to ou median_by_zip
						row1.append(row[0])
						row1.append(row[1])
						count1=1
						try:
							if len(unsorted)==0: #if the output array has no elements just ad the first element.
								row1.append(row[3])
								row1.append(count1)
								row1.append(row[3])
								unsorted.append(row1)
							else:
								donations1=Heap()#Make a heap for the donations on date and to chairty.
								for i in range(0,len(unsorted),1):
									if row1[0]== unsorted[i][0] and row1[1]==unsorted[i][1]:
										count1=count1+1
										donations1.addNum(float(unsorted[i][3]))
										row1.append(donations1.findMedian())#find the median of donations
										row1.append(count1)
										row1.append(unsortedsum(donations1))#fine the sum
										unsorted[i][2]=row1[2]
								unsorted.append(row1)
						except:
							print("Something went wrong at row "+index_of_line)
					if dtCheck(row[2]):#If the date is well-formed add this line to median_by_dt
						row2.append(row[0])
						row2.append(row[2])
						row2.append(row[3])
						try:
							dtDB.insert(row2)#add our row to theAVtree it will cover everything else
						except:
							print("Something went wrong at row "+index_of_line)
					index_of_line=index_of_line+1
				with open("medianvals_by_zip.txt", "w") as text_file:
					output1=""
					try:
						for i in range(0, len(unsorted),1):
							if(i!=len(unsorted)-1):
								for j in range(0,len(unsorted[i]),1):
									if(j!= len(unsorted[i])-1):
										output1=output1+str((unsorted[i][j]))+"|"
									else:
										output1=output1+str((unsorted[i][j]))+"\n"
							else:
								for j in range(0,len(unsorted[i]),1):
									if(j!= len(unsorted[i])-1):
										output1=output1+str((unsorted[i][j]))+"|"
									else:
										output1=output1+str((unsorted[i][j]))
						text_file.write(output1)
					except:
						print("There was a problem with writing to file")
						text_file.write(output1)
				with open("medianvals_by_date.txt", "w") as text_file:
					try:
						text_file.write(dtDB.toPrint())
					except:
						print("There was a problem with writing to file")
						text_file.write("Oops!")
	else:
		print("The file you gave me is corrupted")
