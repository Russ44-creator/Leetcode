import collections

class Solution(object):
    def find_pairs(self, records):
        students = set()
        courseStudent = collections.defaultdict(list)
        for record in records:
            courseStudent[record[1]] += [record[0]]
            students.add(record[0])
        sharedCourse = {}
        students = list(students)
        for i, s1 in enumerate(students):
            for s2 in students[i+1:]:
                sharedCourse[(s1, s2)] = []
        for c, s in courseStudent.items():
            for i, s1 in enumerate(s):
                for s2 in s[i+1:]:
                    if (s1, s2) in sharedCourse:
                        sharedCourse[(s1,s2)] += [c]
                    else:
                        sharedCourse[(s2,s1)] += [c]
        return sharedCourse
    
    def find_midway(self, courses):
        firstCourses = set()
        secondCourses = set()
        hashmap = collections.defaultdict(list)
        for c1, c2 in courses:
            firstCourses.add(c1)
            secondCourses.add(c2)
            hashmap[c1] += [c2]
        starters = firstCourses - secondCourses
        self.paths = []
        res = set()
        def dfs(c, path):
            if c not in hashmap:
                self.paths += [path+[c]]
                return
            for next_c in hashmap[c]:
                dfs(next_c, path+[c])
            return
        for s in list(starters):
            dfs(s, [])
        for p in self.paths:
            res.add(p[(len(p)-1)//2])
        return list(res)
sol = Solution()
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
] 
print(sol.find_pairs(student_course_pairs_1)) # find_pairs(student_course_pairs_1) =>
#{
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
# [17, 94]: []
# [17, 25]: [] #}
student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

 
# find_pairs(student_course_pairs_2) => #{
# [0, 42]: []
# [0, 9]: []
# [9, 42]: [] #}
print(sol.find_pairs(student_course_pairs_2))
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]
print(sol.find_midway(all_courses))
