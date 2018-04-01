import utilities
import stringManipulation as strman
import sys

train_path = sys.argv[1]
test_path = sys.argv[2]
dir_list = strman.chooseRandomClass(train_path)
print('Randomely Chosen classes : ',dir_list)
print('Parsing Train data...')
train_instances, train_class_labels = strman.getAttributesClasses(train_path,dir_list)
print('Finding prior and livelihood...')
prior = utilities.probEvents(train_class_labels)
livelihood = utilities.getLivelihoodTable(train_instances,train_class_labels,prior)
print('Parsing Test data...')
test_instances, test_class_labels = strman.getAttributesClasses(test_path,dir_list)
accuracy = utilities.getAccuracy(train_instances,train_class_labels,livelihood,prior)
print('Accuracy =',accuracy,'%')