months = ['Jan','Feb','Mar','Apr']
months.append('May')
months.append('Jul')
print 'Adding May and July :',months
months.insert(5,'Jun')
print 'Current list :' ,months
print 'Index of May is :',months.index('May')
months.remove('Jun')
print 'June is removed.New list is:',months
months.sort()
print 'Sorted Months:',months
months.reverse()
print 'Reversed Months:',months

