import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="college"
)
cur = con.cursor()


def add_student():
    name = input("Enter student name: ")
    city = input("Enter city: ")
    cur.execute("INSERT INTO student(name, city) VALUES(%s, %s)", (name, city))
    con.commit()
    print("Student Added!")


def show_students():
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    for r in rows:
        print(r)


def update_student():
    sid = input("Enter student id to update: ")
    city = input("Enter new city: ")
    cur.execute("UPDATE student SET city=%s WHERE id=%s", (city, sid))
    con.commit()
    print("Student Updated!")


def delete_student():
    sid = input("Enter student id to delete: ")
    cur.execute("DELETE FROM student WHERE id=%s", (sid,))
    con.commit()
    print("Student Deleted!")


while True:
    print("\n1.Add  2.Show  3.Update  4.Delete  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_student()
    elif ch == 2:
        show_students()
    elif ch == 3:
        update_student()
    elif ch == 4:
        delete_student()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
