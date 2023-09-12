class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    # String representation
    def __str__(self):
        return f"{self.title}\n{self.body}"


post = Post("My post", "The body post...")
print(post)


class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password


class Student(User):
    def __init__(self, name, last_name, email, password):
        # User.__init__(email, password)
        super().__init__(email, password)
        self.name = name
        self.last_name = last_name


student = Student("Leo", "Tosetto", "leonardo.a.tosetto@gmail.com", "123456")

print(student.name, student.email)
