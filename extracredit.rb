# Dr. Taneja
# COMP3220 - 002 : Programming Languages
# Assignment_1

#IAN BROWN 
#EXTRA CREDIT LINKED LIST IMPLEMENTATION 


# Node class for linked list 
class Node
	attr_accessor :next
	attr_accessor :value

	def initialize(value = nil)
		@value = value
		@next = nil
	end 
end

# LinkedList class with operations 
class LinkedList
	attr_accessor :head, :tail, :size
	def initialize
		@head = nil 
		@tail = nil 
		@size = 0
	end 

	# append to LinkedList
    def append(value)
        if @head
            @tail.next = Node.new(value)
            @tail = @tail.next
        else
            @head = Node.new(value)
            @tail = @head
        end
        @size += 1
    end
	
	# append to front of LinkedList
	def append_to_front(value)
		if @head
            node = Node.new(value)
            node.next = @head
            @head = node
		else 
			@head = Node.new(value)
			@tail = @head
        end
        @size += 1
    end

	# check for specific item
	def contain?(value)
		current = @head
		while current 
			return true if current.value == value
			current = current.next
		end
		false 
	end
	
	# remove specific item
	def delete(value)
        current = @head
        prev = nil
        while current
            if current.value == value
                if prev
                    prev.next = current.next
                else
                    @head = current.next
                    @size -= 1
                    return true
                end
            end
            prev = current
            current = current.next 
        end
        return false
	end
	
	#to string and write to file
    def to_s
        string = ""
        current = @head
        while current
		  string += current.value + "\n"
          current = current.next
		end
		File.open("mymovies.txt", "w+") do |f| 
			f.puts string
		end
    end
end 

	


# Database of movies
class Database
	def self.getListOfMovies()
		#adding items from data.txt to linked list
		movie_list = LinkedList.new
		File.open("data.txt").each do |line|
			movie_list.append(line.chomp)
		end
		return movie_list
	end
end

# Search controller class
class SearchController

	attr_accessor :searchSuggestionList

	def self.defaultSearchSuggestionList()
		# Subtask - 1
		@searchSuggestionList = Database.getListOfMovies() 
	end

	def self.getSearchSuggestionList()
		return @searchSuggestionList
	end

	def self.updateList(movieName)
		# Subtask - 3
		movieName = movieName.downcase
		# replaced include, delete, and unshift with 
		# my linked list methods 
		if @searchSuggestionList.contain?(movieName) 
			@searchSuggestionList.delete(movieName)
			@searchSuggestionList.append_to_front(movieName)
		else 
			@searchSuggestionList.append_to_front(movieName)
	end

	def self.saveListToFile()
		#####
		# Subtask - 5 
		#
		# 1.save updated search suggestion list to data.txt file 
		#
		#####
		# calling the linked list to string method which also 
		# writes to file 
		@searchSuggestionList.to_s
	end

end




######
#
# Main starts here
#
######

# Initialize default list ...
SearchController.defaultSearchSuggestionList()

#####
# Subtask - 2 
#
# 1.create endless loop 
# 2.get an input from terminal
# 3.update search suggestion list
# 4.loop should end when user write "exit"
#
#####
puts "Enter search terms, type exit when done: "
mylist_arr = []
while true
	input = gets.chomp
	if input == "exit"
		break
	else 
		SearchController.updateList(input)
		puts "You entered: " + input
		mylist_arr.unshift(input)
	end
end
# writes user input to mylist.txt
File.open("mylist.txt", "w+") do |f|
	f.puts(mylist_arr)
end

#####
# Subtask - 4 
#
# 1.save updated "searchSuggestionList" to data.txt file
#
#####
begin 
	SearchController.saveListToFile() 
rescue NoMethodError
	exit!
end

end

