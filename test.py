class Me:
    def __init__(self, name, job, hobbies):
        self.name = name
        self.job = job
        self.hobbies = hobbies

    def introduce(self):
        return (
            f"안녕하세요, 저는 {self.name}입니다. "
            f"저는 현재 {self.job}을(를) 하고있습니다. "
            f"취미로는 {', '.join(self.hobbies)}을(를) 즐기고 있습니다."
        )

myself = Me(name="정현", job='파이썬 백엔드 개발자', hobbies=['클라이밍', '게임'])

print(myself.introduce())