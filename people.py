# import mem_profile
import meminfo
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


print('Generator Performance:')
# print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
print('\tBefore:')
meminfo.mem_info()
print()

g1 = time.process_time()
people = people_generator(1000000)
g2 = time.process_time()

# print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('\tAfter:')
meminfo.mem_info()
print('Took {:.2f} Seconds'.format(g2 - g1))
print()


print('List Performance:')
print('\tBefore:')
# print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
meminfo.mem_info()
print()

t1 = time.process_time()
people = people_list(1000000)
t2 = time.process_time()

# print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('\tAfter:')
meminfo.mem_info()
print('Took {:.2f} Seconds\n'.format(t2 - t1))
print()
