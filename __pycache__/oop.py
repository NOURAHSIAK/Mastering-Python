class Skill:
    def __init__(self):

        self.skills = ["html", "css", "php"]

    def __str__(self):

        return f"this is my skills => {self.skills}"
    def __len__(self):
        
        return len(self.skills)

profile = Skill()
print(profile)
print(len(profile))
profile.skills.append("python")
profile.skills.append("ux")
print(len(profile))