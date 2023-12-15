class JobPortal:
    def __init__(self):
        self.admin = {'username': 'Lakshmi chandrika', 'password': 'Lucky777'}
        self.students = {}
        self.job_posts = {}

    def login(self, username, password):
        if username == self.admin['username'] and password == self.admin['password']:
            return 'admin'
        elif username in self.students and self.students[username]['password'] == password:
            return 'student'
        
        else:
            return None

    def create_job_post(self, title, description):
        post_id = len(self.job_posts) + 1
        self.job_posts[post_id] = {'title': title, 'description': description}
        return post_id

    def update_job_post(self, post_id, title, description):
        if post_id in self.job_posts:
            self.job_posts[post_id] = {'title': title, 'description': description}
            return True
        else:
            return False

    def delete_job_post(self, post_id):
        if post_id in self.job_posts:
            del self.job_posts[post_id]
            return True
        else:
            return False

    def view_job_posts(self):
        return self.job_posts

    def view_student_details(self, username):
        if username in self.students:
            student_info = self.students[username]
            return f"Name: {student_info['name']}\nMobile: {student_info['mobile']}\nEmail: {student_info['email']}\nSkills: {student_info['skills']}\nExperience: {student_info['experience']} years"
        else:
            return "Student not found"

    def apply_for_job(self, username, post_id):
        if post_id in self.job_posts:
            if username not in self.students:
                return "Student not found"
            if 'applied_posts' not in self.students[username]:
                self.students[username]['applied_posts'] = []
            if post_id not in self.students[username]['applied_posts']:
                name = input("Enter your name: ")
                mobile = input("Enter your mobile number: ")
                email = input("Enter your email: ")
                skills = input("Enter your skills: ")
                experience = input("Enter your experience (in years): ")

                self.students[username]['applied_posts'].append(post_id)
                self.students[username]['name'] = name
                self.students[username]['mobile'] = mobile
                self.students[username]['email'] = email
                self.students[username]['skills'] = skills
                self.students[username]['experience'] = experience
                return "Applied successfully"
            else:
                return "Already applied for this job"
        else:
            return "Job post not found"

    def register_student(self, username, password):
        if username in self.students:
            return "Username already exists"
        self.students[username] = {'username': username, 'password': password}
        return "Student registered successfully"


if __name__ == '__main__':
    job_portal = JobPortal()

    while True:
        print("1. Admin Login")
        print("2. Student Registration")
        print("3. Student Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_username = input("Admin Username: ")
            admin_password = input("Admin Password: ")
            user_type = job_portal.login(admin_username, admin_password)
            if user_type == 'admin':
                while True:
                    print("\nAdmin Menu:")
                    print("1. Create Job Post")
                    print("2. Update Job Post")
                    print("3. Delete Job Post")
                    print("4. View Student Details")
                    print("5. view all students Details")
                    print("6. View Job Posts")
                    print("7. Logout")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == '1':
                        title = input("Enter job title: ")
                        description = input("Enter job description: ")
                        job_portal.create_job_post(title, description)
                        print("Job post created successfully.")
                    elif admin_choice == '2':
                        post_id = int(input("Enter post ID to update: "))
                        title = input("Enter new job title: ")
                        description = input("Enter new job description: ")
                        if job_portal.update_job_post(post_id, title, description):
                            print("Job post updated successfully.")
                        else:
                            print("Job post not found.")
                    elif admin_choice == '3':
                        post_id = int(input("Enter post ID to delete: "))
                        if job_portal.delete_job_post(post_id):
                            print("Job post deleted successfully.")
                        else:
                            print("Job post not found.")
                    elif admin_choice == '4':
                        username = input("Enter student username: ")
                        student_details = job_portal.view_student_details(username)
                        print(student_details)
                    elif admin_choice == '5':
                        student_choice = job_portal.view_student_details()
                        if student_choice:
                            print("\nstudnts : ")
                            for post_id, stu in student_choice.items():
                                print("Hello I am in at line no 130")
                        else:
                            print("line no 132 ")
                    elif admin_choice == '6':
                        job_posts = job_portal.view_job_posts()
                        if job_posts:
                            print("\nJob Posts:")
                            for post_id, post in job_posts.items():
                                print(f"ID: {post_id}, Title: {post['title']}, Description: {post['description']}")
                        else:
                            print("No job posts available.")
                    elif admin_choice == '7':
                        break
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            student_username = input("Student Username: ")
            student_password = input("Student Password: ")
            result = job_portal.register_student(student_username, student_password)
            print(result)
        elif choice == '3':
            student_username = input("Student Username: ")
            student_password = input("Student Password: ")
            user_type = job_portal.login(student_username, student_password)
            if user_type == 'student':
                while True:
                    print("\nStudent Menu:")
                    print("1. View Job Posts")
                    print("2. Apply for a Job")
                    print("3. Logout")
                    student_choice = input("Enter your choice: ")
                    if student_choice == '1':
                        job_posts = job_portal.view_job_posts()
                        if job_posts:
                            print("\nJob Posts:")
                            for post_id, post in job_posts.items():
                                print(f"ID: {post_id}, Title: {post['title']}, Description: {post['description']}")
                        else:
                            print("No job posts available.")
                    elif student_choice == '2':
                        post_id = int(input("Enter the ID of the job post you want to apply for: "))
                        result = job_portal.apply_for_job(student_username, post_id)
                        print(result)
                    elif student_choice == '3':
                        break
            else:
                print("Invalid student credentials.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")