copyfiles:
	cp $(filepath) .

compile-timsort:
	@echo 'Python solution. Nothing to compile.'

run-timsort:
	python3 angular.py $(output-info) < $(input) > $(output-sorted)

list-timsort:
	ls timsort.py

show-timsort:
	@echo 'Showing python file timsort.py'
	cat angular.py

compile-closest:
	javac PointXComparator.java
	javac PointYComparator.java
	javac Point.java
	javac ClosestPoint.java

run-closest:
	java Closest < $(input) > $(output)

list-closest:
	ls *.java

show-closest:
	cat PointXComparator.java
	cat PointYComparator.java
	cat Point.java
	cat ClosestPoint.java